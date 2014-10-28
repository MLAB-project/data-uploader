#!/usr/bin/python

import sys
import threading
import time
from time import gmtime, strftime
import sort
import sync
import subprocess
import time


TimeVarSort = 0.0000
TimeVarSync = 0.0000

def FuncSort():
	print "\n\n==================================================\nStart Sort\n\n"
	sort.main()
	subprocess.Popen(["python","sort.py"])

def FuncSync():
	print "\n\n==================================================\nStart Sync\n\n"
	sync.main()
	subprocess.Popen(["python","sync.py"])

def FuncServerSetup():
	print "\n\n==================================================\nStart Server Setup\n\n"
	sync.main()
	subprocess.Popen(["python","serversetup.py"])

def FuncDiskGuard():
	print "\n\n==================================================\nStart DiskGuard\n\n"
	sync.main()
	subprocess.Popen(["python","DiskGuard.py"])



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
	f = open('Log-RMDS-py','a')
	f.write('\n \nRUN.PY\t\t|| ' + time.strftime("%d %b %Y %H:%M:%S", time.gmtime()) + ' Aplikace RUN.PY byla spustena\n')
	f.close()
	FuncServerSetup()
	try:
		while True:
			TimeVarSort = EverySec(900, TimeVarSort, "Sort")
			TimeVarSync = EverySec(1800, TimeVarSync, "Sync")
			TimeVarSync = EverySec(1800, TimeVarSync, "Sync")
			TimeVarSync = EverySec(3600, TimeVarSync, "DiskGuard")
			time.sleep(5)
	except KeyboardInterrupt:
		sys.exit(0)

