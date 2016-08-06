#!/usr/bin/env python
from mlabutils import ejson

def lookup_child(arr, key, value):
    matches = [x for x in arr if x[key] == value]

    if len(matches) == 0:
        raise Exception('no children such that %r equals %r' % (key, value))

    return matches[0]

parser = ejson.Parser()

try:
    config_path = "/home/alice/ionozor/station/Ionozor.json"
    value = parser.parse_file(config_path)
except Exception as ex:
    print "JSON config file not found"
    import sys
    sys.exit(1)

config_name = value['configuration']
config = lookup_child(value['configurations'], 'key', config_name)
backend = lookup_child(config['children'], 'key', 'backend')

# Station name
Station = backend['origin']
StationSpace = Station
# Observatory name and space.astro.cz logon name
UserSpace = backend['username']
UserName = UserSpace
# Path to unsorted data replaced with absolute path from radio-observer JSON config.
path = ""
# Subdirectory with RAW meteors records ("audio/","meteors")
#path_audio = lookup_child(backend['children'], 'factory', 'bolid')['output_dir']
#path_audio_sort = lookup_child(backend['children'], 'factory', 'bolid')['output_dir_sort']
### NOTE: EVALUATES TO '.' IN CURRENT BOLIDOZOR.JSON AS OF 2015-08-11
# Subdirectory with snapshots ("capture/","snapshots/")
path_image = lookup_child(backend['children'], 'factory', 'snapshot')['output_dir']
path_image_sort = lookup_child(backend['children'], 'factory', 'snapshot')['output_dir_sort']
# Subdirectory with metadata ("data/","data/")
#path_data = backend['metadata_path']
# Space for sorted data
#path_sort = backend['metadata_path_sort']
### NOTE: NO POINTER HERE
# Version of data format
Version = "RadObs_14_7"

