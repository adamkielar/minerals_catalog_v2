import json

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from minerals.models import Mineral


class Command(BaseCommand):
    """Populate database with minerals data from JSON file"""

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as data_file:
            json_data = json.load(data_file)

            for mineral_data in json_data:
                try:
                    Mineral.objects.create(**mineral_data)
                except IntegrityError:
                    continue

