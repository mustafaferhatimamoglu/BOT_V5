from Operations import Databases
Databases.CreateTable_KlineData('BTCUSDT','1m')



import pymssql
conn = pymssql.connect(
    server="172.19.208.1",
    user="sa",
    password="sapass",
    database="BINANCE_V3_002",
    as_dict=True,
)

