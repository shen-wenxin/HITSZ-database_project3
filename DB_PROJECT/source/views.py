from django.shortcuts import render,redirect
from .forms import UploadForm
from . import models
from django.http import HttpResponse, FileResponse

def upload(request):
    if not request.session.get('is_login', None):
        print("get here0")
        return redirect("/index/")
    if request.method == 'POST':
        file_form = UploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            course_id = file_form.cleaned_data['course_id']
            remarks = file_form.cleaned_data['remark']
            file_info = file_form.cleaned_data['file_info']

            course = models.CourseInfo.objects.filter(course_id=course_id)
            if course:
                uploader_id = request.session['user_id']
                if not uploader_id:
                    return redirect("/index/")
                new_file = models.FileInfo.objects.create(
                    course_id=course_id,
                    uploader_id=uploader_id,
                    file_name = file_info.name,
                    remarks = remarks,
                    file_info = file_info
                    )
                message = "上传成功"
                new_file.save()
                
                return render(request, 'source/upload.html', locals())
            else:
                # 找不到这门课
                message = "有点东西不对…检查一下课程id…"
                return render(request, 'source/upload.html', locals())

    file_form = UploadForm()
    return render(request, 'source/upload.html', locals())


# 课程资源
def sourcelist(request):
    if not request.session.get('is_login', None):
        # 没有登录
        return redirect("/index/")

    files = models.FileInfo.objects.all()
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
        print("id:")
        print(type(f.id))
        file_list.append(file_info)
    return render(request, 'source/list.html', locals())


def download(request,id):
    f = models.FileInfo.objects.get(id = id)
    f.download_times = f.download_times + 1
    f.save()
    file_path = "media/"+f.file_info.name
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    return response


            