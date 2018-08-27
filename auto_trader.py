# -*- coding: utf-8 -*-
# @Time : 2018/8/27 23:04
# @File : auto_trader.py
import config
from easytrader import helpers
import easytrader
user = easytrader.use('ths')
user.connect(r'C:\Tool\gjzq\国金证券同花顺独立下单\xiadan.exe')
# user.prepare(user=config.username, password=config.password)
print('余额')
print(user.balance)
print('持仓')
# print(user.position)
for item in user.position:
    print(item)

# 当日成交
print(user.today_trades)

ipo_data = helpers.get_today_ipo_data()
# 当日可以申购的新股
print(ipo_data)

try:
    user.buy('123009', price=110, amount=100)
except Exception as e:
    print(e)