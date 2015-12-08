#!/usr/bin/env python
# coding=utf-8

from conndb.db import *
from audioqiniu import *

import tornado.web

import sys
reload(sys)

class AudioTextHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("audio.html") 

