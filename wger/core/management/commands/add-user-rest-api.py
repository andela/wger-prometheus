from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission

from wger.core.models import User, UserProfile


class Command(BaseCommand):

    help = "Assign REST API User with permissions to create"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, **options):

        user = User.objects.get(username=options['username'])

        profile = UserProfile.objects.get(user=user)

        permission_add = Permission.objects.get(name='Can add user')
        permission_change = Permission.objects.get(name='Can change user')

        if not profile.rest_api_user:

            user.user_permissions.add(permission_add)
            user.user_permissions.add(permission_change)
            user.save()

            profile.rest_api_user = True
            profile.save()

            assigned = "Successfully granted {} user creation rights".format(options['username'])
            print(assigned)

        else:
            print("User already assigned permission")
