# 课程资源管理系统

## 1 实验环境

1、主要操作系统：Windows 10

2、主要软件版本：Visual Studio Code

3、利用django进行web框架搭建

4、前端利用bootstrap进行简单设计

## 2 系统功能

### 2.1 用户管理

​	支持用户的**注册、登录、退出**。

​	用户未登录时，无法获取信息，需要登录之后才能进行信息获取。未登录界面如下：![image-20210421174256911](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421174256911.png)

​	

#### 1）用户注册

注册界面如图所示：

![image-20210421175210360](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421175210360.png)

​	其中，需要输入学生号来进行用户注册。在数据库预存学生/老师的个人信息，预存信息如图：

![image-20210421175430287](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421175430287.png)

​	如果在用户注册的时候输入错误的学生编号id，会有报错提示：

<img src="C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421175502511.png" alt="image-20210421175502511" style="zoom: 80%;" />

​	注册成功后即可登录。

#### 2) 用户登录

​	登录界面如图所示：

![image-20210421175759591](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421175759591.png)

​	密码不正确时会有提示：

<img src="C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421175849847.png" alt="image-20210421175849847" style="zoom:50%;" />

​	用户不存在时会有提示：

<img src="C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421175919254.png" alt="image-20210421175919254" style="zoom:50%;" />

​	登录成功：

![image-20210421223747902](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421223747902.png)

#### 3) 教师/学生信息管理

​	点击"教师/学生信息"可看到系统内预存的学生、教师信息。

​	该信息为系统管理员预存，而不是新注册的用户信息，无法更改。

![image-20210421225728883](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421225728883.png)

### 2.2 课程管理

#### 1) 课程展示

作为老师，可以在"我的课程"界面看到自己的课程，并且可以选择修改课程、新建课程、退出课程。

![image-20210421231700678](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421231700678.png)

#### 2)新建课程

新建课程的界面如图所示：

![image-20210421231907368](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421231907368.png)

新建成功后自动返回显示课程列表的界面，如图，可发现课程列表已更新：

![image-20210421232007654](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421232007654.png)

#### 3) 修改课程

在课程列表点击课程修改按钮之后，可以浏览课程的详细信息：

<img src="C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421232200112.png" alt="image-20210421232200112" style="zoom: 50%;" />

继续点击"课程修改"可继续进行课程的修改，修改界面如图：

<img src="C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421232317446.png" alt="image-20210421232317446" style="zoom:50%;" />

修改之后结果如图所示：

<img src="C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421232346742.png" alt="image-20210421232346742" style="zoom:67%;" />

#### 4)退出课程

为防止老师误删课程，只有当该门课授课老师大于一人时，教师可选择退出该门课。

当点击"course003"的退出之后，course003将不再是王轩老师的课程。

如图：

![image-20210421232618941](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421232618941.png)

#### 5)课程资源下载

在课程列表中，可选择下载某门课程的资源。

如点击"course002"的资源下载：

![image-20210421233433567](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421233433567.png)

可看到该门课程中有一份资源，点击"点我"即可下载。

### 2.3 资源管理

#### 1)资源上传

点击上传资源可进行资源的上传。资源上传界面如图：

![image-20210421233711235](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421233711235.png)

上传成功后在 资源列表 和 我的资源 中均可看到

![image-20210421234347285](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421234347285.png)

![image-20210421234416025](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421234416025.png)

#### 2) 资源删除

在 我的上传 界面，点击删除按钮，可删除之前上传过的资源。

### 2.4 私信管理

在私信列表页面可以看到收到的所有私信。

![image-20210421235455357](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210421235455357.png)

#### 2)查看私信

点击 "点我看看" 可以看到私信详情，可以看到历史记录

![image-20210422003115178](C:\Users\shen_\AppData\Roaming\Typora\typora-user-images\image-20210422003115178.png)

#### 3) 删除私信

点击删除，可以删除私信。


