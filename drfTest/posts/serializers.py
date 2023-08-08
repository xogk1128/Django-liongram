from rest_framework import serializers

from .models import Post

class PostBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['image','content',]
        fields = '__all__'

