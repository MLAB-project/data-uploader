#!/usr/bin/python

import os, sys
import shutil
from time import gmtime, strftime
import config

Station = config.Station
# config.StationSpace
path = config.path
path_audio = config.path_audio
path_audio_sort = config.path_audio_sort
path_image = config.path_image
path_image_sort = config.path_image_sort
path_data = config.path_data
path_sort = config.path_sort
Version = config.Version



def SortRadObs(SortEnd):
    list = os.listdir(config.path_data)
    print list
    for soubor in list:
        if soubor[:1] is not ".":
            path_local = config.path_sort+"/"+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"
            print(config.path_data  + soubor, path_local +soubor)
            if not os.path.exists(path_local):
                os.makedirs(path_local)
                print("data1",path_data + soubor, path_local +soubor)
            if soubor[:10] != strftime("%Y%m%d%H", gmtime()):
                shutil.move(path_data + soubor, path_local +soubor)
                print("data2",path_data + soubor, path_local +soubor)
            else:
                shutil.copy2(path_data+ soubor, path_local +soubor)

    list = os.listdir(config.path_audio)
    print list
    for soubor in list:
        if soubor[:1] is not ".":
            path_local = path_audio_sort+"/"+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"+soubor[8:10]+"/"
            print path_local + soubor
            if not os.path.exists(path_local):
                os.makedirs(path_local)
            shutil.move(path_audio + "/" + soubor, path_local+ "/" +soubor)
            print("audio",path_audio + "/" + soubor, path_local+ "/" +soubor)

    list = os.listdir(path_image)
    print list
    for soubor in list:
        if soubor[:1] is not ".":
            path_local = config.path_image_sort+"/"+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"+soubor[8:10]+"/"
            print path_local + soubor
            if not os.path.exists(path_local):
                os.makedirs(path_local)
            shutil.move(path_image + "/" + soubor, path_local+ "/" +soubor)
            print("image", path_image + "/" + soubor, path_local+ "/" +soubor)

    list = os.listdir(config.path_data)
    print list
    for soubor in list:
        print "!!!!-----! " + soubor    
        if  os.path.isfile(config.path+soubor):
            print " - file"
            path_local = path_sort
            shutil.copy2(path_data+"/" +soubor, path_sort+"/" +soubor)
            print("path",path_data+"/" +soubor, path_sort+"/" +soubor)

    SortEnd = True
    return True



def main():
    global SortEnd
    SortEnd = False
    ErrMax = 10
    ErrCount = 0
    while SortEnd == False:
        try:
            SortEnd = SortRadObs(SortEnd)
        except Exception, e:
            print "ERROR in SORT.PY", e
            ErrCount += 1
            if ErrCount >= ErrMax:
                SortEnd = True
            print "Chyb ERR,", ErrCount


    print "\t\t SORT.PY >>", strftime("%d %b %Y %H:%M:%S", gmtime()), " Konec\n"
if __name__ == "__main__":
    main()
