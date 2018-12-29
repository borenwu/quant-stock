import tushare as ts
import pandas as pd



pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)



# df = ts.get_index()
# df = ts.get_today_all()
# df = ts.get_today_ticks('601333')
pro = ts.pro_api()
# df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# df.to_csv("stock_index.csv")
indexes = pd.read_csv('stock_index.csv')
symbols = indexes['ts_code']
# print(df)
for symbol in symbols:
    # print(symbol)
    code = symbol.split('.')[0]
    print(code)
    df = ts.get_tick_data(code, date='2018-12-28', src='tt')
    print(df)
