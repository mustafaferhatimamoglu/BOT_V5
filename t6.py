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
print(int((parsed_json["serverTime"]) / 1000))

serverTime = int(parsed_json["serverTime"])

counter_kline = 0
flag_KlineStop = False
data_starttime = 0

open_time = 0.0
open_price = 0.0
high_price = 0.0
low_price = 0.0
close_price = 0.0
volume = 0.0
close_time = 0.0
quote_asset_volume = 0.0
number_of_trades = 0.0
taker_buy_base_asset_volume = 0.0
taker_buy_quote_asset_volume = 0.0

#region Description
...
#endregion

while True:
    kline_response = um_futures_client.klines(
        "BTCUSDT", "1d", limit=999, starttime=data_starttime
    )
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
        # print(f"
        # Open Time: {open_time},
        # Open Price: {open_price},
        # High Price: {high_price},
        # Low Price: {low_price},
        # Close Price: {close_price},
        # Volume: {volume},
        # Close Time: {close_time},
        # Quote Asset Volume: {quote_asset_volume},
        # Number of Trades: {number_of_trades},
        # Taker Buy Base Asset Volume: {taker_buy_base_asset_volume},
        # Taker Buy Quote Asset Volume: {taker_buy_quote_asset_volume}")
        counter_kline += 1
        if serverTime < kline[6]:
            print(counter_kline)
            flag_KlineStop = True
            break
    if flag_KlineStop:
        break
    else:
        data_starttime = close_time + 1
        #print("aa")
