from django.db import models

# 课程
class Course(models.Model):
    course_id = models.CharField('课程编号', primary_key=True,null=False,max_length=200)
    name = models.CharField('课程名字',max_length=200,null=False)
    course_teachers = models.TextField("任课教师",max_length=200,null=False)
    course_students = models.TextField("上课学生",max_length=1000,null=False,default="")
    class Meta:
        db_table ="Course"
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
