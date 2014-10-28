import array

# Name of station (which appears in data file names)
Station = "OBSUPICE-R1"
# Project session name
StationSpace = "OBSUPICE-R1"
# Project session name (Server data folder for given username)
UserSpace = "OBSUPICE"
# user name which will be used for login to server. 
UserName = "zebrak"
# path to station output files
path = "/media/nfs/OBSUPICE/OBSUPICE-R1/"
# folder with raw data records ("audio/" or "meteors")
path_audio = "meteors/"
# folder with waterfall snapshots "capture/" (SpectrumLab) or "snapshots/"(Radio-observer)
path_image = "snapshots/"
# folder with station metadata ("data/","data/")
path_data = "data/"
# path to folder for sorting and local data storage (eg. network NAS)
path_sort = "/media/nfs/OBSUPICE/OBSUPICE-R1/Sort/"
# how much space should by cleared with 1GB free space treshold [GB] (does not work for now)
datavolume = 2279
# Output data version eg: "Bolidozor_14", "RadObs_14_7"
Version = "RadObs_14_7"
