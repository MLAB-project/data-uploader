#!/usr/bin/python3

import os
import sys
import optparse
from src import DataUpload
import time


def main():
    arg = sys.argv
    if len(arg) != 2:
        print("Usage: dataUpload [radio-observer configFile]")
        sys.exit(1)
    else:
        du = DataUpload.dataUpload(arg)
        while True:
            last_start = time.time()
            try:
                du.start()
            except Exception as e:
                print("CHYBA: ")
                print(e)
            wait_time = (last_start + 3600 * 100 - time.time())

            if wait_time < time.time():
                print("wait", wait_time, "ms  \n\n\n")
                time.sleep(wait_time/1000)

if __name__ == '__main__':
    main()
