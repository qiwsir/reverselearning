#!/usr/bin/env python
# coding=utf-8

from conndb import *
import tornado.web

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class IndexHandler(tornado.web.RequestHandler):
    """
    the index page of website.
    """
    def get(self):
        pass

    def post(self):
        """
        user login the website.
        """
        pass
