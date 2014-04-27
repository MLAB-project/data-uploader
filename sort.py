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
Version = Configure.Version


def sort(file, name):
	shutil.copy2(path+"station.cfg", path_sort+"station.cfg")
	if file=="audio":
		soubor=path+path_audio
		soubor_new=path_sort+path_audio+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"
		print "\t\t SORT.PY >>", soubor_new
		if not os.path.exists (soubor_new):
			os.makedirs(soubor_new)
		os.rename(soubor+name,soubor_new+name)
	elif file=="image":
		print "\t\t SORT.PY >>", "obr"
		soubor=path+path_image
		soubor_new=path_sort+path_image+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"+name[:+10][-2:]+"/"
		print "\t\t SORT.PY >>", soubor_new
		if not os.path.exists(soubor_new):
			os.makedirs(soubor_new)
		os.rename(soubor+name,soubor_new+name)
	elif file=="data":
		print "\t\t SORT.PY >>", "data"
		soubor=path+path_data
		soubor_new=path_sort+path_data+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"
		print "\t\t SORT.PY >>", soubor_new
		if not os.path.exists(soubor_new):
			os.makedirs(soubor_new)
		if not name == strftime("%Y%m%d%H", gmtime()) + "_" + Station + ".dat":
			os.rename(soubor+name,soubor_new+name)
		else:
			print "\t\t SORT.PY >>", "##### Soubor: '" + strftime("%Y%m%d%H", gmtime()) + "_" + Station + ".dat" + "' byl preskocen"
			shutil.copy2(soubor+name, soubor_new+name)
		#print "\t\t SORT.PY >>", "DATUM ----------------------------DATUM --------DATUM --------DATUM --------DATUM --------"
	elif file=="config":
		shutil.copy2(path+name, path_sort+name)


def sortall():
	f = open('Log-RMDS-py','a')
	if not os.path.exists(path+path_audio):
		print  "\t\t SORT.PY >>", "Audio source path ", path+path_audio, " does NOT EXIST"
		f.write('SORT.PY\t||  >> audio source path ' + path + path_audio + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path+path_data):
		print  "\t\t SORT.PY >>", "Data source path ", path+path_data, " does NOT EXIST"
		f.write('SORT.PY\t||  >> data source path ' + path + path_data + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path+path_image):
		print  "\t\t SORT.PY >>", "Image source path ", path+path_image, " does NOT EXIST"
		f.write('SORT.PY\t||  >> image source path ' + path + path_image + " does NOT EXIST" +'\n')
		f.close()
		exit(0)


	f.write('SORT.PY\t|| Zacatek Sortingu - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
	dirList=os.listdir(path+path_audio)
	print "\t\t SORT.PY >>", "----------------------------------- Audio sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if   fname[-4:]==".wav":
			sort("audio", fname)
			print "\t\t SORT.PY >>", "++++ zvuk wav"
		elif fname[-4:]==".aux":
			print "\t\t SORT.PY >>", "++++ zvuk aux"
			sort("audio", fname)

	dirList=os.listdir(path+path_data)
	print "\t\t SORT.PY >>", "----------------------------------- Data sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if fname[-4:]==".dat":
			print "\t\t SORT.PY >>", "++++ data"
			sort("data", fname)

	dirList=os.listdir(path)
	print "\t\t SORT.PY >>", "----------------------------------- Config sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if fname[-4:]==".cfg":
			print "\t\t SORT.PY >>", "++++ config"
			sort("config", fname)

	dirList=os.listdir(path+path_image)
	print "\t\t SORT.PY >>", "----------------------------------- Image sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if fname[-4:]==".jpg":
			print "\t\t SORT.PY >>", "++++ obrazek"
			sort("image", fname)
	f.write('SORT.PY\t||  >>  Konec sort.py - ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '\n')
	f.close()


def main():
	sortall()

if __name__ == "__main__":
	main()