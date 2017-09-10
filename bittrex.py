#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#

import string
import requests

coin_list = ["BTC","LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","XEM","XMR"]
curr_list = ["BTC","LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","XEM","XMR"]
curr_default = ["BTC","ETH","USDT"]

def getCurrentData():
    bitt = {}
    price = {}
    fee = getFee()["trade"]
    for coin in coin_list:
        bitt[coin] = {}
        for curr in curr_default:
            if coin == curr:
                continue
            if coin == "BTC":
                continue
            if coin == "NXT" and curr != "BTC":
                continue
            if coin == "BTS" and curr == "USDT":
                continue
            if coin == "DOGE" and curr == "ETH":
                continue
            if coin == "DOGE" and curr == "USDT":
                continue
            if coin == "XEM" and curr == "USDT":
                continue
            package = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=%s-%s" % (curr.lower(),coin.lower())
            data = requests.get(package).json()["result"][0]
            bitt[coin][curr] = (float(data["Ask"])+float(data["Bid"]))/2 

    for coin in coin_list:
        for curr in curr_list:
            if coin == "BTC":
                continue
            if curr in curr_default:
                continue
            if coin == curr:
                bitt[coin][curr] = 1.00
            else:
                price["curr"] = bitt[curr]["BTC"]
                price["coin"] = bitt[coin]["BTC"]
                bitt[coin][curr] = (price["coin"]/(1-fee["buy"]))/(price["curr"]*(1-fee["sell"]))
            
    return bitt

def getCoinList():

    return coin_list

def getCurrList():

    return curr_list

def getFee():
    fee = {}
    fee["trade"] = {}
    fee["trade"]["buy"] = 0.00025
    fee["trade"]["sell"] = 0.00025

    for coin in coin_list:
        fee[coin] = {}

    fee["BTC"]["static"] = 0.001
    fee["LTC"]["static"] = 0.002
    fee["ETH"]["static"] = 0.005
    fee["BCC"]["static"] = 0.001
    fee["ZEC"]["static"] = 0.005
    fee["XRP"]["static"] = 0.02
    fee["NXT"]["static"] = 2
    fee["ETC"]["static"] = 0.01
    fee["BTS"]["static"] = 5
    fee["DOGE"]["static"] = 2
    fee["DASH"]["static"] = 0.002
    fee["XEM"]["static"] = 15
    fee["XMR"]["static"] = 0.04

    return fee