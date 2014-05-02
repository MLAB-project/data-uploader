#!/usr/bin/python

import urllib2 
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
Version = Configure.Version


def IsConnected():
    try:
        urllib2.urlopen("http://space.astro.cz/").close()
    except urllib2.URLError:
        return False
    else:
        return True

def UploadTo(location):
	f = open('Log-RMDS-py','a')
	f.write('SYNC.PY\t|| Zacatek synchronizace - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
	if not os.path.exists(path+path_audio):
		print  "\t\t SYNC.PY >>", "Audio sort path ", path_sort+path_audio, " does NOT EXIST"
		f.write('SYNC.PY\t||  >> audio sort path ' + path_sort + path_audio + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path+path_data):
		print  "\t\t SYNC.PY >>", "Data sort path ", path_sort+path_data, " does NOT EXIST"
		f.write('SYNC.PY\t||  >> data sort path ' + path_sort + path_data + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path+path_image):
		print  "\t\t SYNC.PY >>", "Image sort path ", path_sort+path_image, " does NOT EXIST"
		f.write('SYNC.PY\t||  >> image sort path ' + path_sort + path_image + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	f.write('SYNC.PY\t||  >>    Zacatek Uploadu\n') # rsync -vvarz ./../MetData/ZVPP/Sort/data/ ZVPP@space.astro.cz:/storage/meteors/ZVPP/ZVPP-R1/data
	os.system("rsync -vvarz " + path_sort + path_audio + " " + location + Station + "/ZVPP-R1/audio")
	os.system("rsync -vvarz " + path_sort + path_data  + " " + location + Station + "/ZVPP-R1/data")
	os.system("rsync -vvarz --exclude='*/*'" + path_sort + " " + location + Station + "/ZVPP-R1/")
	os.system("timeout 1700 rsync -vvarz " + path_sort + path_image + " " + location + Station + "/ZVPP-R1/capture") # 1700s = 28,3333min
	f.write('SYNC.PY\t||  >>    Konec sync.py - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
	f.close()
 
def main():
	InternetAviable = IsConnected()
	if InternetAviable == True:
		print "LINK ESTABLISHED"
		UploadTo("ZVPP@space.astro.cz:/storage/bolidozor/")
	else:
		f = open('Log-RMDS-py','a')
		f.write('SYNC.PY\t|| Internet connection is NOT aviable' + '\n')
		f.close()
		print "LINK DESTROYED!!!"

if __name__ == "__main__":
	main()
