#!/usr/bin/env python
#coding:utf-8

import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#connect with mysqldb
conn = MySQLdb.connect(host="localhost", user="root", passwd="123123", db="reverselearning", charset="utf8")

cur = conn.cursor()
