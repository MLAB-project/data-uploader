#!/usr/bin/python

import urllib2 
import os
import shutil
from time import gmtime, strftime
import config

Station = config.Station
path = config.path
path_audio = config.path_audio
path_image = config.path_image
path_data = config.path_data
path_sort = config.path_sort
Version = config.Version


def IsConnected():
    try:
        urllib2.urlopen("http://space.astro.cz/").close()
    except urllib2.URLError:
        return False
    else:
        return True

def UploadTo(location):
	f = open('Log-RMDS-py','a')
	f.write('SYNC.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Start of synchronisation \n')
	if not os.path.exists(path_sort+path_audio):
		print  "\t\t SYNC.PY >>", "Audio sort path ", path_sort+path_audio, " does NOT EXIST"
		f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '  >> audio sort path ' + path_sort + path_audio + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path_sort+path_data):
		print  "\t\t SYNC.PY >>", "Data sort path ", path_sort+path_data, " does NOT EXIST"
		f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' >> data sort path ' + path_sort + path_data + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path_sort+path_image):
		print  "\t\t SYNC.PY >>", "Image sort path ", path_sort+path_image, " does NOT EXIST"
		f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' >> image sort path ' + path_sort + path_image + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '\t >>   Start of Upload\n')
	#print "-------"+"rsync -vvarz --exclude='*/*'" + path_sort + path_image + " " + location + config.UserSpace + "/" +   config.StationSpace + "/"+config.path_image
	#print "-------"+"rsync -vvarz --exclude='*/*'" + path_sort + path_data  + " " + location + config.UserSpace + "/" +   config.StationSpace + "/"+config.path_data
	#print "-------"+"rsync -vvarz --exclude='*/*'" + path_sort + " " + location + config.UserSpace + "/" + config.StationSpace + "/"
	#print "-------"+"timeout 1000 rsync -vvarz --exclude='*/*'" + path_sort + path_audio + " " + location + "/" + config.UserSpace + "/" + config.StationSpace + "/"+config.path_audio
	os.system("rsync -vvarz --exclude='*/*'" + path_sort + path_image + " " + location + config.UserSpace + "/" +   config.StationSpace + "/"+config.path_image)
	os.system("rsync -vvarz --exclude='*/*'" + path_sort + path_data  + " " + location + config.UserSpace + "/" +   config.StationSpace + "/"+config.path_data)
	os.system("rsync -vvarz --exclude='*/*'" + path_sort + " " + location + config.UserSpace + "/" + config.StationSpace + "/")
	os.system("timeout 1000 rsync -vvarz --exclude='*/*'" + path_sort + path_audio + " " + location + "/" + config.UserSpace + "/" + config.StationSpace + "/"+config.path_audio) # 1700s = 28,3333min
	f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '\t >>    Finish of upload \n')
	f.close()
	print "SYNC.PY \t|| ", strftime("%d %b %Y %H:%M:%S", gmtime()), " Synchronisation was finished!"
	global SyncEnd
	SyncEnd = False

 

 
def main():
	global SyncEnd
	SyncEnd = True
	while SyncEnd:
		try:
			InternetAviable = IsConnected()
			if InternetAviable:
				print "Pripojeno", strftime("%d %b %Y %H:%M:%S", gmtime())
				UploadTo(config.UserName + "@space.astro.cz:/storage/bolidozor/")

			else:
				f = open('Log-RMDS-py','a')
				f.write('SYNC.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Internet connection is NOT available' + '\n')
				f.close()
				print "Internet connection is NOT available", strftime("%d %b %Y %H:%M:%S", gmtime())
		except Exception, e:
			print "ERROR in SYNC.PY", e
		
if __name__ == "__main__":
	main()
