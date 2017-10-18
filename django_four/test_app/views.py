from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {
            "name":" hello index",
            "number": 100
        }
    return render(request, 'test_app/index.html', context = context_dict)


def other(request):
    return render(request, 'test_app/other.html')


def relative_url(request):
    return render(request, 'test_app/relative_url_templates.html')
