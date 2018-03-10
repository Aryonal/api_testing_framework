#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import requests as r
import testing
import api

def project_detail_by_id(id):
    '''
    id:     "621e4b8e2ca2401940429d2bb2c2676"
    '''
    url = api.domain + "project/" + id
    res = r.get(url)
    print "GET: " + url
    return res

def custom_detail_by_name(name):
    '''
    name:   "1"
    '''
    url = api.domain + "custumes/" + name
    res = r.get(url)
    print "GET: " + url
    return res

def custumes_list():
    '''
    '''
    url = api.domain + "custumes"
    res = r.get(url)
    print "GET: " + url
    return res

def get_asset_with_md5_url(route):
    '''
    route:  "e4d33df8343c3e0cd3c95d47e3ab92b5.png"
    '''
    url = api.domain + "assets/" + route
    res = r.get(url)
    print "GET: " + url
    return res

def sounds_list():
    '''
    '''
    url = api.domain + "sounds"
    res = r.get(url)
    print "GET: " + url
    return res

def backdrops_list():
    '''
    '''
    url = api.domain + "backdrops"
    res = r.get(url)
    print "GET: " + url
    return res

def sound_detail_by_name(name):
    '''
    name:   "meow_0"
    '''
    url = api.domain + "sounds/" + name
    res = r.get(url)
    print "GET: " + url
    return res

def user_projects_list(id):
    '''
    id:     "a"
    '''
    url = api.domain + "user/" + id + "/projects"
    res = r.get(url)
    print "GET: " + url
    return res

def projects_list():
    '''
    '''
    url = api.domain + "projects"
    res = r.get(url)
    print "GET: " + url
    return res

def backdrop_detail_by_name(name):
    '''
    name:   "backdrop_0"
    '''
    url = api.domain + "backdrops/" + name
    res = r.get(url)
    print "GET: " + url
    return res

def upload_custume(file_dir, name, center_x, center_y, resolution, format):
    '''
    file_dir:       "./custume_0"
    name:           "custume_0"
    center_x:       31
    center_y:       100
    resolution:     "1"
    format:         "png"
    '''
    url = api.domain + "custumes"
    d = {
        "name":         name,
        "center_x":     center_x,
        "center_y":     center_y,
        "resolution":   resolution,
        "format":       format
    }
    f = {
        name:           open(file_dir, 'rb')
    }
    res = r.post(url, files=f, data=d)
    print "POST: " + url
    print "data: " + str(d)
    return res

def upload_sound(file_dir, name, rate, sampleCount, format):
    '''
    file_dir:       "./meow_0"
    name:           "meow_0"
    rate:           22050
    sampleCount:    5920
    format:         "wav"
    '''
    url = api.domain + "sounds"
    d = {
        "file_dir":     file_dir,
        "name":         name,
        "rate":         rate,
        "sampleCount":  sampleCount,
        "format":       format
    }
    f = {
        name:           open(file_dir, 'rb')
    }
    res = r.post(url, files=f, data=d)
    print "POST: " + url
    print "data: " + str(d)
    return res

def upload_backdrops(file_dir, name, width, height, resolution, format):
    '''
    file_dir:       "./backdrop_0"
    name:           "backdrop_0"
    width:          480
    height:         360
    resolution:     "1"
    format:         "png"
    '''
    url = api.domain + "backdrops"
    d = {
        "name":         name,
        "width":        width,
        "height":       height,
        "resolution":   resolution,
        "format":       format
    }
    f = {
        name:           open(file_dir, 'rb')
    }
    res = r.post(url, files=f, data=d)
    print "POST: " + url
    print "data: " + str(d)
    return res

def duplicate_project(id, text):
    '''
    id:   "b65f87f01f2bbce16a717651fa03208a"
    text: ```{
	           "id": "teacher_student_b65f87f01f2bbce16a717651fa03208a",
	           "name": "project_0",
	           "owner": "student"
          }```
    '''
    url = api.domain + "projects/" + id
    r.post(url, data=text, headers={'content-type': 'text/plain'})
    print "POST: " + url
    print "data: " + text
    return res

def upload_project(project_text):
    '''
    project_text: ...(too long)...
    '''
    url = api.domain + "projects"
    r.post(url, data=project_text, headers={'content-type': 'text/plain'})
    print "POST: " + url
    print "data: " + text
    return res
