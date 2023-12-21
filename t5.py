#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging

um_futures_client = UMFutures()


import json
dict_BinanceTime = um_futures_client.time()
string_BinanceTime = json.dumps(dict_BinanceTime)
parsed_json = json.loads(string_BinanceTime)

print(f"{parsed_json['serverTime']}")






kline_response = um_futures_client.klines("BTCUSDT", "1m",limit=3,starttime=0)
for kline in kline_response:
    open_time = kline[0]
    open_price = kline[1]
    high_price = kline[2]
    low_price = kline[3]
    close_price = kline[4]
    volume = kline[5]
    close_time = kline[6]
    quote_asset_volume = kline[7]
    number_of_trades = kline[8]
    taker_buy_base_asset_volume = kline[9]
    taker_buy_quote_asset_volume = kline[10]
    print(f"Open Time: {open_time}, Open Price: {open_price}, High Price: {high_price}, Low Price: {low_price}, Close Price: {close_price}, Volume: {volume}, Close Time: {close_time}, Quote Asset Volume: {quote_asset_volume}, Number of Trades: {number_of_trades}, Taker Buy Base Asset Volume: {taker_buy_base_asset_volume}, Taker Buy Quote Asset Volume: {taker_buy_quote_asset_volume}")
    
    
