#!/usr/bin/python
# -*- coding: utf-8 -*-
"""test_app module.

Author: Jan Milik <milikjan@fit.cvut.cz>
"""


import unittest

from rmds_data_uploader import app


class UploaderAppTest(unittest.TestCase):
    def test_constructor(self):
        inst = app.UploaderApp()


def main():
    print __doc__


if __name__ == "__main__":
    main()

