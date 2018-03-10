#-*- coding:utf-8 -*-
import requests as r
import testing
import api

protocol = ""
addr = ""
prefix = ""
domain = ""

def set(protocol, addr, prefix):
    '''
    protocol: "http"
    addr:     "localhost:8082"
    prefix:   "api/v1.0"
    '''
    api.protocol = protocol
    api.addr = addr
    api.prefix = prefix
    api.domain = protocol + "://" + addr + "/"

def get():
    return {
        "protocol": api.protocol,
        "addr": api.addr,
        "prefix": api.prefix,
        "domain": api.domain
    }

__all__ = ['auth', 'assets']
from api import *
