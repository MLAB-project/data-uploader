#import json
from mlabutils import ejson
import time
import os
import subprocess
import paramiko
import hashlib
import requests

class dataUpload():
    def __init__(self, argv):
        self.configFile = argv[1]

    def start(self):
        print "started OK"

        print self.configFile
        parser = ejson.Parser()
        value = parser.parse_file(self.configFile)
        self.value = value

        sync_folders = []
        neindexovano = []

        #navazani ssh spojeni pomoci ssh klice a username z cfg souboru
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(value["storage_hostname"], username = value["storage_username"])
        sftp = ssh.open_sftp()

        self.seyHelloo() #zaregistruje se do RTbolidozoru

        if value["project"] == "bolidozor":
            #TODO: udelat lepsi zpusob ziskani cest z config souboru

            sync_folders.append(value["configurations"][0]["children"][0]["metadata_path"])
            sync_folders.append(value["configurations"][0]["children"][0]["children"][0]["output_dir"])
            sync_folders.append(value["configurations"][0]["children"][0]["children"][1]["output_dir"])
            sync_folders.append(value["project_home_folder"])
            remoteBasePath = os.path.join(value["storage_stationpath"], value["storage_username"], value["configurations"][0]["children"][0]["origin"])

        elif value["project"] == "ionozor":
            sync_folders.append(value["configurations"][0]["children"][0]["metadata_path"])
            sync_folders.append(value["configurations"][1]["children"][0]["children"][0]["output_dir"])
            sync_folders.append(value["project_home_folder"])
            remoteBasePath = os.path.join(value["storage_stationpath"], value["storage_username"], value["configurations"][0]["children"][0]["origin"])

        elif value["project"] == "meteo":
            sync_folders.append(value["configurations"][0]["children"][0]["metadata_path"])
            sync_folders.append(value["project_home_folder"])
            remoteBasePath = os.path.join(value["storage_stationpath"], value["storage_username"], value["origin"])

        elif value["project"] == "geozor":
            sync_folders.append(value["data_path"])
            sync_folders.append(value["project_home_folder"])
            remoteBasePath = os.path.join(value["storage_stationpath"], value["storage_username"], value["origin"])


        else:
            print "Uknown project."

        for i, folder in enumerate(sync_folders):
            print i, folder
            TimeStartFolder = time.time()
            filelist = os.listdir(folder)
            for i2, file in enumerate(filelist):
                try:
                    remote_path = None
                    remove = False# 0 - neodstranovat, 1- odstranit po odeslani, 2 - odstranit po hodine a odeslani
                    local_path = os.path.join(folder,file) # cesta k souboru na stanici
                    type_folder = os.path.basename(os.path.normpath(folder)) # tato promena obsahuje hodnoty jako 'snapshots, meteors, data' (podslozka v rootu stanice)
                    if any(x in file for x in ["meta.csv", "freq.csv", "data.csv"]):
                        remote_path = os.path.normpath(remoteBasePath, type_folder, file[0:4], file[4:6], file[6:8], file)
                        remove = 2

                    elif any(x in file for x in ["data.tsv"]):
                        remote_path = os.path.normpath(remoteBasePath, type_folder, file[0:4], file[4:6], file)
                        remove = 2

                    elif any(x in file for x in ["snap.fits"]):
                        remote_path = os.path.join(remoteBasePath, type_folder, file[0:4], file[4:6], file[6:8], file[8:10], file)
                        remove = 1

                    elif any(x in file for x in ["met.fits","raws.fits"]):
                        remote_path = os.path.join(remoteBasePath, type_folder, file[0:4], file[4:6], file[6:8], file[8:10], file)
                        remove = 1

                    elif "station" in os.path.dirname(folder) and os.path.isfile(local_path):
                        print "file in station folder:", file
                        remote_path = os.path.join(remoteBasePath, file)
                        remove = 0

                    else:
                        print os.path.dirname(folder),
                        print "Skipped:", folder, file

                    if remote_path:
                        print local_path, remote_path
                        # zkontrolovat jestli existuje slozka na remote server, pokud ne - vytvorit ji
                        try:
                            sftp.chdir(os.path.dirname(remote_path))
                        except IOError:
                            print "create folder:", os.path.dirname(remote_path)
                            ssh.exec_command('mkdir -p ' + repr(os.path.dirname(remote_path)) + "/" )
                        
                        # odeslat soubor na space
                        sftp.put(local_path, remote_path)

                        # ziskani kontrolnich souctu md5 na remote serveru a z lokalnich souboru
                        stdin_remote, stdout_remote, stderr_remote = ssh.exec_command("md5 -q "+ remote_path)
                        md5_remote = stdout_remote.read()
                        md5 = hashlib.md5(open(local_path, 'rb').read()).hexdigest()

                        #print md5_remote, md5
                        if not (md5 in md5_remote): # na konci md5_remote je odradkovani, kontrola, zdali nejde o soubor v /bolidozor/station
                            print "soubor se nepodarilo odeslat na server", os.path.basename(os.path.normpath(folder)), md5_remote, md5 in md5_remote
                        else:
                            #TODO: overeni, jestli se jedna o data, nebo o soubory ve slozce /station/ se musi delat v api na blackhole
                            status = self.UploadEvent(remote_path, md5)
                            if status == 1:
                                if remove ==1:
                                    os.remove(local_path)
                                    print "removed"
                                elif remove == 2 and os.path.getmtime(local_path) < time.time() - 4000: # Mazou se soubory starsi nez 4000 sekund, ochrana pred smazanim dat, do kterych se zapisuje prubezne
                                    os.remove(local_path)
                                    print "removed older file"
                                else:
                                    print "Soubor zustava na stanici (neodstranuje se)"
                            else:
                                neindexovano += [status]

                        print neindexovano

                        
                except Exception, e:
                    print "Write error" + repr(e)

        sftp.close()
        ssh.close()

    def seyHelloo(self):
        value = self.value
        print "SEY HELLO!!!"
        print value['observatory']
        payload = {
            'observatory_name': value['observatory'][0]['name'],
            'observatory_owner_login': value['observatory'][0]['owner.login'],
            'observatory_lat': value['observatory'][0]['lat'],
            'observatory_lon': value['observatory'][0]['lon'],
            'observatory_alt': value['observatory'][0]['alt'],
            'observatory_location': value['observatory'][0]['location'],
            'station': self.value["configurations"][0]["children"][0]["origin"],
            'hw_version': value['HWversion']
        }
        print payload
        try:
            r = requests.get('http://vo.astro.cz/api/hello/%s/' %(value["project"]), params=payload, timeout = 5)
            return True
        except Exception, e:
            print e, e[0]
            print "ERR, UNABLE TO SAY HELLO"
            return False

    def UploadEvent(self, file, md5):
        path, file = os.path.split(file)
        payload = {
            'filelocation':  path,
            'filename': file,
            'filename_original':  file,
            'checksum': md5,
            'station': self.value["configurations"][0]["children"][0]["origin"],
            'server': 1,
            'uploadtime': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        print payload
        try:
            r = requests.get('http://vo.astro.cz/api/upload/%s/' %(self.value["project"]), params=payload, timeout=2)
            return 1
        except Exception, e:
            print e
            return payload

