#!/usr/bin/python

import urllib2 
import os
import shutil
from time import gmtime, strftime
import config

Station = config.Station
path = config.path
path_audio = config.path_audio
path_audio_sort = config.path_audio_sort
path_image = config.path_image
path_image_sort = config.path_image_sort
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

def UploadTo(location, SyncEnd):
	f = open('Log-RMDS-py','a')
	f.write('SYNC.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Start of synchronisation \n')
	if not os.path.exists(path_audio_sort):
		print  "\t\t SYNC.PY >>", "Audio sort path ", path_audio_sort, " does NOT EXIST"
		f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '  >> audio sort path ' + path_audio_sort + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path_sort):
		print  "\t\t SYNC.PY >>", "Data sort path ", path_sort, " does NOT EXIST"
		f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' >> data sort path '  +  path_sort  +  " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path_image_sort):
		print  "\t\t SYNC.PY >>", "Image sort path ", path_image_sort, " does NOT EXIST"
		f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' >> image sort path ' + path_image_sort + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '\t >>   Start of Upload\n')

	print "paths for SNAP:", path_image_sort, location+config.UserSpace+'/'+config.StationSpace
	os.system("timeout 1000 rsync -vaz --remove-source-files " + path_image_sort[:-1] + " " + location + config.UserSpace + "/" +   config.StationSpace)

        print "paths for RAW:", path_audio_sort, location+config.UserSpace+'/'+config.StationSpace
	os.system("timeout 1000 rsync -vaz --remove-source-files " + path_audio_sort[:-1] + " " + location + config.UserSpace + "/" +   config.StationSpace)

        print "paths for CSV:", path_sort, location+config.UserSpace+ '/' + config.StationSpace
	os.system("timeout 1000 rsync -vaz --remove-source-files " + path_sort[:-1]  + " " + location + config.UserSpace + "/" +   config.StationSpace )
	
	print "paths for CFG:", path_image_sort, location+config.UserSpace+'/'+config.StationSpace
	os.system("timeout 100  rsync -vazd --exclude='*/' /home/odroid/bolidozor/station/ "+ location+config.UserSpace +"/"+ config.StationSpace ) # 1700s = 28,3333min
#	f.write('SYNC.PY\t\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + '\t >>    Finish of upload \n')

#	print("timeout 1000 rsync -vaz --remove-source-files " + path_image_sort + " " + location + config.UserSpace + "/" +   config.StationSpace +"/" )


	f.close()
	print "SYNC.PY \t|| ", strftime("%d %b %Y %H:%M:%S", gmtime()), " Synchronisation was finished!"
	#global SyncEnd
	SyncEnd = True
	return SyncEnd

 

 
def main():
	SyncEnd = False
	ErrMax = 10
	ErrCount = 0
	while SyncEnd != True:
		try:
			InternetAviable = IsConnected()
			if InternetAviable:
				print "Pripojeno", strftime("%d %b %Y %H:%M:%S", gmtime())
				SyncEnd = UploadTo(config.UserName + "@space.astro.cz:/storage/bolidozor/", SyncEnd)

			else:
				f = open('Log-RMDS-py','a')
				f.write('SYNC.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Internet connection is NOT available' + '\n')
				f.close()
				print "Internet connection is NOT available", strftime("%d %b %Y %H:%M:%S", gmtime())
		except Exception, e:
			print "ERROR in SYNC.PY", e
	ErrCount += 1
	if ErrCount >= ErrMax:
		SyncEnd = True
		print "Chyb ERR,", ErrCount
		
if __name__ == "__main__":
	main()
