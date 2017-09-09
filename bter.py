#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#

import string
import requests

coin_list = ["ltc","eth","bcc","zec","xrp","nxt","etc","bts","doge","dash","nmc","xem","xpm","xmr"]

def getCoinList():

    return coin_list

def getCurrentData():
    data = requests.get("https://data.bter.com/api2/1/marketlist").json()["data"]
    bter = {}
    for i in range(0,len(data)):
        if data[i]["symbol"].lower() in coin_list:
            bter["%s" % data[i]["symbol"].lower()] = data[i]["rate"]

    return bter

def getFee():
    fee = {}
    fee["trade"] = 0.0002
    fee["btc"]["rate"] = 0
    fee["btc"]["static"] = 0.0002
    fee["ltc"]["rate"] = 0
    fee["ltc"]["static"] = 0.02
    fee["eth"]["rate"] = 0
    fee["eth"]["static"] = 0.01
    fee["bcc"]["rate"] = 0
    fee["bcc"]["static"] = 0.0006
    fee["zec"]["rate"] = 0
    fee["zec"]["static"] = 0.0006
    fee["xrp"]["rate"] = 0
    fee["xrp"]["static"] = 0.1
    fee["nxt"]["rate"] = 0.003
    fee["nxt"]["static"] = 1
    fee["etc"]["rate"] = 0
    fee["etc"]["static"] = 0.01
    fee["bts"]["rate"] = 0.01
    fee["bts"]["static"] = 1
    fee["doge"]["rate"] = 0.01
    fee["doge"]["static"] = 5
    fee["dash"]["rate"] = 0.01
    fee["dash"]["static"] = 0.02
    fee["nmc"]["rate"] = 0.01
    fee["nmc"]["static"] = 0.001
    fee["xem"]["rate"] = 0.01
    fee["xem"]["static"] = 10
    fee["xpm"]["rate"] = 0.01
    fee["xpm"]["static"] = 0.1
    fee["xmr"]["rate"] = 0.01
    fee["xmr"]["static"] = 0.2

    return fee