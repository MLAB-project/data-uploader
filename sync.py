#!/usr/bin/python

import os
import shutil
from time import gmtime, strftime
import Configure

Station = Configure.Station
path = Configure.path
path_audio = Configure.path_audio
path_image = Configure.path_image
path_data = Configure.path_data
path_sort = Configure.path_sort
refresh = Configure.refresh
Version = Configure.Version


f = open('Log-sync-py','a')
f.write('SYNC.PY || Zacatek synchronizace - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
if not os.path.exists(path+path_audio):
	print  "\t\t SYNC.PY >>", "Audio sort path ", path_sort+path_audio, " does NOT EXIST"
	f.write('SYNC.PY ||  >> audio sort path ' + path_sort + path_audio + " does NOT EXIST" +'\n')
	f.close()
	exit(0)
if not os.path.exists(path+path_data):
	print  "\t\t SYNC.PY >>", "Data sort path ", path_sort+path_data, " does NOT EXIST"
	f.write('SYNC.PY ||  >> data sort path ' + path_sort + path_data + " does NOT EXIST" +'\n')
	f.close()
	exit(0)
if not os.path.exists(path+path_image):
	print  "\t\t SYNC.PY >>", "Image sort path ", path_sort+path_image, " does NOT EXIST"
	f.write('SYNC.PY ||  >> image sort path ' + path_sort + path_image + " does NOT EXIST" +'\n')
	f.close()
	exit(0)
f.write(' >>    Zacatek Uploadu\n')
os.system("rsync -vvarz --rsh='ssh -p2223' " + path_sort + path_audio + " meteor@meteor1.astrozor.cz:meteors/" + Station + "/audio")
os.system("rsync -vvarz --rsh='ssh -p2223' " + path_sort + path_data  + " meteor@meteor1.astrozor.cz:meteors/" + Station + "/data")
os.system("rsync -vvarz --rsh='ssh -p2223' " + path_sort + path_image + " meteor@meteor1.astrozor.cz:meteors/" + Station + "/capture")
f.write(' >>    Konec sync.py - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
f.close()
