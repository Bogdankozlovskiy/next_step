from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import MyVideo


@api_view(['GET'])
def hello(request):
	response = {}
	if 'all_video' in cache:
		response['all_video'] = cache.get('all_video')
	else:
		all_video = MyVideo.objects.all()
		all_video = [video.to_json() for video in all_video]
		cache.set('all_video', all_video, timeout=DEFAULT_TIMEOUT)
		response['all_video'] = all_video
	return render(request, "index.html", response)


def world(request):
	response = {}
	all_video = MyVideo.objects.all()
	response['all_video'] = [video.to_json() for video in all_video]
	return render(request, 'index.html', response)
# Create your views here.
