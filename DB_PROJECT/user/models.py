from django.db import models



# 院系
class Departments(models.Model):

    ID = models.IntegerField('院系编号', primary_key=True,null=False)
    name = models.TextField('院系名称',max_length=20,null=False)
    name_leader = models.TextField('院长名字',max_length=10,null=False)
    class Meta:
        db_table ="Departments"
        ordering = ['ID']
        verbose_name = "院系"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 班级
class Class(models.Model):

    ID = models.IntegerField('班级编号', primary_key=True,null=False)
    name = models.TextField('班级名称',max_length=20,null=False)
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE)
    people_nums = models.IntegerField('班级人数',default=0)

    class Meta:
        db_table="class"
        ordering = ['ID']
        verbose_name = "班级"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 教师
class Teacher(models.Model):

    ID = models.IntegerField('教师编号', primary_key=True,null=False)
    name = models.TextField('教师名称',max_length=20,null=False)
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE)
    job = models.TextField('职位',max_length=10)

    class Meta:
        db_table='teacher'
        ordering = ['ID']
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 学生
class Student(models.Model):
    
    ID = models.IntegerField('学生编号', primary_key=True,null=False)
    name = models.CharField('学生姓名', max_length=20, null=False)
    ofclass = models.ForeignKey(Class,on_delete=models.CASCADE)

    class Meta:
        db_table='student'
        ordering = ['ID']
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 用户-学生
class UserTeacher(models.Model):
    user_id = models.IntegerField('用户id', primary_key=True,null=False)
    identity = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name = models.TextField('用户姓名', max_length=20, null=False,unique=True)  
    state = models.IntegerField(choices=[(0,'离线'),(1,'在线')],default=0)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField('邮箱', unique=True)
    sourse_num = models.IntegerField('已经上传的资源数',default=0)

    class Meta:
        db_table = 'UserTeacher'
        ordering = ['user_id']
        verbose_name = "用户-教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户-学生
class UserStudent(models.Model):
    user_id = models.IntegerField('用户id', primary_key=True,null=False)
    identity = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.TextField('用户姓名', max_length=20, null=False,unique=True)  
    state = models.IntegerField(choices=[(0,'离线'),(1,'在线')],default=0)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField('邮箱', unique=True)
    sourse_num = models.IntegerField('已经上传的资源数',default=0)

    class Meta:
        db_table = 'userStudent'
        ordering = ['user_id']
        verbose_name = "用户-学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



