import os
from collections import namedtuple
import time
from time import gmtime, strftime
import config

#_ntuple_diskusage = namedtuple('usage', 'total used free')

def disk_usage(path, type):
	st = os.statvfs(path)
	if type=="free":
		data = st.f_bavail * st.f_frsize
	elif type=="used":
		data = (st.f_blocks - st.f_bfree) * st.f_frsize
	elif type=="total":
		data = st.f_blocks * st.f_frsize
	return int(data*0.000000953674316)


def clean():
	 pass



def main():
	f = open('Log-RMDS-py','a')
	freeSpace = disk_usage(config.path, "free")
	if freeSpace > 3*100:
		print " Uziti disku :" + str(freeSpace) + "MB free" + " from " + str(disk_usage(config.path, "total")) + "MB"
		f.write('DISKGUARD.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + " disk usage:" + str(freeSpace) + "MB free" + " from " + str(disk_usage(config.path, "total")) + "MB" + '  \n')
		#clean()
	elif freeSpace < 3*100 and freeSpace >> 2*100:
		print " !!!!!! Na disku dochazi misto :" + freeSpace + "MB free" + " from " + str(disk_usage(config.path, "total")) + "MB"
		f.write('DISKGUARD.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + " disk usage:" + str(freeSpace) + "MB free" + " from " + str(disk_usage(config.path, "total")) + "MB" + " !!!!!! Na disku dochazi misto :" + '  \n')
	elif freeSpace < 2*100:
		print " !!!!!! Na disku doslo misto :" + freeSpace + "MB free" + " from " + str(disk_usage(config.path, "total"))  + "MB "+ "spusteno mazani"
		f.write('DISKGUARD.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + " disk usage:" + str(freeSpace) + "MB free" + " from " + str(disk_usage(config.path, "total")) + "MB" + " !!!!!! Zacalo mazani disku :" + '  \n')
		#clean()
	f.close()

if __name__ == '__main__':
	main()