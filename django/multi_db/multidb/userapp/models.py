# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TbJobs(models.Model):

    companyid = models.IntegerField(db_column='companyId', blank=True, null=True)  # Field name made lowercase.
    positionid = models.IntegerField(db_column='positionId', blank=True, null=True)  # Field name made lowercase.
    jobnature = models.TextField(db_column='jobNature', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=160, blank=True, null=True)  # Field name made lowercase.
    financestage = models.CharField(db_column='financeStage', max_length=160, blank=True, null=True)  # Field name made lowercase.
    companyfullname = models.CharField(db_column='companyFullName', max_length=160, blank=True, null=True)  # Field name made lowercase.
    companysize = models.CharField(db_column='companySize', max_length=160, blank=True, null=True)  # Field name made lowercase.
    industryfield = models.CharField(db_column='industryField', max_length=160, blank=True, null=True)  # Field name made lowercase.
    positionname = models.CharField(db_column='positionName', max_length=160, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=160, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=80, blank=True, null=True)  # Field name made lowercase.
    salary_low = models.IntegerField(blank=True, null=True)
    salary_high = models.IntegerField(blank=True, null=True)
    workyear = models.CharField(db_column='workYear', max_length=160, blank=True, null=True)  # Field name made lowercase.
    education = models.CharField(max_length=160, blank=True, null=True)
    positionadvantage = models.CharField(db_column='positionAdvantage', max_length=160, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(max_length=160, blank=True, null=True)
    companylabellist = models.CharField(db_column='companyLabelList', max_length=320, blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label='userdb'
        managed = False
        db_table = 'tb_jobs'
