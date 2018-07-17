# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbBankCash(models.Model):
    日期 = models.DateTimeField(blank=True, null=True)
    操作 = models.TextField(blank=True, null=True)
    发生金额 = models.FloatField(blank=True, null=True)
    账号 = models.CharField(max_length=20, blank=True, null=True)
    备注 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bank_cash'


class TbBasicInfo(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    pe = models.FloatField(blank=True, null=True)
    outstanding = models.FloatField(blank=True, null=True)
    totals = models.FloatField(blank=True, null=True)
    totalassets = models.FloatField(db_column='totalAssets', blank=True, null=True)  # Field name made lowercase.
    liquidassets = models.FloatField(db_column='liquidAssets', blank=True, null=True)  # Field name made lowercase.
    fixedassets = models.FloatField(db_column='fixedAssets', blank=True, null=True)  # Field name made lowercase.
    reserved = models.FloatField(blank=True, null=True)
    reservedpershare = models.FloatField(db_column='reservedPerShare', blank=True, null=True)  # Field name made lowercase.
    esp = models.FloatField(blank=True, null=True)
    bvps = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    timetomarket = models.BigIntegerField(db_column='timeToMarket', blank=True, null=True)  # Field name made lowercase.
    undp = models.FloatField(blank=True, null=True)
    perundp = models.FloatField(blank=True, null=True)
    rev = models.FloatField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    gpr = models.FloatField(blank=True, null=True)
    npr = models.FloatField(blank=True, null=True)
    holders = models.FloatField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_basic_info'


class TbBlacklist(models.Model):
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', primary_key=True, max_length=6)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='REASON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_blacklist'


class TbCnstock(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=80, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', primary_key=True, max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_cnstock'


class TbDeliveryGj(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    成交日期 = models.TextField(blank=True, null=True)
    证券代码 = models.TextField(blank=True, null=True)
    证券名称 = models.TextField(blank=True, null=True)
    操作 = models.TextField(blank=True, null=True)
    成交数量 = models.FloatField(blank=True, null=True)
    成交均价 = models.FloatField(blank=True, null=True)
    成交金额 = models.FloatField(blank=True, null=True)
    余额 = models.FloatField(blank=True, null=True)
    发生金额 = models.FloatField(blank=True, null=True)
    手续费 = models.FloatField(blank=True, null=True)
    印花税 = models.FloatField(blank=True, null=True)
    过户费 = models.FloatField(blank=True, null=True)
    本次金额 = models.TextField(blank=True, null=True)
    其他费用 = models.TextField(blank=True, null=True)
    交易市场 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_delivery_GJ'


class TbDeliveryHt(models.Model):
    成交日期 = models.DateTimeField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    摘要 = models.TextField(blank=True, null=True)
    证券名称 = models.TextField(blank=True, null=True)
    成交数量 = models.BigIntegerField(blank=True, null=True)
    成交均价 = models.FloatField(blank=True, null=True)
    成交金额 = models.FloatField(blank=True, null=True)
    手续费 = models.FloatField(blank=True, null=True)
    印花税 = models.FloatField(blank=True, null=True)
    其他杂费 = models.FloatField(blank=True, null=True)
    发生金额 = models.FloatField(blank=True, null=True)
    操作 = models.TextField(blank=True, null=True)
    证券代码 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_delivery_HT'


class TbProfit(models.Model):
    证券代码 = models.CharField(max_length=6, blank=True, null=True)
    证券名称 = models.CharField(max_length=16, blank=True, null=True)
    保本价 = models.FloatField(blank=True, null=True)
    股票余额 = models.IntegerField(blank=True, null=True)
    盈亏比例 = models.FloatField(blank=True, null=True)
    盈亏 = models.FloatField(blank=True, null=True)
    市值 = models.FloatField(blank=True, null=True)
    现价 = models.FloatField(blank=True, null=True)
    number_2018_04_12 = models.FloatField(db_column='2018-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_13 = models.FloatField(db_column='2018-04-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_16 = models.FloatField(db_column='2018-04-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_17 = models.FloatField(db_column='2018-04-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_18 = models.FloatField(db_column='2018-04-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_19 = models.FloatField(db_column='2018-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_20 = models.FloatField(db_column='2018-04-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_23 = models.FloatField(db_column='2018-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_24 = models.FloatField(db_column='2018-04-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_25 = models.FloatField(db_column='2018-04-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_26 = models.FloatField(db_column='2018-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_27 = models.FloatField(db_column='2018-04-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_02 = models.FloatField(db_column='2018-05-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_03 = models.FloatField(db_column='2018-05-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_04 = models.FloatField(db_column='2018-05-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_07 = models.FloatField(db_column='2018-05-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_08 = models.FloatField(db_column='2018-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_09 = models.FloatField(db_column='2018-05-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_10 = models.FloatField(db_column='2018-05-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_11 = models.FloatField(db_column='2018-05-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_14 = models.FloatField(db_column='2018-05-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_15 = models.FloatField(db_column='2018-05-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_16 = models.FloatField(db_column='2018-05-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_17 = models.FloatField(db_column='2018-05-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_18 = models.FloatField(db_column='2018-05-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_21 = models.FloatField(db_column='2018-05-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_25 = models.FloatField(db_column='2018-05-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_28 = models.FloatField(db_column='2018-05-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_29 = models.FloatField(db_column='2018-05-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_30 = models.FloatField(db_column='2018-05-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_31 = models.FloatField(db_column='2018-05-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_01 = models.FloatField(db_column='2018-06-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_04 = models.FloatField(db_column='2018-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_05 = models.FloatField(db_column='2018-06-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_06 = models.FloatField(db_column='2018-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_07 = models.FloatField(db_column='2018-06-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_08 = models.FloatField(db_column='2018-06-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_11 = models.FloatField(db_column='2018-06-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_12 = models.FloatField(db_column='2018-06-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_13 = models.FloatField(db_column='2018-06-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_14 = models.FloatField(db_column='2018-06-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_15 = models.FloatField(db_column='2018-06-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_19 = models.FloatField(db_column='2018-06-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_20 = models.FloatField(db_column='2018-06-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_21 = models.FloatField(db_column='2018-06-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_22 = models.FloatField(db_column='2018-06-22', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_28 = models.FloatField(db_column='2018-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_29 = models.FloatField(db_column='2018-06-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_07_04 = models.FloatField(db_column='2018-07-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tb_profit'


class TbProfitHistory(models.Model):
    证券代码 = models.CharField(max_length=6, blank=True, null=True)
    证券名称 = models.CharField(max_length=16, blank=True, null=True)
    保本价 = models.FloatField(blank=True, null=True)
    股票余额 = models.IntegerField(blank=True, null=True)
    盈亏比例 = models.FloatField(blank=True, null=True)
    盈亏 = models.FloatField(blank=True, null=True)
    市值 = models.FloatField(blank=True, null=True)
    现价 = models.FloatField(blank=True, null=True)
    number_2018_04_12 = models.FloatField(db_column='2018-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_13 = models.FloatField(db_column='2018-04-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_16 = models.FloatField(db_column='2018-04-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_17 = models.FloatField(db_column='2018-04-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_18 = models.FloatField(db_column='2018-04-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_19 = models.FloatField(db_column='2018-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_20 = models.FloatField(db_column='2018-04-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_23 = models.FloatField(db_column='2018-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_24 = models.FloatField(db_column='2018-04-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_25 = models.FloatField(db_column='2018-04-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_26 = models.FloatField(db_column='2018-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tb_profit_history'


class TbSimulation(models.Model):
    当前日期 = models.DateField(blank=True, null=True)
    买入日期 = models.DateField(blank=True, null=True)
    代码 = models.CharField(max_length=16, blank=True, null=True)
    股票名称 = models.CharField(max_length=32, blank=True, null=True)
    买入价格 = models.FloatField(blank=True, null=True)
    当前价格 = models.FloatField(blank=True, null=True)
    今日涨幅 = models.FloatField(blank=True, null=True)
    盈亏比例 = models.FloatField(blank=True, null=True)
    买入原因 = models.TextField(blank=True, null=True)
    支撑_压力_位置 = models.FloatField(db_column='支撑(压力)位置', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tb_simulation'


class TbSoldProfit(models.Model):
    证券代码 = models.CharField(max_length=6, blank=True, null=True)
    证券名称 = models.CharField(max_length=16, blank=True, null=True)
    保本价 = models.FloatField(blank=True, null=True)
    股票余额 = models.IntegerField(blank=True, null=True)
    盈亏比例 = models.FloatField(blank=True, null=True)
    盈亏 = models.FloatField(blank=True, null=True)
    市值 = models.FloatField(blank=True, null=True)
    现价 = models.FloatField(blank=True, null=True)
    number_2018_04_12 = models.FloatField(db_column='2018-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_13 = models.FloatField(db_column='2018-04-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_16 = models.FloatField(db_column='2018-04-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_17 = models.FloatField(db_column='2018-04-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_18 = models.FloatField(db_column='2018-04-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_19 = models.FloatField(db_column='2018-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_20 = models.FloatField(db_column='2018-04-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_23 = models.FloatField(db_column='2018-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_24 = models.FloatField(db_column='2018-04-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tb_sold_profit'


class TbSoldStock(models.Model):
    代码 = models.CharField(unique=True, max_length=10, blank=True, null=True)
    股票名称 = models.CharField(max_length=20, blank=True, null=True)
    买入价 = models.FloatField(blank=True, null=True)
    卖出价 = models.FloatField(blank=True, null=True)
    当前价 = models.FloatField(blank=True, null=True)
    卖出后涨跌幅 = models.FloatField(blank=True, null=True)
    卖出日期 = models.DateField(blank=True, null=True)
    盈亏 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sold_stock'


class TbZdt(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    代码 = models.TextField(blank=True, null=True)
    名称 = models.TextField(blank=True, null=True)
    最新价格 = models.FloatField(blank=True, null=True)
    涨跌幅 = models.FloatField(blank=True, null=True)
    封成比 = models.FloatField(blank=True, null=True)
    封流比 = models.FloatField(blank=True, null=True)
    封单金额 = models.FloatField(blank=True, null=True)
    最后一次涨停时间 = models.TextField(blank=True, null=True)
    第一次涨停时间 = models.TextField(blank=True, null=True)
    打开次数 = models.BigIntegerField(blank=True, null=True)
    振幅 = models.FloatField(blank=True, null=True)
    涨停强度 = models.FloatField(blank=True, null=True)
    涨停日期 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_zdt'
