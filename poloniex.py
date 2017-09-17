#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#

import string
import requests

coin_list = ["LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","NMC","XEM","XPM","XMR"]
curr_list = ["BTC","ETH","XMR","USDT","LTC","ETH","BCC","ZEC","XRP","NXT","ETC","BTS","DOGE","DASH","NMC","XEM","XPM","XMR"]
curr_default = ["BTC","ETH","XMR","USDT"]

def getCurrentData():
    data = requests.get("https://poloniex.com/public?command=returnTicker").json()

    polo = {}
    price = {}
    fee = getFee()["trade"]

    for coin in coin_list:
        polo[coin] = {}
        if coin == "BCC":
            polo["BCH"] = {}
        for curr in curr_default:
            if coin == curr:
                continue
            else:
                polo[coin][curr] = {}
                if coin == "BCC":
                    struct = "%s_%s" % (curr,"BCH")
                    if struct in data:
                        polo["BCH"][curr] = {}
                        polo["BCH"][curr]["Last"] = float(data[struct]["last"])
                        polo["BCH"][curr]["Bid"] = float(data[struct]["highestBid"])
                        polo["BCH"][curr]["Ask"] = float(data[struct]["lowestAsk"])
                else:
                    struct = "%s_%s" % (curr,coin)
                    if struct in data:
                        polo[coin][curr]["Last"] = float(data[struct]["last"])
                        polo[coin][curr]["Bid"] = float(data[struct]["highestBid"])
                        polo[coin][curr]["Ask"] = float(data[struct]["lowestAsk"])

    polo["BCC"] = polo["BCH"]

    for coin in coin_list:
        for curr in curr_list:
            if curr in curr_default:
                continue
            if coin == curr:
                continue
            else:
                struct = "%s_%s" % (curr,coin)
                if struct in data:
                    continue
                polo[coin][curr] = {}
                price["curr"] = polo[curr]["BTC"]
                price["coin"] = polo[coin]["BTC"]
                polo[coin][curr]["Ask"] = (price["coin"]["Ask"]/(1-fee["buy"]))/(price["curr"]["Bid"]*(1-fee["sell"]))
                polo[coin][curr]["Bid"] = (price["coin"]["Bid"]/(1-fee["buy"]))/(price["curr"]["Ask"]*(1-fee["sell"]))

    return polo

def getCoinList():

    return coin_list

def getCurrList():

    return curr_list

def getFee():
    fee = {}
    fee["trade"] = {}
    fee["trade"]["buy"] = 0.00025
    fee["trade"]["sell"] = 0.00015

    for coin in coin_list:
        fee[coin] = {}

    fee["BTC"] = {}
    fee["BTC"]["rate"] = 0
    fee["BTC"]["static"] = 0.0001
    fee["LTC"]["rate"] = 0
    fee["LTC"]["static"] = 0.001
    fee["ETH"]["rate"] = 0
    fee["ETH"]["static"] = 0.005
    fee["BCC"]["rate"] = 0
    fee["BCC"]["static"] = 0.0001
    fee["ZEC"]["rate"] = 0
    fee["ZEC"]["static"] = 0.001
    fee["XRP"]["rate"] = 0
    fee["XRP"]["static"] = 0.15
    fee["NXT"]["rate"] = 0
    fee["NXT"]["static"] = 1
    fee["ETC"]["rate"] = 0
    fee["ETC"]["static"] = 0.01
    fee["BTS"]["rate"] = 0
    fee["BTS"]["static"] = 5
    fee["DOGE"]["rate"] = 0
    fee["DOGE"]["static"] = 5
    fee["DASH"]["rate"] = 0
    fee["DASH"]["static"] = 0.01
    fee["NMC"]["rate"] = 0
    fee["NMC"]["static"] = 0.01
    fee["XEM"]["rate"] = 0
    fee["XEM"]["static"] = 15
    fee["XPM"]["rate"] = 0
    fee["XPM"]["static"] = 0.01
    fee["XMR"]["rate"] = 0
    fee["XMR"]["static"] = 0.05

    return fee