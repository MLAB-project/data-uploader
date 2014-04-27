#!/usr/bin/python
 
import sys
import threading
import time
import sort
import sync
import subprocess




def FuncSort():
	print "\n\n==================================================\nStart Sort\n\n"
	sort.main()

def FuncSync():
	print "\n\n==================================================\nStart Sync\n\n"
	sync.main()

def FuncRmob():
	pass



if __name__ == "__main__":

	threadSort = threading.Thread(target=FuncSort)
	threadSSync = threading.Thread(target=FuncSync)
	threadSort.start()
	threadSort.join(600)
	threadSSync.start()
	threadSSync.join(1800)

