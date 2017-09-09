#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#

import string
import requests

coin_list = ["LTC","ETH","BCC","ZEC","XRP","ETC","DASH","XMR"]
curr_list = ["BTC","LTC","ETH","BCC","ZEC","XRP","ETC","DASH","XMR"]
curr_default = ["BTC"]

def getCurrentData():
    data = requests.get("https://api.bitfinex.com/v2/tickers?symbols=tLTCBTC,tETHBTC,tETCBTC,tZECBTC,tXMRBTC,tDSHBTC,tBCHBTC,tXRPBTC").json()

    bit = {}
    price = {}
    fee = getFee()["trade"]

    for coin in coin_list:
        bit[coin] = {}
    bit["LTC"]["BTC"] = data[0][7]
    bit["ETH"]["BTC"] = data[1][7]
    bit["ETC"]["BTC"] = data[2][7]
    bit["ZEC"]["BTC"] = data[3][7]
    bit["XMR"]["BTC"] = data[4][7]
    bit["DASH"]["BTC"] = data[5][7]
    bit["BCC"]["BTC"] = data[6][7]
    bit["XRP"]["BTC"] = data[7][7]
    
    for coin in coin_list:
        for curr in curr_list:
            if curr in curr_default:
                continue
            if coin == curr:
                bit[coin][curr] = 1.00
            else:
                price["curr"] = bit[curr]["BTC"]
                price["coin"] = bit[coin]["BTC"]
                bit[coin][curr] = (price["coin"]/(1-fee["buy"]))/(price["curr"]*(1-fee["sell"]))

    return bit

def getCoinList():

    return coin_list

def getCurrList():

    return curr_list

def getFee():
    fee = {}
    fee["trade"] = {}
    fee["trade"]["buy"] = 0.0002
    fee["trade"]["sell"] = 0.0001

    for coin in coin_list:
        fee[coin] = {}

    fee["BTC"] = {}
    fee["BTC"]["static"] = 0.0004
    fee["LTC"]["static"] = 0.001
    fee["ETH"]["static"] = 0.01
    fee["ETC"]["static"] = 0.01
    fee["ZEC"]["static"] = 0.001  
    fee["XMR"]["static"] = 0.04
    fee["DASH"]["static"] = 0.01
    fee["BCC"]["static"] = 0.0001
    fee["XRP"]["static"] = 0.01 
    
    return fee