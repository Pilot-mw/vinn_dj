from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates superuser if not exists'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'djvinmw@gmail.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Admin user created'))
        else:
            self.stdout.write('Admin user already exists')