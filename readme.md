# 课程资源管理系统

## 1 实验环境

1、利用django进行web框架搭建

2、前端利用bootstrap进行简单设计

## 2 系统功能

### 2.1 用户管理

​	支持用户的**注册、登录、退出**。

### 2.2 课程管理

​	支持课程的**新建、修改、退出**

### 2.3 资源管理

​	支持资源的**上传、下载、删除**

## 3 快速开始

0、django版本：3.2.0

1、进入``DB_PROJECT``目录底下

2、命令行输入：

``python manage.py runserver``

## 4 API

#### 4.1 项目结构

``DB_PROJECT``的文件夹格式：

```
DB_PROJECT
	-course
	-sendmessage
	-source
	-user
	-statics
	-tempates
```

​	该项目分为四个app部分。``course/sendmessage/user/source``

​	以``course``为例，其内部结构为：

```
course
	-admin.pu
	-apps.py
	-forms.py	表单
	-models.py	数据处理模块
	-urls.py	路由地址注册
	-views.py	视图函数
```

​	其中``views.py``为主要实现部分。

#### 4.2 course.views

##### mycourse

​	作用：根据``request.session``获得目前登录用户的id号，从数据库中读取改用户的所有课程信息，存到``course_info_list``中，用以在``mycourse.html``中展示。

##### course_source

·id -(入参)想要获取资源的课程的id号

​	作用：根据``id``,从数据库中获取课程号为id号的该课程的所有资源信息，存到``file_list``中，用以在``course_source.html``中展示。

##### add_course

​	作用：新建课程。

##### course_detels

·id -(入参)课程的id号

​	作用：展示课程信息。

##### course_modify

·id -(入参)课程的id号

​	作用：修改课程。

##### quit_course

·id -(入参)课程的id号

​	作用：退出课程。

#### 4.3 sendmessage.views

##### get_user_name

·id -(入参)用户的id号

​	作用：返回用户名。

##### send_message

​	作用：发送信息。

##### recieve_message

​	作用：以表格的形式展示收到的信息。

##### message_info

·id -(入参)信息id号

​	作用：展示``message``的详细内容。

##### delete_message

·id -(入参)信息id号

​	作用：删除收到的信息。

##### delete_message_send

·id -(入参)信息id号

​	作用：删除已发送的信息。

##### sended_message

​	作用：以表格的形式展示已发送的信息。

#### 4.4 source.views

##### upload

​	作用：上传资源。

##### sourcelist

​	作用：以表格的形式展示资源。

##### mysource_list

​	作用：以表格的形式展示该用户上传的资源。

##### deletesource

·id -(入参)信息id号

​	作用：删除资源。

##### download

·id -(入参)信息id号

​	作用：下载资源。

#### 4.5 user.views

##### index

​	作用：主页。

##### register

​	作用：注册。

##### login

​	作用：登录。

##### logout

​	作用：登出。