#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 FawkesPan
#
#

import time
import bter
import poloniex
import bitfinex

delay=10

def main():
    bter_list = bter.getCoinList()
    polo_list = poloniex.getCoinList()
    bit_list = bitfinex.getCoinList()

    while True:
        bter_price = bter.getCurrentData()
        polo_price = poloniex.getCurrentData()
        bit_price = bitfinex.getCurrentData()
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print currentTime
        for buy in bter_list: 
            for sell in polo_list:
                if buy == sell:
                    ratio = float(polo_price[sell])/float(bter_price[sell])
                    if ratio > 1.00:
                        msg = "Bought %s from Bter and Sold at Poloniex will produce %.5f%% profit." % (sell.upper(),100*(float(ratio)-1))
                    else:
                        ratio = float(bter_price[sell])/float(polo_price[sell])
                        msg = "Bought %s from Poloniex and Sold at Bter will produce %.5f%% profit." % (sell.upper(),100*(float(ratio)-1))
                    print msg
            for sell in bit_list:
                if buy == sell:
                    ratio = float(bit_price[sell])/float(bter_price[sell])
                    if ratio > 1.00:
                        msg = "Bought %s from Bter and Sold at Bitfinex will produce %.5f%% profit." % (sell.upper(),100*(float(ratio)-1))
                    else:
                        ratio = float(bter_price[sell])/float(bit_price[sell])
                        msg = "Bought %s from Bitfinex and Sold at Bter will produce %.5f%% profit." % (sell.upper(),100*(float(ratio)-1))
                    print msg
        time.sleep(delay)

if __name__ == '__main__':
    main()
