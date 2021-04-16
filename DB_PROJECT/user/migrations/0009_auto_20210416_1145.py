# Generated by Django 3.2 on 2021-04-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210416_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='ID',
            field=models.TextField(max_length=20, primary_key=True, serialize=False, verbose_name='班级编号'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='ID',
            field=models.TextField(max_length=20, primary_key=True, serialize=False, verbose_name='院系编号'),
        ),
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.TextField(max_length=20, primary_key=True, serialize=False, verbose_name='学生编号'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='ID',
            field=models.TextField(max_length=20, primary_key=True, serialize=False, verbose_name='教师编号'),
        ),
        migrations.AlterField(
            model_name='userstudent',
            name='user_id',
            field=models.TextField(max_length=20, primary_key=True, serialize=False, verbose_name='用户id'),
        ),
        migrations.AlterField(
            model_name='userteacher',
            name='user_id',
            field=models.TextField(max_length=20, primary_key=True, serialize=False, verbose_name='用户id'),
        ),
    ]
