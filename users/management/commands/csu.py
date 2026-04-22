from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **options):
        email = "admin@sky.pro"
        password = "0987654321admin"

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING("User already exists"))
            return

        User.objects.create_superuser(
            email=email,
            password=password,
        )

        self.stdout.write(self.style.SUCCESS("Superuser created successfully"))