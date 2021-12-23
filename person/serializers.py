from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'first_name', 'last_name','middle_name',
                  'age', 'duty', 'salary', 'photo', 'department')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])

        for key, value in validated_data.items():
            if not 'password' in key:
                setattr(user, key, value)
        
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()

        return user


class DeleteUserSerializer(serializers.Serializer):

    username = serializers.CharField(write_only=True, required=True)

    def validate_username(self, username):
        if User.objects.get_or_create(username=username)[1]:
            raise serializers.ValidationError({"username": "User with it name does not exist."})

        return username


class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'middle_name',
                'duty',
                'age',
                'salary',
                'photo',
                'department_name'
        ]