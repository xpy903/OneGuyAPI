#!/usr/bin/python3
# coding: utf-8

from django.forms.widgets import TextInput


class SendEmailButton(TextInput):
    template_name = 'send_email_widget.html'

    # render_value 是否渲染现有的值
    def __init__(self, attrs=None, render_value=True):
        super().__init__(attrs)
        self.render_value = render_value

    def get_context(self, name, value, attrs):
        if not self.render_value:
            value = None
        return super().get_context(name, value, attrs)



