#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#

import string
import requests

coin_list = ["BTC","LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","NMC","XEM","XPM","XMR"]
curr_list = ["CNY","BTC","LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","NMC","XEM","XPM","XMR"]
curr_default = ["CNY"]

def getCurrentData():
    data = requests.get("https://data.bter.com/api2/1/marketlist").json()["data"]
    
    bter = {}
    price = {}
    fee = getFee()["trade"]

    for coin in coin_list:
        bter[coin] = {}
        bter[coin]["CNY"] = {}
        package = "http://data.bter.com/api2/1/ticker/%s_cny" % coin.lower()
        data = requests.get(package).json()
        bter[coin]["CNY"]["Last"] = data["last"]
        bter[coin]["CNY"]["Bid"] = data["highestBid"]
        bter[coin]["CNY"]["Ask"] = data["lowestAsk"]

    for coin in coin_list:
        for curr in curr_list:
            if curr in curr_default:
                continue
            if coin == curr:
                continue
            else:
                bter[coin][curr] = {}
                price["curr"] = bter[curr]["CNY"]
                price["coin"] = bter[coin]["CNY"]
                bter[coin][curr]["Ask"] = (price["coin"]["Ask"]/(1-fee["buy"]))/(price["curr"]["Bid"]*(1-fee["sell"]))
                bter[coin][curr]["Bid"] = (price["coin"]["Bid"]/(1-fee["buy"]))/(price["curr"]["Ask"]*(1-fee["sell"]))
                #msg = "Bter %s %s %.5f" %(coin,curr,bter[coin][curr])
                #print msg
            
    return bter

def getCoinList():

    return coin_list

def getCurrList():

    return curr_list

def getFee():
    fee = {}
    fee["trade"] = {}
    fee["trade"]["buy"] = 0.0002
    fee["trade"]["sell"] = 0.0002

    for coin in coin_list:
        fee[coin] = {}

    fee["BTC"]["rate"] = 0
    fee["BTC"]["static"] = 0.0002
    fee["LTC"]["rate"] = 0
    fee["LTC"]["static"] = 0.02
    fee["ETH"]["rate"] = 0
    fee["ETH"]["static"] = 0.01
    fee["BCC"]["rate"] = 0
    fee["BCC"]["static"] = 0.0006
    fee["ZEC"]["rate"] = 0
    fee["ZEC"]["static"] = 0.0006
    fee["XRP"]["rate"] = 0
    fee["XRP"]["static"] = 0.1
    fee["NXT"]["rate"] = 0.003
    fee["NXT"]["static"] = 1
    fee["ETC"]["rate"] = 0
    fee["ETC"]["static"] = 0.01
    fee["BTS"]["rate"] = 0.01
    fee["BTS"]["static"] = 1
    fee["DOGE"]["rate"] = 0.01
    fee["DOGE"]["static"] = 5
    fee["DASH"]["rate"] = 0.01
    fee["DASH"]["static"] = 0.02
    fee["NMC"]["rate"] = 0.01
    fee["NMC"]["static"] = 0.001
    fee["XEM"]["rate"] = 0.01
    fee["XEM"]["static"] = 10
    fee["XPM"]["rate"] = 0.01
    fee["XPM"]["static"] = 0.1
    fee["XMR"]["rate"] = 0.01
    fee["XMR"]["static"] = 0.2

    return fee