"""
Django command to wait for the db to be available

"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django command to pause execution until database is available

    """
    def handle(self, *args, **options):
        """
        Handle the command

        """
        self.stdout.write('Waiting for database...')
        pass