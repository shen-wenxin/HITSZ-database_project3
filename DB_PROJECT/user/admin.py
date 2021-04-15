from django.contrib import admin
from .models import Departments, Class, Teacher, Student, UserTeacher, UserStudent

# 在admin中注册模型,使用装饰器注册的方法
@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display=('ID','name','name_leader')
    # 设置默认可编辑字段，在列表里就可以编辑
    list_editable=['name','name_leader']
    # 列表顶部
    actions_on_top=True
    # 搜索框设置，用于对于指定值的搜索
    search_fields=['name']
    

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=('ID','name','departments','people_nums')
    list_editable=['name','departments']
    actions_on_top=True
    search_fields=['name']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('ID','name','departments','job')
    list_editable=['name','departments','job']
    actions_on_top=True
    search_fields=['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('ID','name','ofclass')
    list_editable=['name','ofclass']
    actions_on_top=True
    search_fields=['name']

@admin.register(UserTeacher)
class UserTeacherAdmin(admin.ModelAdmin):
    list_display=('user_id','name','identity','state','password','email','sourse_num')
    list_editable=['password']
    actions_on_top=True
    search_fields=['name']

@admin.register(UserStudent)
class UserStudentAdmin(admin.ModelAdmin):
    list_display=('user_id','name','identity','state','password','email','sourse_num')
    list_editable=['password']
    actions_on_top=True
    search_fields=['name']
