from django.core.management.base import BaseCommand, CommandError

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates fake data for teacher(s), and adds it to database'

    def add_arguments(self, parser):
        parser.add_argument('cnt', type=int, nargs='?', const=1, default=10, help='Amount of teachers to generate')

    def handle(self, *args, **options):
        cnt = options['cnt']

        if cnt <= 100:
            Teacher.gen_teachers(cnt)
            self.stdout.write(self.style.SUCCESS(f'{cnt} teacher(s) created!'))
        else:
            raise CommandError('generator is capped at max 100 teachers per use')
