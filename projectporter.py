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
import bittrex

delay=10
High=1.35
Low=1.01

def main():
    bter_list = bter.getCoinList()
    bter_currs = bter.getCurrList()
    bter_fee = bter.getFee()

    polo_list = poloniex.getCoinList()
    polo_currs = poloniex.getCurrList()
    polo_fee = poloniex.getFee()

    bit_list = bitfinex.getCoinList()
    bit_currs = bitfinex.getCurrList()
    bit_fee = bitfinex.getFee()

    bitt_list = bittrex.getCoinList()
    bitt_currs = bittrex.getCurrList()
    bitt_fee = bittrex.getFee()

    while True:
        bter_price = bter.getCurrentData() 
        polo_price = poloniex.getCurrentData()
        bit_price = bitfinex.getCurrentData()
        bitt_price = bittrex.getCurrentData()
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print currentTime
        #Bter
        for i in bter_currs:
            if i in bter_list:
                for p in bter_list:
                    if i == p:
                        continue

                    if p in polo_price and i in polo_price[p] and "Bid" in polo_price[p][i]:
                        ratio = polo_price[p][i]["Bid"]/bter_price[p][i]["Ask"]*(1-bter_fee[p]["rate"])
                        if High > ratio > Low:
                            msg = "%s (Send to Poloniex), Bter, %s (From Poloniex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bter_fee[p]["static"],p,polo_fee[i]["static"],i)
                            print msg

                    if p in bit_price and i in bit_price[p] and "Bid" in bit_price[p][i]:
                        ratio = bit_price[p][i]["Bid"]/bter_price[p][i]["Ask"]*(1-bter_fee[p]["rate"])
                        if High > ratio > Low:
                            msg = "%s (Send to Bitfinex), Bter, %s (From Bitfinex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bter_fee[p]["static"],p,bit_fee[i]["static"],i)
                            print msg

                    if p in bitt_price and i in bitt_price[p] and "Bid" in bitt_price[p][i]:
                        ratio = bitt_price[p][i]["Bid"]/bter_price[p][i]["Ask"]*(1-bter_fee[p]["rate"])
                        if High > ratio > Low:
                            msg = "%s (Send to Bittrex), Bter, %s (From Bittrex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bter_fee[p]["static"],p,bitt_fee[i]["static"],i)
                            print msg

        #Poloniex
        for i in polo_currs:
            if i in polo_list:
                for p in polo_list:
                    if i == p:
                        continue

                    if p in bter_price and i in bter_price[p] and i not in poloniex.curr_default and "Bid" in bter_price[p][i]:
                        #print "%s %s" % (p,i)
                        ratio = bter_price[p][i]["Bid"]/polo_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Bter), Poloniex, %s (From Bter), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),polo_fee[p]["static"],p,bter_fee[i]["static"],i)
                            print msg

                    if p in bit_price and i in bit_price[p] and i not in poloniex.curr_default and "Bid" in bit_price[p][i]:
                        ratio = bit_price[p][i]["Bid"]/polo_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Bitfinex), Poloniex, %s (From Bitfinex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),polo_fee[p]["static"],p,bit_fee[i]["static"],i)
                            print msg

                    if p in bitt_price and i in bitt_price[p] and i not in poloniex.curr_default and "Bid" in bitt_price[p][i]:
                        ratio = bitt_price[p][i]["Bid"]/polo_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Bittrex), Poloniex, %s (From Bittrex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),polo_fee[p]["static"],p,bitt_fee[i]["static"],i)
                            print msg

        #Bitfinex
        for i in bit_currs:
            if i in bit_list:
                for p in bit_list:
                    if i == p:
                        continue

                    if p in polo_price and i in polo_price[p] and "Bid" in polo_price[p][i]:
                        ratio = polo_price[p][i]["Bid"]/bit_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Poloniex), Bitfinex, %s (From Poloniex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bit_fee[p]["static"],p,polo_fee[i]["static"],i)
                            print msg

                    if p in bter_price and i in bter_price[p] and "Bid" in bter_price[p][i]:
                        ratio = bter_price[p][i]["Bid"]/bit_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Bter), Bitfinex, %s (From Bter), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bit_fee[p]["static"],p,bter_fee[i]["static"],i)
                            print msg

                    if p in bitt_price and i in bitt_price[p] and "Bid" in bitt_price[p][i]:
                        ratio = bitt_price[p][i]["Bid"]/bit_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Bittrex), Bitfinex, %s (From Bittrex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bit_fee[p]["static"],p,bitt_fee[i]["static"],i)
                            print msg

        #Bittrex
        for i in bitt_currs:
            if i in bitt_list:
                for p in bitt_list:
                    if i == p:
                        continue

                    if p in polo_price and i in polo_price[p] and p not in bittrex.curr_default and "Bid" in polo_price[p][i]:
                        ratio = polo_price[p][i]["Bid"]/bitt_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Poloniex), Bittrex, %s (From Poloniex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bitt_fee[p]["static"],p,polo_fee[i]["static"],i)
                            print msg

                    if p in bter_price and i in bter_price[p] and p not in bittrex.curr_default and (p != "NXT" or i != "ETH") and (p != "DOGE" or i != "ETH") and "Bid" in bter_price[p][i]:
                        ratio = bter_price[p][i]["Bid"]/bitt_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Bter), Bittrex, %s (From Bter), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bitt_fee[p]["static"],p,bter_fee[i]["static"],i)
                            print msg

                    if p in bit_price and i in bit_price[p] and p not in bittrex.curr_default and "Bid" in bit_price[p][i]:
                        ratio = bit_price[p][i]["Bid"]/bitt_price[p][i]["Ask"]
                        if High > ratio > Low:
                            msg = "%s (Send to Bitfinex), Bittrex, %s(From Bitfinex), %.4f%%, %s %s + %s %s" % (p,i,100*(float(ratio)-1),bitt_fee[p]["static"],p,bit_fee[i]["static"],i)
                            print msg

        time.sleep(delay)

if __name__ == '__main__':
    main()
