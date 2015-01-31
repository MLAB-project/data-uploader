#!/usr/bin/python

import os, sys
import shutil
import time
from time import gmtime, strftime
from datetime import date
import config

Station = config.Station
path = config.path
path_audio = config.path_audio
path_image = config.path_image
path_data = config.path_data
path_sort = config.path_sort
Version = config.Version

def SortRadObs():
	list = os.listdir(config.path+config.path_data)
	for soubor in list:
		if soubor[:1] is not ".":
			path_local = config.path_sort+config.path_data+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"
			print path_local + soubor
			f = os.path.getmtime(config.path+config.path_data+soubor)
			t = time.time()
			if not os.path.exists(path_local):
				os.makedirs(path_local)
			if int(t-f) > 5400: # pokud je starsi nez 1,5 hodiny
				print "move"
				shutil.move(config.path+config.path_data+soubor, path_local+soubor)
			else:
				print "copy, delta t=", int(t-f)
				shutil.copy2(config.path+config.path_data+soubor, path_local+soubor)
	list = os.listdir(config.path+config.path_audio)
	for soubor in list:
	    if soubor[:1] is not ".":
		    path_local = config.path_sort+config.path_audio+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"+soubor[8:10]+"/"
		    print path_local + soubor
		    if not os.path.exists(path_local):
		        os.makedirs(path_local)
		    shutil.move(config.path+config.path_audio+soubor, path_local+soubor)
	list = os.listdir(config.path+config.path_image)
	for soubor in list:
	    if soubor[:1] is not ".":
		    path_local = config.path_sort+config.path_image+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"+soubor[8:10]+"/"
		    print path_local + soubor
		    if not os.path.exists(path_local):
				os.makedirs(path_local)
		    shutil.move(config.path+config.path_image+soubor, path_local+soubor)
	list = os.listdir(config.path)
        for soubor in list:
	    print "!!!!-----! " + soubor	
            if  os.path.isfile(config.path+soubor):
		path_local = config.path_sort
		shutil.copy2(config.path+soubor, config.path_sort+soubor)
	global SortEnd
	SortEnd = False



def main():
	global SortEnd
	SortEnd = True
	while SortEnd:
		try:
			SortRadObs()
		except Exception, e:
			print "ERROR in SORT.PY", e

	print "\t\t SORT.PY >>", strftime("%d %b %Y %H:%M:%S", gmtime()), " Konec\n"
if __name__ == "__main__":
	main()
