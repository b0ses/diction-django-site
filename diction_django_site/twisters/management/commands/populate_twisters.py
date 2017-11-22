from lxml import html
import re
import requests

from django.core.management.base import BaseCommand
from diction_django_site.twisters.models import Twister

UEBERSETZUNG_SITE = 'http://www.uebersetzung.at/twister/en.htm'

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def add_arguments(self, parser):
        parser.add_argument('--uebersetzung', action='store_true')


    def get_twisters_from_uebersetzung(self):
        page = requests.get(UEBERSETZUNG_SITE)
        #TODO: Simplify this
        replacements = [('<BR>', '\n'),
                        ('<br>', '\n'),
                        ('<TT>', ''),
                        ('\r', ''),
                        ('\n ', '\n'),
                        ('\n\n', '\n')]
        content = page.content.decode()
        for replacement in replacements:
            content = re.sub(replacement[0], replacement[1], content)
        fixed_line_breaks = content.encode()
        tree = html.fromstring(fixed_line_breaks)
        twisters = tree.xpath('//p[@class="TXT"]/text()')
        for twister in twisters:
            Twister.objects.get_or_create(twister=twister, source=UEBERSETZUNG_SITE)

    def handle(self, *args, **options):
        if options['uebersetzung']:
            twisters = self.get_twisters_from_uebersetzung()