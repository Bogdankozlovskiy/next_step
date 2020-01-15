from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
import logging
from .models import MyVideo
from django.views.generic import View 
from .forms import CommentForm


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


class Create(View):
	def get(self, request):
		form = CommentForm(initial={'video_id': '2'})
		return render(request, "index.html", {'form':form})

	def post(self, request, idd):
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save(idd=idd, user=request.user)
			logging.warning('is valid')
			return redirect('main')
		logging.warning('is not valid')
		return redirect('main')
# Create your views here.
