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
    data = requests.get("https://poloniex.com/public?command=returnTicker").json()

    polo = {}
    polo["ltc"] = data["BTC_LTC"]["last"]
    polo["eth"] = data["BTC_ETH"]["last"]
    polo["bcc"] = data["BTC_BCH"]["last"]
    polo["zec"] = data["BTC_ZEC"]["last"]
    polo["xrp"] = data["BTC_XRP"]["last"]
    polo["nxt"] = data["BTC_NXT"]["last"]
    polo["etc"] = data["BTC_ETC"]["last"]
    polo["bts"] = data["BTC_BTS"]["last"]
    polo["doge"] = data["BTC_DOGE"]["last"]
    polo["dash"] = data["BTC_DASH"]["last"]
    polo["nmc"] = data["BTC_NMC"]["last"]
    polo["xem"] = data["BTC_XEM"]["last"]
    polo["xpm"] = data["BTC_XPM"]["last"]
    polo["xmr"] = data["BTC_XMR"]["last"]

    return polo

def getFee():
    fee = {}
    fee["trade"] = 0.0002
    fee["btc"]["rate"] = 0
    fee["btc"]["static"] = 0.0001
    fee["ltc"]["rate"] = 0
    fee["ltc"]["static"] = 0.001
    fee["eth"]["rate"] = 0
    fee["eth"]["static"] = 0.005
    fee["bcc"]["rate"] = 0
    fee["bcc"]["static"] = 0.0001
    fee["zec"]["rate"] = 0
    fee["zec"]["static"] = 0.001
    fee["xrp"]["rate"] = 0
    fee["xrp"]["static"] = 0.15
    fee["nxt"]["rate"] = 0
    fee["nxt"]["static"] = 1
    fee["etc"]["rate"] = 0
    fee["etc"]["static"] = 0.01
    fee["bts"]["rate"] = 0
    fee["bts"]["static"] = 5
    fee["doge"]["rate"] = 0
    fee["doge"]["static"] = 5
    fee["dash"]["rate"] = 0
    fee["dash"]["static"] = 0.01
    fee["nmc"]["rate"] = 0
    fee["nmc"]["static"] = 0.01
    fee["xem"]["rate"] = 0
    fee["xem"]["static"] = 15
    fee["xpm"]["rate"] = 0
    fee["xpm"]["static"] = 0.01
    fee["xmr"]["rate"] = 0
    fee["xmr"]["static"] = 0.05

    return fee