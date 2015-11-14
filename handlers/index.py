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
        self.render("index.html")

    def post(self):
        """
        user login the website.
        """
        user_name = self.get_argument("username")
        user_pwd = self.get_argument("password")
        self.write(user_name)        

