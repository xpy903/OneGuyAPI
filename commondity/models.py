from django.db import models

from common import YGBaseModel


# Create your models here.
class Category(YGBaseModel):
    code = models.CharField(max_length=20,
                            verbose_name='编码')
    name = models.CharField(max_length=20,
                            verbose_name='名称')

    grade = models.IntegerField(default=1,
                                verbose_name='等级')

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name='父类',
                               null=True,
                               blank=True)

    picture_url = models.CharField(max_length=200,
                                   verbose_name='图片路径',
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = verbose_name_plural = '分类表'
