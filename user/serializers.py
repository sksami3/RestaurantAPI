from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import AppUser

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class AppUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'groups')

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        password = validated_data.pop('password', None)
        user = AppUser.objects.create_user(**validated_data)

        for group_data in groups_data:
            group, _ = Group.objects.get_or_create(**group_data)
            user.groups.add(group)

        if password:
            user.set_password(password)
            user.save()

        return user