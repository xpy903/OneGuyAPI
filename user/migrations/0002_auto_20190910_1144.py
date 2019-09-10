# Generated by Django 2.0.1 on 2019-09-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='img1',
            field=models.CharField(default=1, max_length=100, verbose_name='头像'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='status',
            field=models.IntegerField(choices=[(0, '未激活'), (1, '正常'), (2, '注销')], default=0, verbose_name='状态'),
        ),
    ]