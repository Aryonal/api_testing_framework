#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import requests as r
import sys, time
import jwt


class HTTPCodeError(Exception):
    pass

class NotMatchError(Exception):
    pass

class Testing:

    def __init__(self):
        self._all_num = 0
        self._pass_num = 0
        self._fail_num = 0
        self._http_code_error = 0
        self._not_match = 0
        self._connection_error = 0
        self._other_error = 0

    def clear(self):
        self._all_num = 0
        self._pass_num = 0
        self._fail_num = 0
        self._http_code_error = 0
        self._not_match = 0
        self._connection_error = 0
        self._other_error = 0

    def print_all(self):
        print "\n----------"
        print "all cases:" + str(self._all_num)
        print "passes cases:" + str(self._pass_num)
        print "failed cases:" + str(self._fail_num)

    '''
    frame work for single api testing, catch exceptions and judge if passes
    api_name: str: api_name
    '''
    def api_testing(self, api_name):
        def dec(f):
            def func(*args, **kwds):
                #TODO
                self._all_num += 1
                print "-----" + api_name + "-----"
                try:
                    res = f(*args, **kwds)
                except Exception as err:
                    self._fail_num += 1
                    print "FAIL: ",
                    if isinstance(err, HTTPCodeError):
                        #TODO
                        self._http_code_error += 1
                        print "HTTPCodeError"
                    elif isinstance(err, NotMatchError):
                        #TODO
                        self._not_match += 1
                        print "Result is not what we want"
                    elif isinstance(err, r.models.ConnectionError):
                        #TODO
                        self._connection_error += 1
                        print "ConnectionError"
                    else:
                        self._other_error += 1
                        print sys.exc_info()[0]
                    print "\n"
                else:
                    self._pass_num += 1
                    print "PASS\n"
                    return res
            return func
        return dec

    '''
    raise NotMatchError if result cannot match what we want
    f_match: function: return True if result meet what we want
    '''
    def result_should_be(self, f_match = lambda x : True):
        def dec(f):
            def func(*args, **kwds):
                try:
                    res = f(*args, **kwds)
                except:
                    raise
                else:
                    if not f_match(res):
                        #TODO: show diff
                        print ">>>>> FAILED RESPONSE TEXT:"
                        print res.text
                        raise NotMatchError()
                    print ">>>>> Result is what we want"
                    print res.text
                    return res
            return func
        return dec

    '''
    timer
    '''
    def timing(self, f):
        def func(*args, **kwds):
            start = time.time()
            try:
                res = f(*args, **kwds)
            except:
                raise
            stop = time.time()
            print ">>>>> finished within " + str(1000*(stop-start)) + " ms"
            return res
        return func

    '''
    raise HTTPCodeError if response http code is not 200
    '''
    def http_code_testing(self, f):
        def func(*args, **kwds):
            try:
                res = f(*args, **kwds)
            except:
                raise
            if res.status_code is not 200:
                print ">>>>> FAILED RESPONSE TEXT:"
                print res.text
                raise HTTPCodeError()
            print ">>>>> [200 OK]"
            return res
        return func
