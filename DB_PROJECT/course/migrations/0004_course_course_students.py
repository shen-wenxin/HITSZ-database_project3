# Generated by Django 3.2 on 2021-04-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210417_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_students',
            field=models.TextField(default='', max_length=1000, verbose_name='上课学生'),
        ),
    ]