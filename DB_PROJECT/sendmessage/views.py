from django.shortcuts import render,redirect
from .forms import MessageForm,RecallMessageForm
from .models import MessageInfo
from . import models
from user.models import UserStudent,UserTeacher






def send_message(request):
    if not request.session.get('is_login', None):
        # 没有登陆 不可以发私信
        return redirect("/index/")
        
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():  # 获取数据
            sender_id = request.session['user_id']
            if not sender_id:
                return redirect("/index/")
            reciever_id = message_form.cleaned_data['reciever_id']

            # 判断 reciever_id是否合法
            student = UserStudent.objects.filter(user_id=reciever_id)
            if student:
                reciever_name = student[0].name
            else:
                teacher = UserTeacher.objects.filter(user_id=reciever_id)
                if teacher :
                    reciever_name = teacher[0].name
                else:
                    message = '好像没有找到私信的接收者，请检查'
                    return render(request, 'message/send_message.html', locals())
            theme = message_form.cleaned_data['theme']
            text = message_form.cleaned_data['text']

            new_message = models.MessageInfo.objects.create(
                sender_id=sender_id,
                reciever_id=reciever_id,
                theme=theme,
                text=text
            )
            # new_message.save()
            print("get here")
            message = '信息已经传给 {} 啦'.format(reciever_name)
            return render(request, 'message/send_success.html', locals())
    new_message = MessageForm()
    return render(request, 'message/send_message.html', locals())


def recieve_message(request):
    # 接收信息
    if not request.session.get('is_login', None):
        # 没有登陆 不可以查看私信
        return redirect("/index/")
    # 在信息数据库中将所有接收者是本人的信息读出来
    msgs = models.MessageInfo.objects.filter(reciever_id=request.session['user_id'],reciever_delete=False)
    print(msgs)
    
    msgs_list = []
    for msg in msgs:
        student = UserStudent.objects.filter(user_id=msg.sender_id)
        if student:
            sender_name = student[0].name
        else:
            teacher = UserTeacher.objects.filter(user_id=msg.sender_id)
            sender_name = teacher[0].name
        if msg.read_flag :
            read = "已读"
        else:
            read = "未读"
        msg_info = {
            "send_time":msg.send_time,
            "sender":sender_name,
            "theme": msg.theme,
            "text":msg.text[0:150],
            "read":read,
            "id":msg.id
        }
        msgs_list.append(msg_info)
    print(msgs_list)
    return render(request, 'message/recieve_message.html', locals())


def message_info(request,id):
    msgs = models.MessageInfo.objects.filter(id=id,reciever_delete=False)
    msg = msgs[0]
    msg.read_flag = True
    msg.save()
    student = UserStudent.objects.filter(user_id=msg.sender_id)
    if student:
        sender_name = student[0].name
        student[0].read_flag=True
        student[0].save()
    else:
        teacher = UserTeacher.objects.filter(user_id=msg.sender_id)
        sender_name = teacher[0].name
        teacher[0].read_flag = True
        teacher[0].save()
    reciever_id =request.session['user_id']
    student_re = UserStudent.objects.filter(user_id=reciever_id)
    if student_re:
        reciever_name = student_re[0].name
    else:
        teacher_re = UserTeacher.objects.filter(user_id=reciever_id)
        reciever_name = teacher_re[0].name
    # # 从系统里加载历史对话信息
    # old_msgs_list = []
    
    # old_msgs = models.MessageInfo.objects.filter(sender_id=msg.sender_id, reciever_id = reciever_id)
    # for om in old_msgs:
    #     om_info = {
    #         "send_time":om.send_time,
    #         "sender_id":msg.sender_id,
    #         "theme":om.theme,
    #         "text":om.text
    #     }
    #     old_msgs_list.append(om_info)
    # if msg.sender_id != reciever_id:
    #     old_msgs = models.MessageInfo.objects.filter(sender_id=reciever_id, reciever_id = msg.sender_id)
    #     for om in old_msgs:
    #         om_info = {
    #             "send_time":om.send_time,
    #             "sender_id":reciever_id,
    #             "theme":om.theme,
    #             "text":om.text
    #         }
    #         old_msgs_list.append(om_info)
    # sorted_old_msgs=sorted(old_msgs_list, key= lambda st : st['send_time'])
    # print(sorted_old_msgs)

    msg_info = {
            "sender_id":msg.sender_id,
            "send_time":msg.send_time,
            "sender":sender_name,
            "reciever":reciever_name,
            "theme": msg.theme,
            "text":msg.text,
            "reciever_id":reciever_id,
            "id":id
    }
    return render(request, 'message/message_info.html', locals())


def delete_message(request,id):
    obj = models.MessageInfo.objects.filter(id = id).update(reciever_delete = True)
    obj = models.MessageInfo.objects.filter(reciever_delete = True,sender_delete = True).delete()

    
    return redirect('/recieve_message/')

def delete_message_send(request,id):
    obj = models.MessageInfo.objects.filter(id = id).update(sender_delete = True)
    obj = models.MessageInfo.objects.filter(reciever_delete = True,sender_delete = True).delete()
    print("get here")
    return redirect('/sended_message/')


def sended_message(request):
    # 接收信息
    if not request.session.get('is_login', None):
        # 没有登陆 不可以查看私信
        return redirect("/index/")
    # 在信息数据库中将所有接收者是本人的信息读出来
    msgs = models.MessageInfo.objects.filter(sender_id=request.session['user_id'],sender_delete=False)
    msgs_list = []
    for msg in msgs:
        student = UserStudent.objects.filter(user_id=msg.reciever_id)
        if student:
            reciever_name = student[0].name
        else:
            teacher = UserTeacher.objects.filter(user_id=msg.reciever_id)
            reciever_name = teacher[0].name
        msg_info = {
            "send_time":msg.send_time,
            "reciever":reciever_name,
            "theme": msg.theme,
            "text":msg.text[0:150],
            "id":msg.id
        }
        msgs_list.append(msg_info)
    print(msgs_list)
    return render(request, 'message/sended_message.html', locals())

