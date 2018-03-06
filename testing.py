#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import api
import testing
import jwt

def match_jwt(res):
    encode = (res.json())["data"]
    return testing.feasible_jwt(encode)

def testing_case():
    a = api.Api("http", "localhost:8082", "api/v1.0")
    t = testing.Testing()

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
    res = test_Register_once()

    # test case 2
    @t.api_testing("Register")
    @t.result_should_be(match_jwt)
    @t.http_code_testing
    @t.timing
    def test_Login_once():
        res = a.Login(
            id      = "a",
            pwd     = "202cb962ac59075b964b07152d234b70")
        return res
    res = test_Login_once()

    t.print_all()

if __name__ == '__main__':
    #testing_case()
    a = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImEiLCJuYW1lIjoiamFtaWUyIiwib3BlbmlkIjoiIiwidW5pb25pZCI6IiIsInBlcm1pc3Npb24iOnt9LCJleHAiOjE1MjI5MjYwMTMsImlz\ncyI6IlVsdHJhYmVhci1BdXRoLVNlcnZpY2UiLCJuYmYiOjE1MjAzMzQwMTN9.VT-9bEt4SenN-NbZlDu2OOVV9q39FqqnDsaQZlBybkw"
    print jwt.decode(a, 'secret', algorithm="HMAC")
