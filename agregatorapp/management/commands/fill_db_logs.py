from django.core.management import BaseCommand

from agregatorapp.models import Log
from agregatorapp.services import load_logs


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_logs = load_logs()
        Log.objects.bulk_create(data_logs)
