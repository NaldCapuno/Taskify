from django.core.management.base import BaseCommand
from main import models

class Command(BaseCommand):
    help = 'Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_priorities()

    def create_priorities(self):
        low = models.Priority(name='Low', level=1)
        medium = models.Priority(name='Medium', level=2)
        high = models.Priority(name='High', level=3)

        prios = [low, medium, high]

        for prio in prios:
            prio.save()

        self.stdout.write(self.style.SUCCESS('Successfully created priorities.'))