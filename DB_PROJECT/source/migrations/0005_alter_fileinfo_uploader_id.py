# Generated by Django 3.2 on 2021-04-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0004_alter_fileinfo_uploader_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinfo',
            name='uploader_id',
            field=models.TextField(max_length=20, verbose_name='上传者编号'),
        ),
    ]