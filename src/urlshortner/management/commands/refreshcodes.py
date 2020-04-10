from django.core.management.base import BaseCommand, CommandError
from urlshortner.models import MyURL
class Command(BaseCommand):
    help = 'Refreshes all MyURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return MyURL.objects.refresh_shortcode(items=options['items'])