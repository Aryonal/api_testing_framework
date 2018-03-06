#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import api
import testing

a = api.Api("http", "localhost:8082", "api/v1.0")
t = testing.Testing()

# setting
def set(protocol, addr, prefix):
    a = api.Api(protocol, addr, prefix)

# test case 1
@t.api_testing("Register")
@t.result_should_be(lambda res : (res.json())["code"] is not 2)
@t.http_code_testing
@t.timing
def test_Register_once():
    res = a.Register(
        id      = "a",
        pwd     = "202cb962ac59075b964b07152d234b70",
        name    = "jamie2")
    return res


def match_jwt(res):
    encode = (res.json())["data"]
    return testing.feasible_jwt(encode)

# test case 2
@t.api_testing("Login")
@t.result_should_be(match_jwt)
@t.http_code_testing
@t.timing
def test_Login_once():
    res = a.Login(
        id      = "a",
        pwd     = "202cb962ac59075b964b07152d234b70")
    return res

# test case 3
@t.api_testing("ADDID")
@t.result_should_be(lambda res : (res.json())["code"] is not 2)
@t.http_code_testing
@t.timing
def test_addID_once():
    res = a.AddID(
        id      = "a",
        pwd     = "202cb962ac59075b964b07152d234b70",
        name    = "jamie2")
    return res

# test case 4
@t.api_testing("Signup")
@t.result_should_be(lambda res : (res.json())["code"] is not 2)
@t.http_code_testing
@t.timing
def test_Signup_once():
    res = a.Signup(
        phone       = "7272178348",
        school      = "Primary",
        grade       = 5,
        experienced  = True)
    return res
