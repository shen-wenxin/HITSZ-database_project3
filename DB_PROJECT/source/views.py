from django.shortcuts import render,redirect
from .forms import UploadForm
from . import models
from django.http import HttpResponse, FileResponse
from user.models import Teacher,Student
import os
from course.models import Course

def get_user_name(request,id):
    user = Teacher.objects.filter(ID = id)
    if not user:
        user = Student.objects.filter(ID = id)
    user_name = user[0].name
    return user_name

def upload(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == 'POST':
        file_form = UploadForm(request.POST, request.FILES)
        file_form.fields['course'].choices = get_course_gender(request)
        if file_form.is_valid():
            course_id = file_form.cleaned_data['course']

            remarks = file_form.cleaned_data['remark']
            file_info = file_form.cleaned_data['file_info']

            course = models.Course.objects.filter(course_id=course_id)
            uploader_id = request.session['user_id']
            if not uploader_id:
                return redirect("/index/")
            new_file = models.FileInfo.objects.create(
                course_id=course_id,
                uploader_id=get_user_name(request,uploader_id),
                file_name = file_info.name,
                remarks = remarks,
                file_info = file_info
                )
            message = "上传成功"
            new_file.save()
            
            return render(request, 'source/upload.html', locals())
    file_form = UploadForm()
    file_form.course_list = get_course_gender(request)
    file_form.fields['course'].choices = get_course_gender(request)
    return render(request, 'source/upload.html', locals())


# 课程资源
def sourcelist(request):
    if not request.session.get('is_login', None):
        # 没有登录
        return redirect("/index/")

    # 不能再一下子打出所有课程的资源
    user_id = request.session['user_id']
    user = Teacher.objects.filter(ID = user_id)
    if not user:
        user = Student.objects.filter(ID = user_id)

    course = user[0].course.split(',')
    l_files = []
    
    for c in course:
        files = models.FileInfo.objects.filter(course_id = c)
        l_files.extend(files)
    file_list = []

    for f in l_files:
        file_info = {
            "filename":f.file_name,
            "remarks":f.remarks,
            "uploader_id": f.uploader_id,
            "file_info": f.file_info,
            "course":f.course.name,
            "download_times":f.download_times,
            "id":f.id
        }
        file_list.append(file_info)
    return render(request, 'source/list.html', locals())

def mysource_list(request):
    if not request.session.get('is_login', None):
        # 没有登录
        return redirect("/index/")

    # 不能再一下子打出所有课程的资源
    mysource_flag = True
    user_id = request.session['user_id']
    user = Teacher.objects.filter(ID = user_id)
    if not user:
        user = Student.objects.filter(ID = user_id)
    user_name = user[0].name
    
    files = models.FileInfo.objects.filter(uploader_id = user_name)

    file_list = []
    for f in files:
        file_info = {
            "filename":f.file_name,
            "remarks":f.remarks,
            "uploader_id": f.uploader_id,
            "file_info": f.file_info,
            "course":f.course.name,
            "download_times":f.download_times,
            "id":f.id
        }
        file_list.append(file_info)
    return render(request, 'source/list.html', locals())

def deletesource(request,id):
    f = models.FileInfo.objects.filter(id = id)
    file_name = f[0].file_info.name
    
    print("id")
    # 然后将其从数据库中删掉
    file_path = "media/"+file_name
    if os.path.exists(file_path):
        os.remove(file_path)
    f.delete()

    return redirect('/source/mysource_list/')

def download(request,id):
    f = models.FileInfo.objects.get(id = id)
    f.download_times = f.download_times + 1
    f.save()
    file_path = "media/"+f.file_info.name
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    return response

def get_course_gender(request):
    user_id = request.session['user_id']
    user = Teacher.objects.filter(ID = user_id)
    if not user:
        user = Student.objects.filter(ID = user_id)
    course_id = user[0].course.split(',')
    choise_list = []
    for id in course_id:
        course = Course.objects.filter(course_id = id)
        if course:
            gender = [(course[0].course_id,course[0].name)]
            choise_list = choise_list+gender

    return choise_list

            