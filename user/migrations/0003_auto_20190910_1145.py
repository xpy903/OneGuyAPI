# Generated by Django 2.0.1 on 2019-09-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190910_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='img1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='头像'),
        ),
    ]