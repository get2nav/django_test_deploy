from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    my_dict = {
        "date_data": now,
    }

    return render(request, 'test_app/index.html', context = my_dict)
