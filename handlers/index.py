#!/usr/bin/env python
# coding=utf-8

from conndb.db import *
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
        
        if user_name and user_pwd:
            sql = "select * from users where username='{0}'".format(user_name)

        try:
            cur.execute(sql)
            password_in = cur.fetchone()[2]
            if user_pwd == password_in:
                self.write("1")
            else:
                self.write("0")
        except:
            self.write("-1")
        
class ListenWriteHandler(tornado.web.RequestHandler):
    def get(self):
        user_name = self.request.uri.split("=")[-1]
        self.render("listenwrite.html", username = user_name)

    def post(self):
        audio_name = self.get_argument("audioname")
        audio_text = self.get_argument("audiotext")

        print audio_text
        self.write("1")
