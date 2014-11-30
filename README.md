RMDS data uploader
==================

Python utility which sorts measured data to folders and upload it to data
server. 


Usage
-----

The `setuptools` package creates entry script named `bzupld` which is installed
in `/usr/local/bin` if the package is installed.

        # To install the package
        $ python setup.py install
        
        # To run the daemon
        $ sudo bzupld
        
        # To kill the daemon
        $ ./kill_bzupld

