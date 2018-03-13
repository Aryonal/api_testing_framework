#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import requests as r
import testing
import api

def Register(id, pwd, name):
    '''
    id:     "a"
    pwd:    "password"
    name:   "Adam"
    '''
    url = api.domain + "auth/" + api.prefix + "/register"
    data = {
        "id": id,
        "pwd": pwd,
        "name": name
    }
    res = r.post(url, json = data)
    print "POST: " + url
    print "data: " + str(data)
    return res

def AddID(id, pwd, name):
    '''
    id:     "a"
    pwd:    "password"
    name:   "Adam"
    '''
    url = api.domain + "auth/" + api.prefix + "/adduserid"
    data = {
        "id": id,
        "pwd": pwd,
        "name": name
    }
    res = r.post(url, json = data)
    print "POST: " + url
    print "data: " + str(data)
    return res

def SetRole(id, pwd, name):
    '''
    id:     "a"
    pwd:    "password"
    name:   "Adam"
    '''
    Register(id, pwd, name)

def Login(id, pwd):
    '''
    id:     "a"
    pwd:    "password"
    '''
    url = api.domain + "auth/" + api.prefix + "/login"
    data = {
        "id": id,
        "pwd": pwd
    }
    res = r.post(url, json = data)
    print "POST: " + url
    print "data: " + str(data)
    return res

def Signup(phone, school, grade, experienced):
    '''
    phone:          "7272178348"
    school:         "Primary"
    grade:          5
    experienced:     true
    '''
    url = api.domain + "auth/" + api.prefix + "/login"
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
