#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#

import string
import requests

coin_list = ["ltc","eth","bcc","zec","xrp","etc","dash","xmr"]

def getCoinList():

    return coin_list

def getCurrentData():
    data = requests.get("https://api.bitfinex.com/v2/tickers?symbols=tLTCBTC,tETHBTC,tETCBTC,tZECBTC,tXMRBTC,tDSHBTC,tBCHBTC,tXRPBTC").json()

    bit = {}
    bit["ltc"] = data[0][7]
    bit["eth"] = data[1][7]
    bit["etc"] = data[2][7]
    bit["zec"] = data[3][7]
    bit["xmr"] = data[4][7]
    bit["dash"] = data[5][7]
    bit["bcc"] = data[6][7]
    bit["xrp"] = data[7][7]
    
    return bit

def getFee():
    fee = {}
    fee["trade"] = 0.00015
    fee["btc"]["static"] = 0.0004
    fee["ltc"]["static"] = 0.001
    fee["eth"]["static"] = 0.01
    fee["etc"]["static"] = 0.01
    fee["zec"]["static"] = 0.001  
    fee["xmr"]["static"] = 0.04
    fee["dash"]["static"] = 0.01
    fee["bcc"]["static"] = 0.0001
    fee["xrp"]["static"] = 0.01 
    
    return fee