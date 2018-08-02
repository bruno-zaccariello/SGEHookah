from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import *

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
		if Categoriaproduto.objects.count() == 0:
			Categoriaproduto.objects.create(nomecategoria='Juice')
			print('Categoria criada')
		if Unidademedida.objects.count() == 0:
			Unidademedida.objects.create(unidademedida='ml')
			print('Unidade de Medida criada')