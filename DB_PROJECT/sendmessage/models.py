from django.db import models
from django.utils import timezone


# 私信表
class MessageInfo(models.Model):
    send_time = models.DateTimeField('发送时间',default=timezone.now)
    sender_id = models.TextField('发送者编号', max_length=20, db_index = True)
    reciever_id = models.TextField('接收者编号', max_length=20, db_index = True)
    theme = models.TextField('主题', max_length=50)
    text = models.TextField('私信内容', max_length=1000)
    read_flag = models.BooleanField('新信息？',default=False)
    sender_delete = models.BooleanField('发送者有将他删除吗',default=False)
    reciever_delete = models.BooleanField('接收者有将他删除吗',default=False)
    class Meta:
        db_table ="MessageInfo"
        verbose_name = "私信"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.theme
