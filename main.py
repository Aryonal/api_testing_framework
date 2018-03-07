#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from cases import *
import testing

def main():

    test_Register_once()
    test_Login_once()
    test_Signup_once()
    test_addID_once()
    t.print_all()

if __name__ == '__main__':
    #main()

    a = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImEiLCJuYW1lIjoiamFtaWUyIiwib3BlbmlkIjoiIiwidW5pb25pZCI6IiIsInBlcm1pc3Npb24iOnt9LCJleHAiOjE1MjI5MjY3ODUsImlzcyI6IlVsdHJhYmVhci1BdXRoLVNlcnZpY2UiLCJuYmYiOjE1MjAzMzQ3ODV9.ZedJwDhWV5ISaKZi2QCWZ_ewZMW6VMvSlw8pFbJMUoY"
    print testing.feasible_jwt(a)
