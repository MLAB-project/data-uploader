#!/usr/bin/python
 
import sys
import threading
import time
import sort
import sync
import subprocess
import time


TimeVarSort = time.time()
TimeVarSync = time.time()

def FuncSort():
	print "\n\n==================================================\nStart Sort\n\n"
	#sort.main()
	#subprocess.Popen(["python","sort.py"])

def FuncSync():
	print "\n\n==================================================\nStart Sync\n\n"
	#sync.main()
	#subprocess.Popen(["python","sync.py"])


def EverySec(period, timeVar, func):
	if timeVar+period <= time.time():
		timeVar = time.time()
		print ("local \t\t",timeVar)
		if func == "Sort":
			FuncSort()
		elif func == "Sync":
			FuncSync()

	return timeVar



if __name__ == "__main__":
	try:
		while True:
			TimeVarSort = EverySec(900, TimeVarSort, "Sort")
			TimeVarSync = EverySec(1800, TimeVarSync, "Sync")
			time.sleep(5)

	except KeyboardInterrupt:
		sys.exit(0)

