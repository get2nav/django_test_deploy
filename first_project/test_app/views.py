from django.shortcuts import render

from django.http import HttpResponse

from test_app.models import AccessRecord,  Topic, Webpage


from . import forms
# Create your views here.


def index(request):
    accessRecord_list = AccessRecord.objects.order_by("date")
    web_dict = {"access_records": accessRecord_list}

    return render(request,'test_app/index.html', context = web_dict)


def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validtion")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request, "test_app/form.html", {'form': form} )
