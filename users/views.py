from django.shortcuts import render
from users.models import User

# Create your views here.


def index(req):
    return render(req, 'index.html')


def users(req):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(req, 'users.html', context=user_dict)
