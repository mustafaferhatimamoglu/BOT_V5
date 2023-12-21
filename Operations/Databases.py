#importing the library
import pymssql
conn = pymssql.connect( 
    server='172.19.208.1', 
    user='sa', 
    password='sapass',
    database='BINANCE_V3_002',
    as_dict=True 
)
#print('Connection Established')
cursor = conn.cursor()
#print('Cursor Established')

def SQL(SQL_Query):
    cursor.execute(SQL_QUERY)
    
def CreateTable_KlineData(var_CoinName,var_Interval):
    sql_Query ="""
    --GO
--/****** Object:  Table [dbo].[{0}_{1}]    Script Date: 21.12.2023 19:07:21 ******/
SET ANSI_NULLS ON
--GO

SET QUOTED_IDENTIFIER ON
--GO

CREATE TABLE [dbo].[{0}_{1}](
	[Kline_open_time] [bigint] NOT NULL,
	[Open_price] [decimal](30, 15) NOT NULL,
	[High_price] [decimal](30, 15) NOT NULL,
	[Low_price] [decimal](30, 15) NOT NULL,
	[Close_price] [decimal](30, 15) NOT NULL,
	[Volume] [decimal](30, 15) NOT NULL,
	[Kline_close_time] [bigint] NOT NULL,
	[Quote_asset_volume] [decimal](30, 15) NOT NULL,
	[Number_of_trades] [int] NOT NULL,
	[Taker_buy_base_asset_volume] [decimal](30, 15) NOT NULL,
	[Taker_buy_quote_asset_volume] [decimal](30, 15) NOT NULL,
 CONSTRAINT [PK_{0}_{1}] PRIMARY KEY CLUSTERED 
(
	[Kline_open_time] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
--GO
""".format(var_CoinName,var_Interval)
    #print(sql_Query)    
    try:
        cursor.execute(sql_Query) 
        conn.commit()
        print('Kline Table Created')
    except Exception as exp:
        print('error')
        print(exp)
