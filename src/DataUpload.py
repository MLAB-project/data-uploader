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
        remoteBasePath = os.path.join(value["storage_stationpath"], value["storage_username"], value["origin"])

        #navazani ssh spojeni pomoci ssh klice a username z cfg souboru
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(value["storage_hostname"], username = value["storage_username"])
        sftp = ssh.open_sftp()

        if value["project"] == "bolidozor":
            #TODO: udelat lepsi zpusob ziskani cest z config souboru

            sync_folders.append(value["configurations"][0]["children"][0]["metadata_path"])
            sync_folders.append(value["configurations"][0]["children"][0]["children"][0]["output_dir"])
            sync_folders.append(value["configurations"][0]["children"][0]["children"][1]["output_dir"])
            sync_folders.append(value["project_home_folder"])

        elif value["project"] == "ionozor":
            sync_folders.append(value["configurations"][1]["children"][0]["children"][0]["output_dir"])
            sync_folders.append(value["project_home_folder"])

        elif value["project"] == "meteo":
            sync_folders.append(value["configurations"][0]["children"][0]["metadata_path"])
            sync_folders.append(value["project_home_folder"])

        elif value["project"] == "geozor":
            sync_folders.append(value["data_path"])
            sync_folders.append(value["project_home_folder"])


        else:
            print "Uknown project."

        for i, folder in enumerate(sync_folders):
            print i, folder
            TimeStartFolder = time.time()
            filelist = os.listdir(folder)
            for i2, file in enumerate(filelist):
                try:
                    remote_path = None
                    local_path = os.path.join(folder,file)
                    if any(x in file for x in ["meta.csv", "freq.csv", "data.csv"]):
                        remote_path = os.path.join(remoteBasePath, os.path.basename(folder), "data", file[0:4], file[4:6], file[6:8], file)

                    elif any(x in file for x in ["snap.fits"]):
                        remote_path = os.path.join(remoteBasePath, os.path.basename(folder), "snapshots", file[0:4], file[4:6], file[6:8], file[8:10], file)

                    elif any(x in file for x in ["met.fits","raws.fits"]):
                        remote_path = os.path.join(remoteBasePath, os.path.basename(folder), "meteors", file[0:4], file[4:6], file[6:8], file[8:10], file)

                    elif "station" in os.path.dirname(folder) and os.path.isfile(local_path):
                        print "file in station folder:", file
                        remote_path = os.path.join(remoteBasePath, file)

                    else:
                        print os.path.dirname(folder),
                        print "Skipped:", folder, file

                    if remote_path:
                        print local_path, remote_path
                        # zkontrolovat jestli existuje slozka na remote server
                        try:
                            sftp.chdir(os.path.dirname(remote_path))
                        except IOError:
                            # popripade ji vytvorit
                            print "create folder:", os.path.dirname(remote_path)
                            #sftp.mkdir(os.path.dirname(remote_path)+ "/") # touto cesto nelze vytvorit vice slozek zaroven TODO: otestovat jine moznosti
                            ssh.exec_command('mkdir -p ' + repr(os.path.dirname(remote_path)) + "/" )
                        sftp.put(local_path, remote_path)

                        # ziskani kontrolnich souctu na remote serveru a lokalnich souboru
                        stdin_remote, stdout_remote, stderr_remote = ssh.exec_command("md5 -q "+ remote_path)
                        md5_remote = stdout_remote.read()
                        md5 = hashlib.md5(open(local_path, 'rb').read()).hexdigest()

                        #print md5_remote, md5
                        if md5 in md5_remote and "station" not in os.path.basename(os.path.normpath(folder)): # na konci md5_remote je odradkovani, kontrola, zdali nejde o soubor v /bolidozor/stotion
                            self.UploadEvent(remote_path, md5)
                            if ".csv" not in local_path:
                                os.remove(local_path)
                                print "removed"
                            elif os.path.getmtime(local_path) < time.time() - 4000: # Mazou se soubory starsi nez 4000 sekund, ochrana pred smazanim dat, do kterych se zapisuje prubezne
                                os.remove(local_path)
                                print "removed older file"
                            else:
                                print "will be removed"
                        else:
                            print "Unable to send", os.path.basename(os.path.normpath(folder)), md5_remote, md5 in md5_remote
                        
                except Exception, e:
                    print "Write error" + repr(e)

        sftp.close()
        ssh.close()

    def UploadEvent(self, file, md5):
        path, file = os.path.split(file)
        payload = {
            'filelocation':  path,
            'filename': file,
            'filename_original':  file,
            'checksum': md5,
            'station': self.value["origin"],
            'server': 5,
            'uploadtime': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        print payload
        try:
            r = requests.get('http://api.vo.mlab.cz/upload/%s/' %(self.value["project"]), params=payload)
            pass
        except Exception, e:
            print e

