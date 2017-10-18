from django.shortcuts import render
# from django.http import HttpResponse
from test_app.forms import NewUserForm

# Create your views here.
def index(request):
    form =  NewUserForm()

    if request.method == 'POST':
        form =  NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("form error")

    return render(request,'test_app/index.html', {'form': form})
