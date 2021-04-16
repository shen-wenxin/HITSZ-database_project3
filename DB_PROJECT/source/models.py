from django.db import models
from django.utils import timezone
import json

# 课程
class CourseInfo(models.Model):
    course_id = models.TextField('课程编号', primary_key=True,null=False)
    name = models.TextField('课程名字',max_length=200,null=False)
    course_teachers = models.CharField("任课教师",max_length=200)

    class Meta:
        db_table ="CourseInfo"
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name
    
    def set_course_teachers(self,x):
        self.course_teachers = json.dumps(x)
    
    def get_course_teachers(self):
        return json.loads(self.course_teachers)

    def __str__(self):
        return self.name

# 资源表
class FileInfo(models.Model):
    file_name = models.TextField('文件名称',max_length=200,null=False)
    remarks = models.TextField('文件备注',max_length=200,null=False)
    upload_time = models.DateTimeField('上传时间',default=timezone.now)
    uploader_id = models.TextField('上传者编号', max_length=20)
    download_times = models.IntegerField('下载次数', default=0)
    file_info = models.FileField(upload_to = 'upload/%Y%m%d')
    course = models.ForeignKey(CourseInfo,on_delete=models.CASCADE)
    class Meta:
        db_table ="FileInfo"
        verbose_name = "文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file_name


