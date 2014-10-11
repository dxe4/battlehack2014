import django
django.setup()

from theapp.models import User


def make_user(flag):
    email = 'user_{}@eggs.spam'.format(flag)
    password = 'user_{}'.format(flag)

    user = User.objects.create_user(
        email, email=email, password=password)
    user.is_active = True
    user.save()
    print('user made', email)

for i in ('a', 'b', 'c'):
    make_user(i)
