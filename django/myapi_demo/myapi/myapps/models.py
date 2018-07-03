from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    top_speed = models.IntegerField()

    def __str__(self):
        return self.car_name


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TbBackpaylist(models.Model):
    enterprise = models.CharField(max_length=180, blank=True, null=True)
    project_name = models.CharField(max_length=200, blank=True, null=True)
    backpay_people = models.IntegerField(blank=True, null=True)
    backpay_money = models.FloatField(blank=True, null=True)
    happen_date = models.DateField(blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_backpaylist'

    def __str__(self):
        return self.enterprise

class TbCreditrecord(models.Model):
    institution = models.CharField(max_length=50, blank=True, null=True)
    qualification_no = models.CharField(max_length=20, blank=True, null=True)
    punish_date = models.DateField(blank=True, null=True)
    punish_dept = models.CharField(max_length=50, blank=True, null=True)
    punish_type = models.CharField(max_length=50, blank=True, null=True)
    punish_reason = models.TextField(blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_creditrecord'


class TbFrauds2(models.Model):
    executed_name = models.CharField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    identity_number = models.CharField(max_length=50, blank=True, null=True)
    court = models.CharField(max_length=200, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    case_number = models.CharField(max_length=100, blank=True, null=True)
    performance = models.CharField(max_length=100, blank=True, null=True)
    disrupt_type_name = models.TextField(blank=True, null=True)
    duty = models.TextField(blank=True, null=True)
    release_time = models.CharField(max_length=50, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)
    data_resource = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_frauds2'

    def __str__(self):
        return self.executed_name


class TbFrauds(models.Model):
    executed_name = models.CharField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    identity_number = models.CharField(max_length=50, blank=True, null=True)
    court = models.CharField(max_length=200, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    case_number = models.CharField(max_length=100, blank=True, null=True)
    performance = models.CharField(max_length=100, blank=True, null=True)
    disrupt_type_name = models.TextField(blank=True, null=True)
    duty = models.TextField(blank=True, null=True)
    release_time = models.CharField(max_length=50, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)
    data_resource = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_frauds_'


class TbGdcic(models.Model):
    enterprise = models.CharField(max_length=180, blank=True, null=True)
    enterprise_link = models.CharField(max_length=380, blank=True, null=True)
    punish_file = models.CharField(max_length=100, blank=True, null=True)
    punish_file_no = models.CharField(max_length=50, blank=True, null=True)
    punish_dept = models.CharField(max_length=80, blank=True, null=True)
    punish_date = models.DateField(blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_gdcic'


class TbMissed(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    appcet_unit = models.TextField(blank=True, null=True)
    apply_seral_number = models.BigIntegerField(blank=True, null=True)
    cancel_date = models.TextField(blank=True, null=True)
    certificate_book_type = models.TextField(blank=True, null=True)
    certificate_no = models.TextField(blank=True, null=True)
    certificate_type = models.TextField(blank=True, null=True)
    enterprise = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_missed'


class TbPersoninfo(models.Model):
    identity_card = models.CharField(max_length=100, blank=True, null=True)
    sexy = models.CharField(max_length=120, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    working_company_link = models.CharField(max_length=300, blank=True, null=True)
    register_certification_info_type = models.CharField(max_length=50, blank=True, null=True)
    register_certification_info_number = models.CharField(max_length=50, blank=True, null=True)
    register_certification_info_register_company = models.CharField(max_length=150, blank=True, null=True)
    register_certification_info_licence_issue_institution = models.CharField(max_length=50, blank=True, null=True)
    register_certification_info_licence_issue_date = models.CharField(max_length=50, blank=True, null=True)
    register_certification_info_validity = models.CharField(max_length=50, blank=True, null=True)
    certificate_title_info_level = models.CharField(max_length=500, blank=True, null=True)
    certificate_title_info_name = models.CharField(max_length=500, blank=True, null=True)
    certificate_title_info_issue_office = models.CharField(max_length=500, blank=True, null=True)
    certificate_title_info_issue_date = models.CharField(max_length=500, blank=True, null=True)
    certificate_title_info_validity = models.CharField(max_length=500, blank=True, null=True)
    safety_production_assessment_info_type = models.CharField(max_length=500, blank=True, null=True)
    safety_production_assessment_info_number = models.CharField(max_length=500, blank=True, null=True)
    safety_production_assessment_info_issue_office = models.CharField(max_length=500, blank=True, null=True)
    safety_production_assessment_info_issue_issue_date = models.CharField(max_length=500, blank=True, null=True)
    safety_production_assessment_info_issue_issue_validity = models.CharField(max_length=500, blank=True, null=True)
    job_certificate_information_info_name = models.CharField(db_column='Job_certificate_information_info_name',
                                                             max_length=500, blank=True,
                                                             null=True)  # Field name made lowercase.
    job_certificate_information_info_number = models.CharField(db_column='Job_certificate_information_info_number',
                                                               max_length=500, blank=True,
                                                               null=True)  # Field name made lowercase.
    job_certificate_information_info_issue_office = models.CharField(
        db_column='Job_certificate_information_info_issue_office', max_length=500, blank=True,
        null=True)  # Field name made lowercase.
    job_certificate_information_info_issue_date = models.CharField(
        db_column='Job_certificate_information_info_issue_date', max_length=500, blank=True,
        null=True)  # Field name made lowercase.
    job_certificate_information_info_issue_validity = models.CharField(
        db_column='Job_certificate_information_info_issue_validity', max_length=500, blank=True,
        null=True)  # Field name made lowercase.
    bad_behavious_number = models.CharField(max_length=500, blank=True, null=True)
    bad_behavious_punish_institution = models.CharField(max_length=500, blank=True, null=True)
    bad_behavious_punish_date = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_personinfo'


class TbPersonpunishment(models.Model):
    name = models.CharField(max_length=180, blank=True, null=True)
    punish_no = models.CharField(max_length=100, blank=True, null=True)
    punish_institution = models.CharField(max_length=120, blank=True, null=True)
    punish_date = models.CharField(max_length=50, blank=True, null=True)
    person_link = models.CharField(max_length=200, blank=True, null=True)
    punish_link = models.CharField(max_length=200, blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_personpunishment'


class TbQualCancel(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    cancel_date = models.TextField(blank=True, null=True)
    cancel_institution = models.TextField(blank=True, null=True)
    cancel_method = models.TextField(blank=True, null=True)
    cancel_qualification = models.TextField(blank=True, null=True)
    certificate = models.TextField(blank=True, null=True)
    certificate_no = models.TextField(blank=True, null=True)
    enterprise = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_qual_cancel'


class TbSafeaccident(models.Model):
    happend_date = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    development_corp = models.CharField(max_length=200, blank=True, null=True)
    contractor_construction = models.CharField(max_length=200, blank=True, null=True)
    development_charger = models.CharField(max_length=200, blank=True, null=True)
    construction_manger = models.CharField(max_length=200, blank=True, null=True)
    construction_charger = models.CharField(max_length=200, blank=True, null=True)
    project_director_supervising = models.CharField(max_length=200, blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_safeaccident'

# remote mysql db
class BaiduSearchLink(models.Model):
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    card_bin = models.CharField(max_length=15, blank=True, null=True)
    search_url = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baidu_search_link'


class Bid(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    stat = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.CharField(max_length=50, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    crawtime = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=2000, blank=True, null=True)
    contact = models.CharField(max_length=2000, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bid'


class Bidchance(models.Model):
    bidtype = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    pubdate = models.CharField(max_length=20, blank=True, null=True)
    bidno = models.CharField(max_length=30, blank=True, null=True)
    buyer = models.CharField(max_length=255, blank=True, null=True)
    bidcompany = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postalcode = models.CharField(max_length=20, blank=True, null=True)
    deadline = models.CharField(max_length=20, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    crawltime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bidchance'


class CaseResult(models.Model):
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    name = models.CharField(max_length=64, blank=True, null=True)
    url = models.CharField(max_length=64, blank=True, null=True)
    beg_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    para_in = models.CharField(max_length=1024, blank=True, null=True)
    para_rin = models.CharField(max_length=1024, blank=True, null=True)
    para_rout = models.CharField(max_length=1024, blank=True, null=True)
    para_out = models.CharField(max_length=1024, blank=True, null=True)
    expected_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_result'


class CompanyBankCard(models.Model):
    website_id = models.CharField(max_length=300, blank=True, null=True)
    website_url = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    baidu_cache_url = models.CharField(max_length=800, blank=True, null=True)
    cache_html = models.TextField(blank=True, null=True)
    cache_text = models.TextField(blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_bank_card'


class ConstructionBadRecord(models.Model):
    record_number = models.CharField(max_length=50, blank=True, null=True)
    record_body = models.CharField(max_length=100, blank=True, null=True)
    record_body_url = models.CharField(max_length=100, blank=True, null=True)
    decision_content = models.CharField(max_length=500, blank=True, null=True)
    decision_date = models.CharField(max_length=15, blank=True, null=True)
    cause = models.CharField(max_length=300, blank=True, null=True)
    implement_dept = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    release_validity_period = models.CharField(max_length=15, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construction_bad_record'


class ConstructionBlacklist(models.Model):
    record_body = models.CharField(max_length=150, blank=True, null=True)
    record_body_url = models.CharField(max_length=100, blank=True, null=True)
    assert_basis = models.CharField(max_length=300, blank=True, null=True)
    assert_dept = models.CharField(max_length=100, blank=True, null=True)
    blacklist_date = models.CharField(max_length=20, blank=True, null=True)
    remove_blacklist_date = models.CharField(max_length=20, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construction_blacklist'


class ConstructionEnterprise(models.Model):
    unified_social_credit_code = models.CharField(max_length=50, blank=True, null=True)
    org_code_bus_licenseno = models.CharField(db_column='org_code_bus_licenseNO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enterprise_name = models.CharField(max_length=100, blank=True, null=True)
    legal = models.CharField(max_length=20, blank=True, null=True)
    register_local = models.CharField(max_length=20, blank=True, null=True)
    business_address = models.CharField(max_length=100, blank=True, null=True)
    register_type = models.CharField(max_length=30, blank=True, null=True)
    enterprise_url = models.CharField(max_length=100, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construction_enterprise'


class ConstructionEnterpriseQualification(models.Model):
    enterprise_name = models.CharField(max_length=100, blank=True, null=True)
    enterprise_url = models.CharField(max_length=100, blank=True, null=True)
    qualification_type = models.CharField(max_length=50, blank=True, null=True)
    qualification_certificate_no = models.CharField(db_column='qualification_certificate_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qualification_name = models.CharField(max_length=100, blank=True, null=True)
    issue_date = models.CharField(max_length=15, blank=True, null=True)
    certificate_validity_period = models.CharField(max_length=15, blank=True, null=True)
    issue_org = models.CharField(max_length=50, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construction_enterprise_qualification'


class DianpingCategory(models.Model):
    url = models.CharField(max_length=400, blank=True, null=True)
    category_ids = models.CharField(max_length=255, blank=True, null=True)
    region_ids = models.CharField(max_length=600, blank=True, null=True)
    sub_region_ids = models.CharField(max_length=600, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    crawed_page = models.CharField(max_length=500, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dianping_category'


class DianpingCategory1(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    regions = models.CharField(max_length=255, blank=True, null=True)
    subregions = models.CharField(max_length=255, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dianping_category1'


class DianpingCityList(models.Model):
    cityname = models.CharField(db_column='cityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cityurl = models.CharField(db_column='cityUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dianping_city_list'


class DianpingFood(models.Model):
    shop_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    star = models.CharField(max_length=50, blank=True, null=True)
    taste = models.CharField(max_length=10, blank=True, null=True)
    env = models.CharField(max_length=10, blank=True, null=True)
    service = models.CharField(max_length=10, blank=True, null=True)
    mean_price = models.CharField(max_length=50, blank=True, null=True)
    review_num = models.CharField(max_length=255, blank=True, null=True)
    detail_add = models.CharField(max_length=255, blank=True, null=True)
    shop_type = models.CharField(max_length=255, blank=True, null=True)
    shop_dist = models.CharField(max_length=255, blank=True, null=True)
    shop_url = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    craw_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dianping_food'


class DianpingPage(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=1000, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    crawed_pages = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dianping_page'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EnvPunishment(models.Model):
    punishment_no = models.CharField(db_column='punishment_NO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unit_name = models.CharField(max_length=200, blank=True, null=True)
    credit_code = models.CharField(max_length=200, blank=True, null=True)
    punishment = models.CharField(max_length=800, blank=True, null=True)
    punishment_dept = models.CharField(max_length=200, blank=True, null=True)
    punishment_date = models.CharField(max_length=50, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'env_punishment'


class JobMonitor(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    work_address = models.CharField(max_length=255, blank=True, null=True)
    pub_date = models.CharField(max_length=25, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_monitor'


class Moneyblacklist(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    third_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    un_list_type = models.CharField(max_length=255, blank=True, null=True)
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    listed_on = models.CharField(max_length=255, blank=True, null=True)
    name_original_script = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    list_type = models.CharField(max_length=255, blank=True, null=True)
    last_day_updated = models.CharField(max_length=255, blank=True, null=True)
    individual_date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    type_of_document = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=500, blank=True, null=True)
    entity_alias = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    blacklist_name = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneyblacklist'


class MoneyblacklistCopy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    third_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    un_list_type = models.CharField(max_length=255, blank=True, null=True)
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    listed_on = models.CharField(max_length=255, blank=True, null=True)
    name_original_script = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    list_type = models.CharField(max_length=255, blank=True, null=True)
    last_day_updated = models.CharField(max_length=255, blank=True, null=True)
    individual_date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    type_of_document = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=500, blank=True, null=True)
    entity_alias = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneyblacklist_copy'


class Product(models.Model):
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    name = models.CharField(max_length=64, blank=True, null=True)
    addr = models.CharField(max_length=64, blank=True, null=True)
    sid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('sid', 'name'),)


class ProductCase(models.Model):
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    name = models.CharField(max_length=64, blank=True, null=True)
    addr = models.CharField(max_length=64, blank=True, null=True)
    pid = models.IntegerField()
    protocol = models.CharField(max_length=16, blank=True, null=True)
    method = models.CharField(max_length=16, blank=True, null=True)
    para_in = models.CharField(max_length=1024, blank=True, null=True)
    expected_results = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_case'
        unique_together = (('pid', 'name'),)


class ProductQuality(models.Model):
    enterprise_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_detail_name = models.CharField(max_length=200, blank=True, null=True)
    specifications = models.CharField(max_length=200, blank=True, null=True)
    product_grade = models.CharField(max_length=200, blank=True, null=True)
    batch_number = models.CharField(max_length=50, blank=True, null=True)
    test_results = models.CharField(max_length=50, blank=True, null=True)
    unqualified_project = models.CharField(max_length=50, blank=True, null=True)
    tester = models.CharField(max_length=50, blank=True, null=True)
    test_date = models.CharField(max_length=50, blank=True, null=True)
    test_type = models.CharField(max_length=50, blank=True, null=True)
    sampling_source = models.CharField(max_length=50, blank=True, null=True)
    test_org = models.CharField(max_length=50, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_quality'


class Service(models.Model):
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    addr = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class TaxPunishment(models.Model):
    taxpayer = models.CharField(max_length=255, blank=True, null=True)
    taxpayer_identity_no = models.CharField(db_column='taxpayer_identity_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    org_code = models.CharField(max_length=50, blank=True, null=True)
    reg_address = models.CharField(max_length=255, blank=True, null=True)
    legal_info = models.CharField(max_length=255, blank=True, null=True)
    finance_info = models.CharField(max_length=255, blank=True, null=True)
    agency_info = models.CharField(max_length=255, blank=True, null=True)
    case_nature = models.CharField(max_length=255, blank=True, null=True)
    illegality = models.TextField(blank=True, null=True)
    punishment = models.TextField(blank=True, null=True)
    unique_key = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_punishment'


class TbBackpaylist(models.Model):
    enterprise = models.CharField(max_length=180, blank=True, null=True)
    enterprise_link = models.CharField(max_length=380, blank=True, null=True)
    project_link = models.CharField(max_length=380, blank=True, null=True)
    project_name = models.CharField(max_length=200, blank=True, null=True)
    backpay_people = models.IntegerField(blank=True, null=True)
    backpay_money = models.FloatField(blank=True, null=True)
    happen_date = models.DateField(blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_backpaylist'


class TbCreditrecord(models.Model):
    institution = models.CharField(max_length=50, blank=True, null=True)
    qualification_no = models.CharField(max_length=20, blank=True, null=True)
    punish_date = models.DateField(blank=True, null=True)
    punish_dept = models.CharField(max_length=50, blank=True, null=True)
    punish_type = models.CharField(max_length=50, blank=True, null=True)
    punish_reason = models.TextField(blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_creditrecord'


class TbEnterpriseBadBehavious(models.Model):
    enterprise_name = models.CharField(max_length=180, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    punish_institution = models.CharField(max_length=120, blank=True, null=True)
    punish_date = models.CharField(max_length=50, blank=True, null=True)
    company_link = models.CharField(max_length=200, blank=True, null=True)
    project_link = models.CharField(max_length=200, blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_enterprise_bad_behavious'


class TbEnterpriseBlacklist(models.Model):
    enterprise_name = models.CharField(max_length=180, blank=True, null=True)
    blacklist_type = models.CharField(max_length=100, blank=True, null=True)
    identified_institution = models.CharField(max_length=120, blank=True, null=True)
    identified_date = models.CharField(max_length=50, blank=True, null=True)
    enterprise_link = models.CharField(max_length=200, blank=True, null=True)
    blacklist_type_link = models.CharField(max_length=200, blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_enterprise_blacklist'


class TbFrauds(models.Model):
    executed_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    identity_number = models.CharField(max_length=50, blank=True, null=True)
    court = models.CharField(max_length=200, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    case_number = models.CharField(max_length=100, blank=True, null=True)
    performance = models.CharField(max_length=100, blank=True, null=True)
    disrupt_type_name = models.TextField(blank=True, null=True)
    duty = models.TextField(blank=True, null=True)
    release_time = models.CharField(max_length=50, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)
    data_resource = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_frauds'


class TbFrauds2(models.Model):
    executed_name = models.CharField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    identity_number = models.CharField(max_length=50, blank=True, null=True)
    court = models.CharField(max_length=200, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    case_number = models.CharField(max_length=100, blank=True, null=True)
    performance = models.CharField(max_length=100, blank=True, null=True)
    disrupt_type_name = models.TextField(blank=True, null=True)
    duty = models.TextField(blank=True, null=True)
    release_time = models.CharField(max_length=50, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)
    data_resource = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_frauds2'


class TbGdcic(models.Model):
    enterprise = models.CharField(max_length=180, blank=True, null=True)
    punish_file = models.CharField(max_length=100, blank=True, null=True)
    punish_file_no = models.CharField(max_length=50, blank=True, null=True)
    punish_dept = models.CharField(max_length=80, blank=True, null=True)
    punish_date = models.DateField(blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_gdcic'


class TbJszx(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    zx = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_jszx'


class TbPersonpunishment(models.Model):
    name = models.CharField(max_length=180, blank=True, null=True)
    punish_no = models.CharField(max_length=100, blank=True, null=True)
    punish_institution = models.CharField(max_length=120, blank=True, null=True)
    punish_date = models.CharField(max_length=50, blank=True, null=True)
    person_link = models.CharField(max_length=200, blank=True, null=True)
    punish_link = models.CharField(max_length=200, blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_personpunishment'


class TbQualCancel(models.Model):
    index = models.BigIntegerField(primary_key=True)
    cancel_date = models.TextField(blank=True, null=True)
    cancel_institution = models.TextField(blank=True, null=True)
    cancel_method = models.TextField(blank=True, null=True)
    cancel_qualification = models.TextField(blank=True, null=True)
    certificate = models.TextField(blank=True, null=True)
    certificate_no = models.TextField(blank=True, null=True)
    enterprise = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_qual_cancel'


class TbQualMissed(models.Model):
    index = models.BigIntegerField(primary_key=True)
    accept_unit = models.TextField(blank=True, null=True)
    apply_seral_number = models.BigIntegerField(blank=True, null=True)
    cancel_date = models.TextField(blank=True, null=True)
    certificate_book_type = models.TextField(blank=True, null=True)
    certificate_no = models.TextField(blank=True, null=True)
    certificate_type = models.TextField(blank=True, null=True)
    enterprise = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_qual_missed'


class TbSafeaccident(models.Model):
    happend_date = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    development_corp = models.CharField(max_length=200, blank=True, null=True)
    contractor_construction = models.CharField(max_length=200, blank=True, null=True)
    development_charger = models.CharField(max_length=200, blank=True, null=True)
    construction_manger = models.CharField(max_length=200, blank=True, null=True)
    construction_charger = models.CharField(max_length=200, blank=True, null=True)
    project_director_supervising = models.CharField(max_length=200, blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_safeaccident'


class User(models.Model):
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    password_hash = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Wenshu(models.Model):
    casename = models.CharField(db_column='caseName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    casetype = models.CharField(db_column='caseType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doc_guid = models.CharField(unique=True, max_length=50, blank=True, null=True)
    proceeding = models.CharField(max_length=200, blank=True, null=True)
    caseno = models.CharField(db_column='caseNo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    judgementdate = models.DateField(db_column='judgementDate', blank=True, null=True)  # Field name made lowercase.
    courtname = models.CharField(db_column='courtName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    brief = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    pubdate = models.CharField(max_length=10, blank=True, null=True)
    view_num = models.IntegerField(blank=True, null=True)
    crawtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wenshu'


class WenshuAnyou(models.Model):
    anyou = models.CharField(max_length=255, blank=True, null=True)
    anyou_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wenshu_anyou'


class WenshuAnyouDic(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    parentid = models.CharField(db_column='parentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=200, blank=True, null=True)
    key = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wenshu_anyou_dic'


class WenshuHelp(models.Model):
    anyou = models.CharField(max_length=255, blank=True, null=True)
    qdate = models.CharField(max_length=40, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    crawed_page = models.CharField(max_length=600, blank=True, null=True)
    crawtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wenshu_help'


class WsCha(models.Model):
    year = models.IntegerField(blank=True, null=True)
    first_court = models.CharField(max_length=500, blank=True, null=True)
    case_type = models.CharField(max_length=50, blank=True, null=True)
    case_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_cha'


class WsHelpv2(models.Model):
    qyear = models.IntegerField()
    param = models.CharField(max_length=500, blank=True, null=True)
    crawed_page = models.CharField(max_length=600, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_helpv2'
