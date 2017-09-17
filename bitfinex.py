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
        bit[coin]["BTC"] = {}

    bit["LTC"]["BTC"]["Last"] = data[0][7]
    bit["LTC"]["BTC"]["Bid"] = data[0][1]
    bit["LTC"]["BTC"]["Ask"] = data[0][3]

    bit["ETH"]["BTC"]["Last"] = data[1][7]
    bit["ETH"]["BTC"]["Bid"] = data[1][1]
    bit["ETH"]["BTC"]["Ask"] = data[1][3]

    bit["ETC"]["BTC"]["Last"] = data[2][7]
    bit["ETC"]["BTC"]["Bid"] = data[2][1]
    bit["ETC"]["BTC"]["Ask"] = data[2][3]

    bit["ZEC"]["BTC"]["Last"] = data[3][7]
    bit["ZEC"]["BTC"]["Bid"] = data[3][1]
    bit["ZEC"]["BTC"]["Ask"] = data[3][3]

    bit["XMR"]["BTC"]["Last"] = data[4][7]
    bit["XMR"]["BTC"]["Bid"] = data[4][1]
    bit["XMR"]["BTC"]["Ask"] = data[4][3]

    bit["DASH"]["BTC"]["Last"] = data[5][7]
    bit["DASH"]["BTC"]["Bid"] = data[5][1]
    bit["DASH"]["BTC"]["Ask"] = data[5][3]

    bit["BCC"]["BTC"]["Last"] = data[6][7]
    bit["BCC"]["BTC"]["Bid"] = data[6][1]
    bit["BCC"]["BTC"]["Ask"] = data[6][3]

    bit["XRP"]["BTC"]["Last"] = data[7][7]
    bit["XRP"]["BTC"]["Bid"] = data[7][1]
    bit["XRP"]["BTC"]["Ask"] = data[7][3]
    
    for coin in coin_list:
        for curr in curr_list:
            if curr in curr_default:
                continue
            if coin == curr:
                continue
            else:
                bit[coin][curr] = {}
                price["curr"] = bit[curr]["BTC"]
                price["coin"] = bit[coin]["BTC"]
                bit[coin][curr]["Ask"] = (price["coin"]["Ask"]/(1-fee["buy"]))/(price["curr"]["Bid"]*(1-fee["sell"]))
                bit[coin][curr]["Bid"] = (price["coin"]["Bid"]/(1-fee["buy"]))/(price["curr"]["Ask"]*(1-fee["sell"]))

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