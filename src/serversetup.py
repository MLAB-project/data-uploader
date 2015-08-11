#!/usr/bin/python

import os
import shutil
from time import gmtime, strftime
import config
import subprocess
import pipes


def existsfile(host, path):
	exist = subprocess.Popen(['ssh', host, 'test -e %s' % pipes.quote(path)])
	exist.wait()
	return exist.returncode == 0

def createfile(host, path):
	exist = subprocess.call('ssh ' + host + ' \"mkdir ' + path + ' \" ' , shell=True)
	return 0
      

def main():
	f = open('Log-RMDS-py','a')
	f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Zacatek server setup \n')
	if config.Version is "Bolidozor_14" or config.Version is "RadObs_14_7":
		if not existsfile(config.UserSpace + "@space.astro.cz", "/storage/bolidozor/" + config.UserSpace + "/" +   config.StationSpace + "/"):
			print "slozka " + config.path_data + " neexistuje"
			f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' slozka ' + config.path_data + ' neexistuje \n')
			createfile(config.UserSpace + "@space.astro.cz", "/storage/bolidozor/" + config.UserSpace + "/" +   config.StationSpace + "/" + config.path_data)
		else:
			print "slozka " + config.path_data + " existuje"
		if not existsfile(config.UserSpace + "@space.astro.cz", "/storage/bolidozor/" + config.UserSpace + "/" +   config.StationSpace + "/"+ config.path_image):
			print "slozka  " + config.path_image + " neexistuje"
			f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' slozka ' + config.path_image + ' neexistuje\n')
			createfile(config.UserSpace + "@space.astro.cz", "/storage/bolidozor/" + config.UserSpace + "/" +   config.StationSpace + "/"+ config.path_image)
		else:
			print "slozka " + config.path_image + " existuje"
		if not existsfile(config.UserSpace + "@space.astro.cz", "/storage/bolidozor/" + config.UserSpace + "/" +   config.StationSpace + "/"+ config.path_audio):
			print "slozka " + config.path_audio + " neexistuje"
			f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' slozka ' + config.path_audio + ' neexistuje \n')
			createfile(config.UserSpace + "@space.astro.cz", "/storage/bolidozor/" + config.UserSpace + "/" +   config.StationSpace + "/"+ config.path_audio)
		else:
			print "slozka " + config.path_audio + " existuje"
	f.write('SERVERSETUP.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Konec server setup \n')
	f.close()
			
		
	print "\t\t SERVERSETUP.PY >>", strftime("%d %b %Y %H:%M:%S", gmtime()), " Konec\n"

if __name__ == "__main__":
	main()
