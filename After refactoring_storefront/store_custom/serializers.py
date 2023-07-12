from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','password','email','first_name', 'last_name']

class UserSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserSerializer):

        fields = ['id','username','email','first_name', 'last_name']