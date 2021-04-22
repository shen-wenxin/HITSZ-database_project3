from django.db import models
from django.utils import timezone
import json
from course.models import Course

# 资源表
class FileInfo(models.Model):
    file_name = models.TextField('文件名称',max_length=200,null=False)
    remarks = models.TextField('文件备注',max_length=200,null=False)
    upload_time = models.DateTimeField('上传时间',default=timezone.now)
    uploader_id = models.TextField('上传者', max_length=20,db_index = True)
    download_times = models.IntegerField('下载次数', default=0)
    file_info = models.FileField(upload_to = 'upload/%Y%m%d')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    class Meta:
        db_table ="FileInfo"
        verbose_name = "文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file_name


