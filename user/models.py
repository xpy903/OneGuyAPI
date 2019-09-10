from django.db import models
from common import YGBaseModel


class AppUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~models.Q(status=2))

# Create your models here.
class AppUser(YGBaseModel):
    name = models.CharField(max_length=50,
                            verbose_name='用户名')
    auth_key = models.CharField(max_length=100,
                                verbose_name='口令')
    phone = models.CharField(max_length=11,
                             verbose_name='手机号')
    email = models.CharField(max_length=50,
                             verbose_name='邮件')

    create_time = models.DateField(verbose_name='注册时间',
                                   auto_now_add=True)

    status = models.IntegerField(verbose_name='状态',
                                 default=0,
                                 choices=((0, '未激活'),
                                          (1, '正常'),
                                          (2, '注销')))

    img1 = models.CharField(max_length=100,
                            verbose_name='头像', null=True,
                            blank=True)

    objects = AppUserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_app_user'
        verbose_name = verbose_name_plural = '客户信息'