from django.shortcuts import render,redirect
from .forms import UserForm,RegisterForm
from . import models
from sendmessage.models import MessageInfo
def index(request):
    # 主页
    
    return render(request, 'user/index.html') 

def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():  # 获取数据
            user_id = register_form.cleaned_data['user_id']
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            identity = register_form.cleaned_data['identity']
            
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'user/register.html', locals())
            else:
                same_id_stu = models.UserStudent.objects.filter(user_id=user_id)
                same_id_tea = models.UserTeacher.objects.filter(user_id=user_id)
                if same_id_stu or same_id_tea:  # 用户名唯一
                    message = '用户已经存在'
                    return render(request, 'user/register.html', locals())

                same_name_user_student = models.UserStudent.objects.filter(name=username)
                same_name_user_teacher = models.UserTeacher.objects.filter(name=username)
                if same_name_user_student or same_name_user_teacher:  # 用户名唯一
                    message = '昵称已经被抢啦'
                    return render(request, 'user/register.html', locals())
                same_email_user_student = models.UserStudent.objects.filter(email=email)
                same_email_user_teacher = models.UserTeacher.objects.filter(email=email)
                if same_email_user_student or same_email_user_teacher:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'user/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                
                if identity == "Teacher":
                    try:
                        identity = models.Teacher.objects.get(ID=user_id)
                        new_user = models.UserTeacher.objects.create(user_id = user_id,identity_id=user_id)
                        new_user.name = username
                        new_user.password = password1
                        new_user.email = email
                        new_user.identity = identity
                        new_user.save()
                        return redirect('/login/')  # 自动跳转到登录页面

                    except:
                        message = '你是谁啊，找不到你这个小坏蛋啊，你确定这是对的id嘛'
                        return render(request, 'user/register.html', locals())

                elif identity == "Student":
                    try:
                        identity = models.Student.objects.get(ID=user_id)
                        new_user = models.UserStudent.objects.create(user_id = user_id,identity_id=user_id)
                        new_user.user_id = user_id
                        new_user.name = username
                        new_user.password = password1
                        new_user.email = email
                        new_user.identity = identity
                        print("[DEBUG][POST][SAVE2DB][ID]:{}".format(new_user.user_id))
                        print("[DEBUG][POST][SAVE2DB][new_user]:{}".format(new_user))
                        new_user.save()
                        return redirect('/login/')  # 自动跳转到登录页面

                    except:
                        message = '你是谁啊，找不到你这个小坏蛋啊，你确定这是对的id嘛'
                        return render(request, 'user/register.html', locals())
    register_form = RegisterForm()
    return render(request, 'user/register.html', locals())
    
def get_message_num(request,id):
    msgs = models.MessageInfo.objects.filter(reciever_id=id,reciever_delete=False,read_flag = Flase)
    nums = msgs.count()
    print("nums = {}".format(nums))
    return nums

def login(request):
    if request.session.get('is_login',None):
        print("[DEBUG][POST][STATE]:已经登陆")
        return redirect("/index/")

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # identy 表示
            print("[DEBUG][POST][LOGIN][username]:{}".format(username))
            print("[DEBUG][POST][LOGIN][password]:{}".format(password))

            try:
                print("[DEBUG][POST][STATE]:查询用户-学生数据库")
                user_student = models.UserStudent.objects.get(name=username)
                if user_student.password == password:
                    print("[DEBUG][POST][USERNAME]:{}".format(user_student.name))
                    print("[DEBUG][POST][STATE]:登录成功，身份：学生")
                    print("[DEBUG][POST][USERID]:{}".format(user_student.user_id))
                    user_student.state = 1
                    user_student.save()
                    request.session['is_login']=True
                    request.session['user_id']=user_student.user_id
                    request.session['user_name']=user_student.name
                    # request.session['message_num'] = get_message_num(request,user_student.user_id)
                    return redirect("/index/")
                else:
                    print("[DEBUG][POST][STATE]:密码不正确")
                    message="密码不正确"

            except:
                print("[DEBUG][POST][STATE]:查询用户-教师数据库")
                try:
                    user_teacher = models.UserTeacher.objects.get(name=username)
                    print("user_teacher.password={}".format(user_teacher.password))
                    print("password:{}".format(password))
                    if user_teacher.password == password:
                        user_teacher.state = 1
                        user_teacher.save()
                        print("[DEBUG][POST][STATE]:登录成功")
                        request.session['is_login']=True
                        request.session['user_id']=user_teacher.user_id
                        request.session['user_name']=user_teacher.name
                        # request.session['message_num'] = get_message_num(request,user_teacher.user_id)
                        return redirect('/index/')
                    else:
                        print("[DEBUG][POST][STATE]:密码不正确")
                        message="密码不正确"
                except:
                    print("[DEBUG][POST][STATE]:用户不存在")
                    message="用户不存在"
        return render(request, 'user/login.html', locals())
    login_form = UserForm()
    return render(request, 'user/login.html', locals())
    



def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    user_id = request.session['user_id']
    print("[DEBUG][REQUEST][退出]]")
    print("[DEBUG][REQUEST][USER_ID]:{}".format(user_id))
    try:
        user_teacher = models.UserTeacher.objects.get(user_id=user_id)
        print("[DEBUG][REQUEST][退出]]：退出用户身份：老师")
        user_teacher.state = 0  # 更新离线状态
        user_teacher.save()
    except:
        try:
            print("get here")
            user_student = models.UserStudent.objects.get(user_id=user_id)
            print("[DEBUG][REQUEST][退出]]：退出用户身份：学生")
            user_student.state = 0
            user_student.save()
        except:
            print("[DEBUG][request][STATE]:退出错误，无法更新数据库中用户状态")

    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

def user_info_teacher(request):
    if not request.session.get('is_login', None):
    # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    # 获取系统里所有的老师
    teacher_user = models.Teacher.objects.filter()
    return render(request, 'user/user_info_teacher.html', locals())

def user_info_student(request):
    if not request.session.get('is_login', None):
    # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    # 获取系统里所有的老师
    teacher_user = models.Student.objects.filter()
    return render(request, 'user/user_info_student.html', locals())

