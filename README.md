RMDS data uploader
==================

 Python utility which sort measured data to folders and upload it to data server. 

Configuration
-------------

Edit config.py as is desired for station configuration.

Example: 

# Name of station (it appears in data file names)
Station = "uFlu-R0"
# Project session name
StationSpace = "uFlu-R0"
# Observatory name
UserSpace = "uFlu"
# Unsorted data files
path = "/home/odroid/Bolidozor/uFlu/uFlu-R0/"
# Folder with unsorted raw meteor data records ("audio/","meteors")
path_audio = "meteors/"
# Folder with snapshots ("capture/","snapshots/")
path_image = "snapshots/"
# Folder with metadata ("data/","data/")
path_data = "data/"
# Folder to sort data files
path_sort = "/home/odroid/Bolidozor/uFlu/uFlu-R0/Sort/"
# Version of input data files eg: "Bolidozor_14", "RadObs_14_7"
Version = "RadObs_14_7"


Usage
-----

Execute the Run.py script

        $ python Run.py
