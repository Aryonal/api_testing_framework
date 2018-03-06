#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import requests as r
import testing

class Api:

    def __init__(self, protocol, addr, prefix):
        '''
        protocol: "http"
        addr:     "localhost:8123"
        prefix:   "api/v1.0"
        '''
        self.protocol = protocol
        self.addr = addr
        self.prefix = prefix
        self.domain = protocol + "://" + addr + "/"

    def Register(self, id, pwd, name):
        '''
        id:     "a"
        pwd:    "password"
        name:   "Adam"
        '''
        url = self.domain + "auth/" + self.prefix + "/register"
        data = {
            "id": id,
            "pwd": pwd,
            "name": name
        }
        res = r.post(url, json = data)
        print "POST: " + url
        print "data: " + str(data)
        return res

    def AddID(self, id, pwd, name):
        '''
        id:     "a"
        pwd:    "password"
        name:   "Adam"
        '''
        url = self.domain + "auth/" + self.prefix + "/adduserid"
        data = {
            "id": id,
            "pwd": pwd,
            "name": name
        }
        res = r.post(url, json = data)
        print "POST: " + url
        print "data: " + str(data)
        return res

    def SetRole(self, id, pwd, name):
        '''
        id:     "a"
        pwd:    "password"
        name:   "Adam"
        '''
        self.Register(id, pwd, name)

    def Login(self, id, pwd):
        '''
        id:     "a"
        pwd:    "password"
        '''
        url = self.domain + "auth/" + self.prefix + "/login"
        data = {
            "id": id,
            "pwd": pwd
        }
        res = r.post(url, json = data)
        print "POST: " + url
        print "data: " + str(data)
        return res

    def Signup(self, phone, school, grade, experienced):
        '''
        phone:          "7272178348"
        school:         "Primary"
        grade:          5
        experienced:     true
        '''
        url = self.domain + "auth/" + self.prefix + "/login"
        data = {
            "phone": phone,
            "school": school,
            "grade": grade,
            "experienced": experienced
        }
        res = r.post(url, json = data)
        print "POST: " + url
        print "data: " + str(data)
        return res
