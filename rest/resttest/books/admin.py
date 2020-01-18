from django.contrib import admin
from .models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
	list_display = ('creater', 'invited_user', 'data')

	def invited_user(self, obj):
		return "\n".join([user.username for user in obj.invited.all()])

admin.site.register(Room, RoomAdmin)


class ChatAdmin(admin.ModelAdmin):
	list_display = ('chat', 'user', 'text', 'date')

admin.site.register(Chat, ChatAdmin)
