from django.contrib.auth.models import User

if User.objects.get(email='admin@example.com'):
    pass
else:
    User.objects.create_superuser('admin', 'admin@example.com', 'pass')
