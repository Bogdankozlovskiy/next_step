from django.urls import path
from . import views

urlpatterns = [
	path('roms/', views.RoomAPI.as_view(), name="roms"),
	path('chat/', views.Dialog.as_view(), name='chat'),
]