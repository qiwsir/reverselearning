#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handlers.index import IndexHandler
from handlers.index import ListenWriteHandler
from handlers.audio import AudioTextHandler

url=[
    (r'/', IndexHandler),
    (r'/listenwrite', ListenWriteHandler),
    (r'/audio', AudioTextHandler),
    ]
