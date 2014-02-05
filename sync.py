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


def sort(file, name):
	if file=="sync.log":
		soubor=path+path_audio
		soubor_new=path_sort+path_audio+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"
		print soubor_new
		if not os.path.exists (soubor_new):
			os.makedirs(soubor_new)
		os.rename(soubor+name,soubor_new+name)
	elif file=="image":
		print "obr"
		soubor=path+path_image
		soubor_new=path_sort+path_image+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"+name[:+10][-2:]+"/"
		print soubor_new
		if not os.path.exists(soubor_new):
			os.makedirs(soubor_new)
		os.rename(soubor+name,soubor_new+name)
	elif file=="data":
		print "data"
		soubor=path+path_data
		soubor_new=path_sort+path_data+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"
		print soubor_new
		if not os.path.exists(soubor_new):
			os.makedirs(soubor_new)
		if not name == strftime("%Y%m%d%H", gmtime()) + "_" + Station + ".dat":
			os.rename(soubor+name,soubor_new+name)
		else:
			print "##### Soubor: '" + strftime("%Y%m%d%H", gmtime()) + "_" + Station + ".dat" + "' byl preskocen"
			shutil.copy2(soubor+name, soubor_new+name)
		#print "DATUM ----------------------------DATUM --------DATUM --------DATUM --------DATUM --------"
		#print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
		#print strftime("%Y", gmtime())
		#print strftime("%m", gmtime())
		#print strftime("%d", gmtime())
		#print strftime("%H", gmtime())
		#print strftime("%Y%m%d%H", gmtime())
		
def sync():
	f = open('Log-sync-py','a')
	f.write('Zacatek Sortingu - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
	dirList=os.listdir(path+path_audio)
	print "----------------------------------- Audio sorting"
	for fname in dirList:
		print fname
		if   fname[-4:]==".wav":
			sort("audio", fname)
			print "++++ zvuk wav"
		elif fname[-4:]==".aux":
			print "++++ zvuk aux"
			sort("audio", fname)
	dirList=os.listdir(path+path_data)
	print "----------------------------------- Data sorting"
	for fname in dirList:
		print fname
		if fname[-4:]==".dat":
			print "++++ data"
			sort("data", fname)
	dirList=os.listdir(path+path_image)
	print "----------------------------------- Image sorting"
	for fname in dirList:
		print fname
		if fname[-4:]==".jpg":
			print "++++ obrazek"
			sort("image", fname)
	f.write(' >>    Zacatek Uploadu\n')
	os.system("rsync -vvarz --rsh='ssh -p2223' " + path_sort + path_audio + " meteor@meteor1.astrozor.cz:meteors/" + Station + "/audio")
	os.system("rsync -vvarz --rsh='ssh -p2223' " + path_sort + path_data  + " meteor@meteor1.astrozor.cz:meteors/" + Station + "/data")
	os.system("rsync -vvarz --rsh='ssh -p2223' " + path_sort + path_image + " meteor@meteor1.astrozor.cz:meteors/" + Station + "/capture")
	f.write(' >>    Konec sync.py - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
	f.close()

if __name__ == "__main__":
	sync()