import os
from collections import namedtuple

#_ntuple_diskusage = namedtuple('usage', 'total used free')

def disk_usage(path, type):
    st = os.statvfs(path)
    if type=="free":
    	data = st.f_bavail * st.f_frsize
    elif type=="used":
    	data = (st.f_blocks - st.f_bfree) * st.f_frsize
    elif type=="total":
    	data = st.f_blocks * st.f_frsize
    return data*0.000000953674316


print disk_usage("/","free")