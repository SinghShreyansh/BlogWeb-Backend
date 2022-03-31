from dataclasses import field, fields
from rest_framework import serializers
from BlogApp.models import Blogs

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields=('id','title','description','body','author','category')
