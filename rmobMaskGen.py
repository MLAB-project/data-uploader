#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
import os
import ConfigParser
import config
import datetime
import numpy
import numpy as np
import sys


if __name__ == "__main__":
	#gui.main()
        year = 2015
        month = 5

	print "generování pro:"+ config.Station +"@"+ config.UserName
	print "otevírání souboru" + config.path_sort + "/" + config.path_data + "/" + str(year) + "/" + str(month).zfill(2) + "/" + config.Station + "_" + config.UserName + "_" + str(year) + "_" +str(month).zfill(2)+"_badData.npy"


	#manthData = np.load("ZVPP_ZVPP-R2_dataMask_"+str(year) + "_" +str(month)+".npy")
			#np.save("ZVPP_ZVPP-R2_dataMask_"+str(year) + "_" +str(month)+".npy", monthDataMask)
	try:
		monthDataMask = np.load(config.path_sort + "/" + config.path_data + "/" + str(year) + "/" + str(month).zfill(2) + "/" + config.Station + "_" + config.UserName + "_" + str(year) + "_" +str(month).zfill(2)+"_badData.npy")
	except Exception, e:
	#	monthDataMask = np.fill((24,32), True, bool)
		monthDataMask = np.ones((24,32), dtype=bool)
		print e
	monthDataMask=monthDataMask.astype(bool)
	monthDataMask=numpy.resize(monthDataMask,(24,32))





	print "a .......................... Nová maska"
	print "r .......................... Odstranit masku"
	print "w .......................... Ukázat masky"
	print "s .......................... Ulozit a ukončit"
	print "c .......................... Ukončit"


	run = True
	while run:
		var = raw_input("\n\nHodnota: ")
		if var == 'a':
			day = raw_input("den: ")
			hou = raw_input("hodina: ")
			monthDataMask[int(hou)-1,int(day)-1] = False
		elif var == 'r':
			day = raw_input("den: ")
			hou = raw_input("hodina: ")
			monthDataMask[int(hou)-1,int(day)-1] = True
		elif var == 'w':
			for x in xrange(0,24):
				for y in xrange(0,31):
					print monthDataMask[x,y],
				print ""
		elif var == 's':
       			np.save(config.path_sort + "/" + config.path_data + "/" + str(year) + "/" + str(month).zfill(2) + "/" + config.Station + "_" + config.UserName + "_" + str(year) + "_" + str(month).zfill(2) +"_badData.npy", monthDataMask)
		#	np.save(config.path + "/" + config.path_data + "/" + config.Station + "_" + config.UserName +str(year) + "_" +str(month)+".npy", monthDataMask)

			run = False
		elif var == 'c':
			run = False
		else:
			print "není definováno"
