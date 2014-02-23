import array

# Znacka stanice
Station = "ZVPP"
# Cesta k nezarazenym datum
path = "/home/roman/MetData/ZVPP/"
# slozka s audio
path_audio = "audio/"
# slozka s obrazky
path_image = "capture/"
# slozka s daty
path_data = "data/"
# misto k rozrazeni
path_sort = "/home/roman/MetData/ZVPP/Sort/"
# Verze vstupnich dat eg: "Bolidozor_14"
Version = "Bolidozor_14"


###############################################################
##
##				Configure for RUN.py
##
##	Time[appname] = int Time             ## How often run app in sec
##	MxLi[appname] = int MaxLifeTime      ## After this timeout app will be killed
##	Open[appname] = ['aplication','Arg1','Arg2']  ## witch app must be started
##	Temp[appname] = {} ## [1]-last update; [2]- was done
##
##

TimeDlouhaPrace = 5*1 *1 
MxLiDlouhaPrace = 10 *1 *1 
OpenDlouhaPrace = ['python','./aa/DlouhaPrace2.py']
TempDlouhaPrace = array.array('l', [0,0,0,0,0,0,0,0,0])

TimeDlouhaPraceb = 30*1 *1 
MxLiDlouhaPraceb = 1 *60*1 
OpenDlouhaPraceb = ['python','./aa/DlouhaPrace2b.py']
TempDlouhaPraceb = array.array('l', [0,0,0,0,0,0,0,0,0])


##
###############################################################