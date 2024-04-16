from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    This command create superuser in your service DB for work with data in admin-panel.
    Default user data:
    username - admin,
    password - admin.
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            username='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('admin')
        user.save()
