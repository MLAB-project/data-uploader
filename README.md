Measurement station data uploader
==================

 Python utility which sort measured data to folders and upload it to data server. It is used in Bolidozor, Ionozor and Geozor projects. 


Configuration
-------------

Edit station configuration file as is desired for your project configuration.

An example for Ionozor project: 

        "project": "ionozor",
        "project_home_folder": "/home/odroid/ionozor/station/",
        "storage_hostname": "space.astro.cz",
        "storage_username": "svakov",
        "storage_stationpath": "/storage/ionozor/VLF/",
        "storage_protocol": "ssh",

These values are in Ionozor.json which is in station configuration folder.

Usage
-----

The script is usualy executed by station-supervisor. The following command can be used to run the script manually: 
        ./dataUpload.py ~/ionozor/station/Ionozor.json

Where the argument is a path to station configuration file. 
