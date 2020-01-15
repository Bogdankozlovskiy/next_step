from django.urls import path
from . import views

urlpatterns = [
	path('hello/create/<int:idd>/', views.Create.as_view(), name='create'),
	path('hello/create/', views.Create.as_view(), name='create'),
	path('hello/', views.hello, name='main'),
	path('world/', views.world),
]