from django.contrib.auth.models import User

from mezzanine.blog.models import BlogPost
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']
        filtering = {
            'username': ALL,
        }


class BlogPostResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = BlogPost.objects.all()
        resource_name = 'blogpost'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'publish_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
