#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#
# Bittrex's API Interface
# https://bittrex.com/Home/Api
#

import string
import requests

coin_list = ["BTC","LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","XEM","XMR"]
curr_list = ["BTC","LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","XEM","XMR"]
curr_default = ["BTC","ETH","USDT"]
ban_list = ["ETH_NXT","USDT_NXT","USDT_BTS","ETH_DOGE","USDT_XEM"]

def getCurrentData():
    bitt = {}
    price = {}
    coin_pair = []
    fee = getFee()["trade"]
    data = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries").json()["result"]

    for coin in coin_list:
        if coin == "BTC":
            continue
        bitt[coin] = {}
        for curr in curr_default:
            pair = "%s-%s" % (curr,coin)
            if coin == curr:
                continue
            if pair in ban_list:
                continue
            bitt[coin][curr] = {}
            for i in range(0,len(data)):
                if data[i]["MarketName"] == pair:
                    bitt[coin][curr]["Last"] = data[i]["Last"]
                    bitt[coin][curr]["Bid"] = data[i]["Bid"]
                    bitt[coin][curr]["Ask"] = data[i]["Ask"]

    for coin in coin_list:
        for curr in curr_list:
            if coin == "BTC":
                continue
            if curr in curr_default:
                continue
            if coin == curr:
                continue
            else:
                bitt[coin][curr] = {}
                price["curr"] = bitt[curr]["BTC"]
                price["coin"] = bitt[coin]["BTC"]
                bitt[coin][curr]["Ask"] = (price["coin"]["Ask"]/(1-fee["buy"]))/(price["curr"]["Bid"]*(1-fee["sell"]))
                bitt[coin][curr]["Bid"] = (price["coin"]["Bid"]/(1-fee["buy"]))/(price["curr"]["Ask"]*(1-fee["sell"]))
            
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
