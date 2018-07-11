from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
	def handle(self, *args, **options):
		if User.objects.count() == 0:
			admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
			admin.is_active = True
			admin.is_admin = True
			admin.save()
			print('Admin created. \nUser: admin\nPass:admin123')
		else:
			print('Admin exists, skipping ...')