#!/usr/bin/python
import signal
import sys
import threading
import time
import subprocess
import array

i = 0
Exit = 0

###############################################################
##
##	Time[appname] = int Time             ## How often run app in sec
##	MxLi[appname] = int MaxLifeTime      ## After this timeout app will be killed
##	Open[appname] = ['aplication','Arg1','Arg2']  ## witch app must be started
##	Temp[appname] = {} ## [1]-last update; [2]- was done
##
##
###########################################################
TimeRmobGen = 15*60*1 
MxLiRmobGen = 5 *60 *1 
OpenRmobGen = ['python','../rmob-export/Run.py']
TempRmobGen = array.array('l', [0,0,0,0,0,0,0,0,0])

###########################################################
TimeSortData = 15*60*1 
MxLiSortData = 5 *60 *1 
OpenSortData = ['python','sort.py']
TempSortData = array.array('l', [0,0,0,0,0,0,0,0,0])

###########################################################
TimeSyncData = 30*60*1 
MxLiSyncData = 25*60 *1 
OpenSyncData = ['python','sort.py']
TempSyncData = array.array('l', [0,0,0,0,0,0,0,0,0])




##
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################


######################################## Start INIT SORT PY
if TempSortData[1] == 0:								## zinicializovani promenych
	TempSortData[1] = int(time.time())
	ProcSortData = subprocess.Popen(OpenSortData)

######################################## End   INIT SORT PY

######################################## Start INIT Rmob-Export
if TempRmobGen[1] == 0:								## zinicializovani promenych
	TempRmobGen[1] = int(time.time())
	ProcRmobGen = subprocess.Popen(OpenRmobGen)

######################################## End   INIT Rmob-Export

######################################## Start INIT SYNC PY
if TempSyncData[1] == 0:								## zinicializovani promenych
	TempSyncData[1] = int(time.time())
	ProcSyncData = subprocess.Popen(OpenSyncData)

######################################## End   INIT SYNC PY


##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

while Exit is 0:
	time.sleep(1)
	i += 1

######################################## Start SORT PY
	if TempSortData[1]+TimeSortData < int(time.time()) and ProcSortData.poll() != None: ## Pokud je cas na spusteni a proces jiz nebezi
		ProcSortData = subprocess.Popen(OpenSortData)
		TempSortData[1] = int(time.time())

	if TempSortData[1]+MxLiSortData < int(time.time()) and MxLiSortData != 0:	## Pokud je po limitu a limit neni 0
		ProcSortData.kill()
		print ">> Proces timeout EXPIRED: process was killed"

####################################### End   SORT PY


######################################## Start Rmob-Export
	if TempRmobGen[1]+TimeRmobGen < int(time.time()) and ProcRmobGen.poll() != None: ## Pokud je cas na spusteni a proces jiz nebezi
		ProcRmobGen = subprocess.Popen(OpenRmobGen)
		TempRmobGen[1] = int(time.time())

	if TempRmobGen[1]+MxLiRmobGen < int(time.time()) and MxLiRmobGen != 0:	## Pokud je po limitu a limit neni 0
		ProcRmobGen.kill()
		print ">> Proces timeout EXPIRED: process was killed"

####################################### End   Rmob-Export


######################################## Start Sync PY
	if TempSyncData[1]+TimeSyncData < int(time.time()) and ProcSyncData.poll() != None: ## Pokud je cas na spusteni a proces jiz nebezi
		ProcSyncData = subprocess.Popen(OpenSyncData)
		TempSyncData[1] = int(time.time())

	if TempSyncData[1]+MxLiSyncData < int(time.time()) and MxLiSyncData != 0:	## Pokud je po limitu a limit neni 0
		ProcSyncData.kill()
		print ">> Proces timeout EXPIRED: process was killed"

####################################### End   SYNC PY



	#if TempRmobGenb[1] == 0:
	#	TempRmobGenb[1] = int(time.time())
	#	ProcRmobGenb = subprocess.Popen(OpenRmobGenb)
	#if TempRmobGenb[1]+TimeRmobGenb < int(time.time()):
	#	ProcRmobGenb = subprocess.Popen(OpenRmobGenb)
	#	TempRmobGenb[1] = int(time.time())
	#print "AhBB", (TempRmobGenb[1]+TimeRmobGenb) - int(time.time()), (TempRmobGenb[1]+TimeRmobGenb) < int(time.time())


	if i is 10:
		print ">> Sort", (TempSortData[1]+TimeSortData)-int(time.time()), "\t>> RmobGen", (TempRmobGen[1]+TimeRmobGen) - int(time.time()), "\t>> SyncData", (TempSyncData[1]+TimeSyncData) - int(time.time())
		i = 0