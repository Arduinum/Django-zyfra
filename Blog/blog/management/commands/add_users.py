from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from blog.management.commands.data import data_users


class Command(BaseCommand):
    help = 'создаст пользователей для db'

    def handle(self, *args, **options):
        try:
            for user in data_users:
                
                if not User.objects.filter(username=data_users[user]['username']).exists():
                    user_model = User()
                    user_model.username = data_users[user]['username']
                    user_model.is_superuser = data_users[user]['is_superuser']
                    user_model.is_staff = data_users[user]['is_staff']
                    user_model.is_active = data_users[user]['is_active']
                    user_model.password = data_users[user]['password']
                    user_model.save()
        except KeyError as err:
            raise err
        except IndexError as err:
            raise err
        except IntegrityError as err:
            raise err
        self.stdout.write(self.style.SUCCESS('Успешное заполнение модели User!'))
