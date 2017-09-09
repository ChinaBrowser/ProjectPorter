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
    bter_currs = bter.getCurrList()
    polo_list = poloniex.getCoinList()
    polo_currs = poloniex.getCurrList()
    bit_list = bitfinex.getCoinList()
    bit_currs = bitfinex.getCurrList()

    while True:
        bter_price = bter.getCurrentData() 
        polo_price = poloniex.getCurrentData()
        bit_price = bitfinex.getCurrentData()
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print currentTime
        #Bter
        for i in bter_currs:
            if i in bter_list:
                for p in bter_list:
                    if i == p:
                        continue

                    if p in polo_price and i in polo_price[p]:
                        ratio = polo_price[p][i]/bter_price[p][i]
                        if 1.15 > ratio > 1.035:
                            msg = "Bought %s from Bter via %s, Sold at Poloniex, %.4f%% profit, %s%% + %s %s fee" % (p,i,100*(float(ratio)-1),100*bter.getFee()[p]["rate"],bter.getFee()[p]["static"],p)
                            print msg

                    if p in bit_price and i in bit_price[p]:
                        ratio = bit_price[p][i]/bter_price[p][i]
                        if 1.15 > ratio > 1.035:
                            msg = "Bought %s from Bter via %s, Sold at Bitfinex, %.4f%% profit, %s%% + %s %s fee" % (p,i,100*(float(ratio)-1),100*bter.getFee()[p]["rate"],bter.getFee()[p]["static"],p)
                            print msg

        #Poloniex
        for i in polo_currs:
            if i in polo_list:
                for p in polo_list:
                    if i == p:
                        continue

                    if p in bter_price and i in bter_price[p] and i not in poloniex.curr_default:
                        #print "%s %s" % (p,i)
                        ratio = bter_price[p][i]/polo_price[p][i]
                        if 1.15 > ratio > 1.035:
                            msg = "Bought %s from Poloniex via %s, Sold at Bter, %.4f%% profit, %s %s fee" % (p,i,100*(float(ratio)-1),poloniex.getFee()[p]["static"],p)
                            print msg

                    if p in bit_price and i in bit_price[p] and i not in poloniex.curr_default:
                        ratio = bit_price[p][i]/polo_price[p][i]
                        if 1.15 > ratio > 1.035:
                            msg = "Bought %s from Poloniex via %s, Sold at Bitfinex, %.4f%% profit, %s %s fee" % (p,i,100*(float(ratio)-1),poloniex.getFee()[p]["static"],p)
                            print msg

        #Bitfinex
        for i in bit_currs:
            if i in bit_list:
                for p in bit_list:
                    if i == p:
                        continue

                    if p in polo_price and i in polo_price[p]:
                        ratio = polo_price[p][i]/bit_price[p][i]
                        if 1.15 > ratio > 1.035:
                            msg = "Bought %s from Bitfinex via %s, Sold at Poloniex, %.4f%% profit, %s %s fee" % (p,i,100*(float(ratio)-1),bitfinex.getFee()[p]["static"],p)
                            print msg

                    if p in bter_price and i in bter_price[p]:
                        ratio = bter_price[p][i]/bit_price[p][i]
                        if 1.15 > ratio > 1.035:
                            msg = "Bought %s from Bitfinex via %s, Sold at Bter, %.4f%% profit, %s %s fee" % (p,i,100*(float(ratio)-1),bitfinex.getFee()[p]["static"],p)
                            print msg

        time.sleep(delay)

if __name__ == '__main__':
    main()
