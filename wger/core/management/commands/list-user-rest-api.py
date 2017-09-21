from django.core.management.base import BaseCommand

from wger.core.models import User, APIUsers


class Command(BaseCommand):

    help = "List all REST API Users with permissions to create users"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, **options):

        try:

            user = User.objects.get(username=options['username'])

            api_users = APIUsers.objects.filter(app_owner=user).select_related('app_user')

            print("Users created by ", options['username'], "\n")

            for api_user in api_users:

                result = "API User {} , Has Permissions: \nAdd User: {}, \nChange User: {}\n"\
                    .format(api_user.app_user, api_user.app_user.has_perm('auth.add_user'),
                            api_user.app_user.has_perm('auth.change_user'))

                print(result)

        except:
            print("Could Not Find User Provided")
