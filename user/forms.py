#!/usr/bin/python3
# coding: utf-8
import re

from django import forms
from django.core.exceptions import ValidationError

from .models import AppUser
from .widgets import SendEmailButton

class AppUserForm(forms.ModelForm):
    name = forms.CharField(min_length=8,
                           max_length=20,
                           required=True,
                           error_messages={
                               'required': '账户不能为空',
                               'max_length': '账户不能超过20个字符',
                               'min_length': '账户不能少于8个字符'
                           })

    # 自定义验证规则： 必须包含大写、小写和数字等字符
    auth_key = forms.CharField(widget=forms.PasswordInput,
                               label='口令',
                               min_length=6,
                               error_messages={
                                   'required': '口令不能为空',
                                   'min_length': ' 口令不少于6位'
                               })

    phone = forms.CharField(max_length=11,
                            min_length=11,
                            required=False, label='手机号')

    # 通过widget属性指定自定义widget部件
    email = forms.CharField(required=False,
                            widget=SendEmailButton, label='邮箱')

    class Meta:
        model = AppUser
        fields = ('name', 'auth_key', 'phone', 'email')
        error_messages = {
            'email': {
                'required': '邮箱不能为空'
            }
        }


    def is_valid(self):
        print('--is_valid---')
        return super().is_valid()


    def clean_auth_key(self):
        # 以上验证都通过了
        # 自定义验证规则： 必须包含大写、小写和数字等字符
        auth_key = self.cleaned_data.get('auth_key')
        if all((
            re.search(r'\d+', auth_key),
            re.search(r'[a-z]+', auth_key),
            re.search(r'[A-Z]+',auth_key)
        )):
            print('-----clean_auth_key-----')
            return auth_key

        raise ValidationError('口令必须包含大写、小写和数字等字符')
