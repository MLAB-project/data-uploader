RMDS data uploader
==================

 Python utility which sort measured data to folders and upload it to data server. 

Configuration
-------------

Edit config.py as is desired for station configuration.

Example: 
		# Station name
		Station = "TEST-R0"
		StationSpace = Station
		# Observatory name and space.astro.cz logon name
		UserSpace = "svakov"
		UserName = UserSpace
		# Path to unsorted data
		path = "/home/odroid/Bolidozor/TEST-R0/"
		# Subdirectory with RAW meteors records ("audio/","meteors")
		path_audio = "meteors/"
		# Subdirectory with snapshots ("capture/","snapshots/")
		path_image = "snapshots/"
		# Subdirectory with metadata ("data/","data/")
		path_data = "data/"
		# Space for sorted data
		path_sort = "/home/odroid/Bolidozor/TEST-R0/Sort/"
		# Version of data format
		Version = "RadObs_14_7"

Usage
-----

Execute the run.py script:

        $ python run.py
