#!/usr/bin/python
# -*- coding: utf-8 -*-
"""rmds_data_uploader.app module.

Author: Jan Milik <milikjan@fit.cvut.cz>
"""


import sys
import time

import daemon
import lockfile

import mlabutils.app


class UploaderApp(mlabutils.app.DaemonAppBase):
	def setup_app(self):
		self.app_name = __name__
		mlabutils.app.DaemonAppBase.setup_app(self)

	def run_daemon(self):
		while True:
			try:
				with open("/home/jan/rmds_data_uploader.log", "a") as f:
					f.write(time.ctime() + "\n")
			except Exception:
				pass
			time.sleep(3)


def main():
	app = UploaderApp()
	app.main()


if __name__ == "__main__":
	main()

