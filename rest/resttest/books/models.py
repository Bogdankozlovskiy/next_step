from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
	creater = models.ForeignKey(User, on_delete=models.CASCADE)
	invited = models.ManyToManyField(User, related_name="invited_user")
	data = models.DateTimeField('Дата создания', auto_now_add=True)

	class Meta:
		verbose_name = "Комната чата"
		verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
	chat = models.ForeignKey(Room, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "сообщение"
		verbose_name_plural = "сообщения"


# Create your models here.
