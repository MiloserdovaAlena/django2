from decimal import Decimal

from django.core.management import BaseCommand

from onlinerating.models import AccessRights


class Command(BaseCommand):
    help = 'Remove all rights of user to view any questionnaire'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')

    def handle(self, *args, **options):
        username = options['username']
        try:
            rights = AccessRights.objects.filter(user__username=username)
            
            for right in rights:
                right.can_view_answers = False
                right.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully changed rights for {username}.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
            