from django.db import models

# Create your models here.
class TbBasicInfo(models.Model):

    index = models.BigIntegerField(primary_key=True)
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