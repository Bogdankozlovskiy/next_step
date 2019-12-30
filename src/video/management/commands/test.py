from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Test Base Command'
	def handle(self, *args, **kwargs):
		print('hello test 1')