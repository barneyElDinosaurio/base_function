from django.db import models

# Create your models here.
class HljShixin1106(models.Model):
    case_no = models.CharField(max_length=255, blank=True, null=True)
    frname1 = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    cidno = models.CharField(max_length=255, blank=True, null=True)
    frname2 = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    exec_court = models.CharField(max_length=255, blank=True, null=True)
    exec_accroding_to = models.CharField(max_length=255, blank=True, null=True)
    exec_accroding_department = models.CharField(max_length=255, blank=True, null=True)
    fulfill_status = models.CharField(max_length=255, blank=True, null=True)
    fulfill_detail_info = models.CharField(max_length=255, blank=True, null=True)
    fulfilled = models.CharField(max_length=255, blank=True, null=True)
    not_fulfill = models.CharField(max_length=255, blank=True, null=True)
    file_time = models.CharField(max_length=255, blank=True, null=True)
    pub_time = models.CharField(max_length=255, blank=True, null=True)
    crawl_time = models.CharField(max_length=255, blank=True, null=True)
    page_no = models.IntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        app_label = 'crawler'
        managed = False
        db_table = 'hlj_shixin_1106'
        # ordering=['name']