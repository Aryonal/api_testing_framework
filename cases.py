#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import api
import testing
import jwt

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
def test_Register_once(
    id      = "a",
    pwd     = "202cb962ac59075b964b07152d234b70",
    name    = "jamie2"):
    res = a.Register(id, pwd, name)
    return res


def match_jwt(res):
    encode = (res.json())["data"]
    return feasible_jwt(encode)

def feasible_jwt(a):
    try:
        d = jwt.decode(a, verify=False)
    except:
        return False
    else:
        if d["iss"] == 'Ultrabear-Auth-Service':
            return True
        return False

# test case 2
@t.api_testing("Login")
@t.result_should_be(match_jwt)
@t.http_code_testing
@t.timing
def test_Login_once(
    id      = "a",
    pwd     = "202cb962ac59075b964b07152d234b70"):
    res = a.Login(id, pwd)
    return res

# test case 3
@t.api_testing("ADDID")
@t.result_should_be(lambda res : (res.json())["code"] is not 2)
@t.http_code_testing
@t.timing
def test_addID_once(
    id      = "a",
    pwd     = "202cb962ac59075b964b07152d234b70",
    name    = "jamie2"):
    res = a.AddID(id, pwd, name)
    return res

# test case 4
@t.api_testing("Signup")
@t.result_should_be(lambda res : (res.json())["code"] is not 2)
@t.http_code_testing
@t.timing
def test_Signup_once(
    phone       = "7272178348",
    school      = "Primary",
    grade       = 5,
    experienced  = True):
    res = a.Signup(phone, school, grade, experienced)
    return res
