import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

import django
django.setup()

from faker import Faker
from test_app.models import User



def user_data(N = 5):
    fakegen = Faker()


    for entry in range(N):

        fake_first_name = fakegen.first_name()
        fake_last_name= fakegen.last_name()
        fake_email = fakegen.email()

        user_insert = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]
        user_insert.save()



if __name__ == '__main__':
    print("start populate")
    user_data(20)
    print("end populate")
