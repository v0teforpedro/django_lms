from django.core.management.base import BaseCommand, CommandError

from students.models import Student


class Command(BaseCommand):
    help = 'Generates fake data for student(s), and adds it to database'        # noqa

    def add_arguments(self, parser):
        parser.add_argument('cnt', type=int, nargs='?', const=1, default=10, help='Amount of students to generate')

    def handle(self, *args, **options):
        cnt = options['cnt']

        if cnt <= 100:
            Student.generate(cnt)
            self.stdout.write(self.style.SUCCESS(f'{cnt} student(s) created!'))
        else:
            raise CommandError('generator is capped at max 100 students per use')
