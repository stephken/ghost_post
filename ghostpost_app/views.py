from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost_app.models import Roast_Boast
from ghostpost_app.forms import add_roastboast

# Create your views here.


def index_view(request):
    roastboast_history = Roast_Boast.objects.all()
    return render(request, "index.html", {"most_recent": roastboast_history})
    

def boast_view(request):
    pass

def roast_view(request):
    pass

def add_roastboast_view(request):
    if request.method == 'POST':
        form = add_roastboast(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Roast_Boast.objects.create(boast=data.get("roastboast"), user_input=data.get("content"))
            return HttpResponseRedirect(reverse('homepage'))
    form = add_roastboast()
    return render(request, "generic_form.html", {"form": form} )


def score_view(request):
    pass