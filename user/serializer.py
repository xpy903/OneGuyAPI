#!/usr/bin/python3
# coding: utf-8

from rest_framework import serializers

from .models import AppUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'name', 'phone', 'email', 'img1')
