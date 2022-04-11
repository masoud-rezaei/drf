from rest_framework import serializers 
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','title','author','body','created_ad',)
        model=Post