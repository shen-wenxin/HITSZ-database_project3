from django.shortcuts import render,redirect
from user.models import UserTeacher,UserStudent,Student,Teacher
from .models import Course
from source.models import FileInfo
from .forms import CourseForm,CourseModifyForm
def mycourse(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    # 查询

    # 从数据库中得到我的课程的编号
    identity = UserStudent.objects.filter(user_id = request.session['user_id'])
    
    if not identity:
        print("get here")
        message_teacher = "新建课程"
        identity = UserTeacher.objects.filter(user_id = request.session['user_id'])
    course_list = identity[0].identity.course.split(',')


    """
        开始从数据库中将课程的信息取出来

    """
    course_info_list = []
    for cid in course_list:
        course = Course.objects.filter(course_id = cid)
        if not course:
            print(cid)
            continue
        teacher_num = len(course[0].course_teachers.split(','))
        course_info = {
            "id":cid,
            "name":course[0].name,
            "teacher":course[0].course_teachers,
            "teacher_num":teacher_num
        }
        course_info_list.append(course_info)


    return render(request, 'course/mycourse.html', locals())

def course_source(request,id):
    if not request.session.get('is_login', None):
        # 没有登录
        return redirect("/index/")

    # 在数据库中查找该课程的所有资源
    source_list = FileInfo.objects.filter(course_id = id)
    print(source_list)
    file_list = []

    
    for f in source_list:
        uploader = UserStudent.objects.filter(user_id = f.uploader_id)

        if not uploader:
            uploader = UserTeacher.objects.filter(user_id = f.uploader_id)
        file_info = {
            "uploade_time":f.upload_time,
            "filename":f.file_name,
            "remarks":f.remarks,
            "uploader_id": uploader[0].name,
            "file_info": f.file_info,
            "course":f.course.name,
            "download_times":f.download_times,
            "id":f.id,
            "file":f.file_info.name.split('/')[-1]
        }
        print(f.upload_time)
        course_name = f.course.name
        print(type(f.id))
        file_list.append(file_info)
    if len(file_list) == 0:
        message = "这里啥也没有……"


    
    return render(request, 'course/course_source.html', locals())

def add_course(request):
    if not request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        course_form = CourseForm(request.POST)
        if course_form.is_valid():  # 获取数据
            course_id = course_form.cleaned_data['course_id']
            name = course_form.cleaned_data['name']
            teacher = course_form.cleaned_data['teacher']
            student = course_form.cleaned_data['student']

            # 检查课程编号是否合理
            c = Course.objects.filter(course_id = course_id)
            if c:
                message = "课程编号已和<{}>重复".format(c[0].name)
                return render(request, 'course/course_add.html', locals())

            # 查看老师是否合理
            teacher_list = teacher.split(',')
            for n in teacher_list:
                teach = Teacher.objects.filter(name = n)
                if teach:
                    print(teach[0].name)
                if not teach:
                    message = "老师名单有误，请检查"
                    return render(request, 'course/course_add.html', locals())

            # 查看学生是否合理
            student_list = student.split(',')
            for s in student_list:
                stu = Student.objects.filter(name = s)
                if stu:
                    print(stu[0].name)
                if not stu:
                    message = "学生名单有误，请检查"
                    return render(request, 'course/course_add.html', locals())

            # 更新老师状态
            for n in teacher_list:
                teach = Teacher.objects.filter(name = n)[0]
                teach.course = teach.course + ",{}".format(course_id)
                teach.save()

            # 更新学生状态
            for n in student_list:
                stu = Student.objects.filter(name = n)[0]
                stu.course = stu.course + ",{}".format(course_id)
                stu.save()

            #将该课程存到数据库中

            new_course = Course.objects.create(course_id = course_id,name = name, course_teachers = teacher,course_students = student)
            new_course.save()

        return redirect('/course/mycourse') 
    course_form = CourseForm()
    return render(request, 'course/course_add.html', locals())

def course_deteils(request,id):
    if not request.session.get('is_login', None):
    # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    print("------")
    course_id = id
    # 先从课程表中将课程信息读出来

    course= Course.objects.filter(course_id = id)
    course_name = course[0].name
    course_teacher = course[0].course_teachers.split(',')
    course_student = course[0].course_students.split(',')
    return render(request, 'course/course_deteils.html', locals())

def course_modify(request,id):
    if not request.session.get('is_login', None):
    # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    course_id = id
    print("get here0")
    course= Course.objects.filter(course_id = id)
    if request.method == "POST":
        courseform = CourseModifyForm(request.POST)
        if courseform.is_valid():
            course_teacher_add = courseform.cleaned_data['teacher']
            course_student_add = courseform.cleaned_data['student']
            name = courseform.cleaned_data['name']
            print("course_teacher_add:{}".format(course_teacher_add))
            print("course_student_add:{}".format(course_student_add))

            if name != "不修改":
                # 修改其名字
                course.update(name = name)
            
            if course_teacher_add != "不修改":
                # 查看老师是否合理
                teacher_list = course_teacher_add.split(',')
                for n in teacher_list:
                    teach = Teacher.objects.filter(name = n)
        
                    if not teach:
                        message = "老师名单有误，请检查"
                        return render(request, 'course/course_modify.html', locals())

                 # 检查这门课是否已经包含该老师
                course_teacher = course[0].course_teachers.split(',')
                add_teacher_list = course_teacher_add.split(',') 
                for at in course_teacher:
                    if at in add_teacher_list:
                        message = "{}老师已经在这门课里拉".format(at)
                        return render(request, 'course/course_modify.html', locals())

                # 更新老师状态
                for n in add_teacher_list:
                    teach = Teacher.objects.filter(name = n)[0]
                    teach.course = teach.course + ",{}".format(course_id)
                    teach.save()

                #将该课程存到数据库中
                for c in add_teacher_list:
                    print("c:{}".format(c))
                    course_teachers = course[0].course_teachers
                    course_teachers = course_teachers + ",{}".format(c)
                    course.update(course_teachers = course_teachers)

            if course_student_add != "不修改":
                # 查看学生是否合理
                student_list = course_student_add.split(',')
                for s in student_list:
                    stu = Student.objects.filter(name = s)
                
                    if not stu:
                        message = "学生名单有误，请检查"
                        return render(request, 'course/course_modify.html', locals())
                # 检查这门课是否已经包含学生
                course_student = course[0].course_students.split(',')
                add_student_list = course_student_add.split(',') 
                for at in course_student:
                    if at in add_student_list:
                        message = "{}学生已经在这门课里拉".format(at)
                        return render(request, 'course/course_modify.html', locals())
                # 更新学生状态
                for n in add_student_list:
                    stu = Student.objects.filter(name = n)[0]
                    stu.course = stu.course + ",{}".format(course_id)
                    stu.save()
                for t in add_student_list:
                    course_students = course[0].course_students + ",{}".format(t)
                    course.update(course_students = course_students)

            return redirect("/course/mycourse/")

    courseform = CourseModifyForm()
    return render(request, 'course/course_modify.html', locals())

def quit_course(request, id):
    if not request.session.get('is_login', None):
        return redirect("/index/")

    '''
    退出一门课的规则是：只有老师允许退出该课程，学生不允许退出该课程
    '''

    user_id = request.session['user_id']
    course_id = id

    # 更新course数据库
    course = Course.objects.filter(course_id = course_id)[0]

    user = Teacher.objects.filter(ID = user_id)[0]

    course_teacher = course.course_teachers.split(',')
    course_teacher.remove(user.name)

    print("course_teacher{}".format(course_teacher))

    if len(course_teacher) == 0:
        print("get message")
        message = "您退出后将没人教学<{}>课程，请直接删除该课程".format(course.name)
        return redirect('/course/mycourse/')
    
    course_teacher_str = course_teacher[0]
    for i in range(1,len(course_teacher)):
        course_teacher_str = course_teacher_str + ",{}".format(course_teacher[i])

    Course.objects.filter(course_id = course_id).update(course_teachers =course_teacher_str)
    print(course_teacher_str)

    # 更新老师名单

    user_course_id = user.course.split(',')
    print("user_course_id{}".format(user_course_id))
    user_course_id.remove(course_id)
    print("user_course_id:{}".format(user_course_id))
    course_user_str = ""
    for i in user_course_id:
        course_user_str = course_user_str + ",{}".format(i)

    print("course_user_str:{}".format(course_user_str))
    Teacher.objects.filter(ID = user_id).update(course = course_user_str)
    return redirect('/course/mycourse')

