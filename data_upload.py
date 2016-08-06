#!/usr/bin/python

import sys
import threading
import time
from time import gmtime, strftime
from src import sort
from src import sync
import subprocess
import time


TimeVarSort = 0.0000
TimeVarSync = 0.0000

def FuncSort():
	print "\n\n==================================================\nStarting Sort\n\n"
	sort.main()
	subprocess.Popen(["python","./src/sort.py"])

def FuncSync():
	print "\n\n==================================================\nStarting Sync\n\n"
	sync.main()
	subprocess.Popen(["python","./src/sync.py"])

def FuncServerSetup():
	print "\n\n==================================================\nStarting Server Setup\n\n"
	sync.main()
	subprocess.Popen(["python","./src/serversetup.py"])

def FuncDiskGuard():
	print "\n\n==================================================\nStarting DiskGuard\n\n"
	sync.main()
	subprocess.Popen(["python","./src/DiskGuard.py"])



def EverySec(period, timeVar, func):
	if timeVar+period <= time.time():
		timeVar = time.time()
		print ("local \t\t",timeVar)
		if func == "Sort":
			FuncSort()
		elif func == "Sync":
			FuncSync()
		elif func == "DiskGuard":
			FuncDiskGuard()
	return timeVar



if __name__ == "__main__":
	if len(sys.argv) != 2:
	    sys.stderr.write("Invalid number of arguments.\n")
	    sys.stderr.write("Usage: %s CONFIGFILE \n" % (sys.argv[0], ))
	    sys.exit(1)
	config_path = sys.argv[1]

	f = open('./uploader.log','a')
	f.write('\n \nRUN.PY\t\t|| ' + time.strftime("%d %b %Y %H:%M:%S", time.gmtime()) + 'Data synchronisation system was started.\n')
	f.close()
	#FuncServerSetup()
	try:
		while True:
			TimeVarSort = EverySec(900, TimeVarSort, "Sort")
			TimeVarSync = EverySec(1800, TimeVarSync, "Sync")
			TimeVarSync = EverySec(1800, TimeVarSync, "Sync")
			#TimeVarSync = EverySec(3600, TimeVarSync, "DiskGuard")
			time.sleep(5)
	except KeyboardInterrupt:
		sys.exit(0)

