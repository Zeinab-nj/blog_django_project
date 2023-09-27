from django.shortcuts import render
from django.http import HttpResponse , Http404
from . models import Post 

# Create your views here. 

def index (request) : 
    return HttpResponse("index")



def post_list(request):
    posts = Posts.published.all() 
    context ={
        'posts' : posts ,
    }

    return render(request ,"template1.html",context)


def post_details(request, id) :
    try:
        posts = Post.published.get(id=id)
    except:
        raise Http404("No Posts Found!")

        context ={
        'post' : post ,
    }

    return render(request ,"template2.html",context)

