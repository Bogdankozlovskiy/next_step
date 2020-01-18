from rest_framework import serializers
from .models import Room, Chat
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User 
		fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
	creater = UserSerializer()
	invited = UserSerializer(many=True)
	class Meta:
		model = Room
		fields = ('creater', 'invited', 'data')


class ChatSerialiser(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Chat
		fields = ('chat', "user", "text", "date")


class ChatPostSerialiser(serializers.ModelSerializer):
	class Meta:
		model = Chat
		fields = ("text", "chat")