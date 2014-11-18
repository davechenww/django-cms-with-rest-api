# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from aldryn_blog.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
