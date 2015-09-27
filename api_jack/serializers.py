from django.contrib.auth.models import User
from .models import UserInfo
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class UserInfoSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta(object):
        model = UserInfo        
