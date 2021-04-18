# Generated by Django 3.2 on 2021-04-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('course_id', models.TextField(primary_key=True, serialize=False, verbose_name='课程编号')),
                ('name', models.TextField(max_length=200, verbose_name='课程名字')),
                ('course_teachers', models.CharField(max_length=200, verbose_name='任课教师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
                'db_table': 'Course',
            },
        ),
    ]
