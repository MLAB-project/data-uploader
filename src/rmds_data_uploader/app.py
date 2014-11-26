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


class UploaderApp(mlabutils.app.CLIAppBase):
	def setup_app(self):
		mlabutils.app.CLIAppBase.setup_app(self)
		self.app_name = __name__

		self.pidfile_name = "/var/run/%s.pid" % (self.app_name, )
		self.daemon_context = daemon.DaemonContext(
			pidfile = lockfile.FileLock(self.pidfile_name)
		)

	def run(self):
		if self.daemon_context.pidfile.is_locked():
			sys.stderr.write("PID file %s is locked. Daemon is probably running.\n" % (
				self.pidfile_name,
			))
			return 1
		else:
			sys.stderr.write("PID file is not locked.\n")

		print "Starting daemon..."
		with self.daemon_context:
			print "In daemon!"
			self.run_daemon()

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

