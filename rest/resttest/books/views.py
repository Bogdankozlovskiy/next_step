from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Room, Chat
from .serializer import RoomSerializers, ChatSerialiser, ChatPostSerialiser
# you shoud install it  pip install markdown==3.0

class RoomAPI(APIView):
	permission_classes = [permissions.AllowAny]

	def get(self, request):
		rooms = Room.objects.all()
		ser = RoomSerializers(rooms, many=True)
		return Response(ser.data)


class Dialog(APIView):
	permission_classes = [permissions.AllowAny]
	def get(self, request):
		room = request.GET.get('room')#?room=1
		chat = Chat.objects.filter(chat=room)
		ser = ChatSerialiser(chat, many=True)
		return Response({"data":ser.data})

	def post(self, request):
		ser = ChatPostSerialiser(data = request.data)
		print(request.data)   
		if ser.is_valid():     #{'chat': 1, 'text': 'rrr'}
			ser.save(user=request.user)
			return Response({'status':'done'})
		return Response({'status':'error'})


# Create your views here.
