# Django - Fake Factory

generates test data using library faker

```py
# install faker (in terminal - active environment)
pip install faker

# setup
# populate_users.py
...
from faker import Faker
fakegen = Faker()

def poplate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # new entry
        user = User.objects.get_or_create(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake_email
        )[0]


if __name__ == '__main__':
    print('POPULATE DATABASE')
    poplate(20)
    print('COMPLETE')


# and then in terminal populate this (in active environment)
# (env) C:\Users\User\projects\faker_project_>python populate_users.py
python populate_users.py

```


