#!/usr/bin/python

import thread
import time
import os
import DiscGuard
import threading
import signal
import time
import sys
from time import gmtime, strftime
from time import sleep
import sync


def sigint_handler(signum, frame):
	print 'Stop pressing the CTRL+C!'
	t1.kill()
	t2.kill()
	sys.exit()

def Vlakno1():
	#while t1.isAlive() == True:
	#	pass
	#	print "##############################  Sync porad bezi"
	#	time.sleep(16)
	t1 = threading.Timer(60*4, Vlakno1).start()
	sync.sync()
	print "==============================  Vlakno 1 bylo dokonceno"

	

def Vlakno2():
	#while run == 1:
	for x in xrange(1,50):
		print "-"
		#time.sleep(0.25)



signal.signal(signal.SIGINT, sigint_handler)
signal.signal(signal.SIGPWR, sigint_handler)
signal.signal(signal.SIGSYS, sigint_handler)



def main():
	t1 = threading.Timer(5, Vlakno1)
	t1.start()
	t2 = threading.Timer(60, Vlakno2)
	#t2.start()
	It1=1
	It2=1
	while True:
		#if It1 == 5:
		#	It1 = 1
		#	t1.run()
		#if It2 == 60:
		#	print "Minuta" + strftime("%Y %m %d %H:%M:%S", gmtime())
		#	It2=1
		#It1=It1+1
		#It2=It2+1
		#time.sleep(1)
		pass


##########

if __name__ == "__main__":
	main()

