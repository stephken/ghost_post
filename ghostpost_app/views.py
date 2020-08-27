from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost_app.models import Roast_Boast
from ghostpost_app.forms import add_roastboast

# Create your views here.


def index_view(request):
    roastboast_history = Roast_Boast.objects.filter().order_by('-id')
    return render(request, "index.html", {"most_recent": roastboast_history})
    

def boast_view(request):
    boast_posts = Roast_Boast.objects.filter(boast=True).order_by('-id')
    return render(request, 'boast.html', {'boast_post': boast_posts, 'boast_title': 'Boasts!!!'})

def roast_view(request):
    roast_posts = Roast_Boast.objects.filter(boast=False).order_by('-id')
    return render(request, 'roast.html', {'roast_posts': roast_posts, 'roast_title': 'Roasts!!!'})

#def add_roastboast_view(request):
    #if request.method == 'POST':
        #form = add_roastboast(request.POST)
        #if form.is_valid():
            #data = form.cleaned_data
            #Roast_Boast.objects.create(boast=data.get("roastboast"), user_input=data.get("user_input"))
            #return HttpResponseRedirect(reverse('Home'))
    #form = add_roastboast()
    #return render(request, "generic_form.html", {"form": form} )


def score_view(request):
    votes = sorted(Roast_Boast.objects.all(), key=lambda votes: votes.count_votes)[::-1]
    return render(request, 'score.html', {'score': score, 'score_title': 'Sorted by your votes!!!'})

def add_post_view(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
              user_input = data.get('user_input'),
              boast = data.get('boast')
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddPost()
    return render(request, 'form.html', {'form': form, 'add_title': 'Add a post now!'})


def up_vote(request, post_id):
    post = Roast_Boast.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def down_vote(request, post_id):
    post = Roast_Boast.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

