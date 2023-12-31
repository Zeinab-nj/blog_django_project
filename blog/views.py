from django.shortcuts import render , get_object_or_404,redirect 
from django.http import HttpResponse , Http404
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView,DetailView
from django.views.decorators.http import require_POST
# Create your views here. 

def index (request) : 
    return render(request,'blog/index.html')



#def post_list(request):
 #   posts = Post.published.all() 
  #  paginator = Paginator(posts, 3)
   # page_number = request.GET.get('page',1)
    #try:
     #   posts = paginator.page(page_number)
    #except EmptyPage:
     #   posts = paginator.page(paginator.num_pages)
    #except PageNotAnInteger:
     #   posts = paginator.page(1)
    #context ={
     #   'posts' : posts ,
    #}

   # return render(request ,"blog/list.html",context)

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3 
    template_name = "blog/list.html"

def post_detail(request, pk):
    post = get_object_or_404(Post , id=pk , status=Post.Status.PUBLISHED)
    form = CommentForm()
    comments = post.comments.filter(active = True)
    context = {
        'post': post,
        'form' : form, 
        'comments' : comments,
    }
    return render(request,"blog/detail.html", context)
    
#class PostDetailView(DetailView) :
 #   model= Post
  #  template_name = "blog/detail.html"

def ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create(message=cd["message"],name=cd["name"],
                                               email=cd["email"],phone=cd["phone"],subject=cd["subject"])
            cd = form.cleaned_data
            ticket_obj.save() 
            return redirect("blog:ticket")
    else:
        form = TicketForm()
    return render(request , "forms/ticket.html" , {"form":form})

@require_POST
def post_comment(request , post_id) :
    post = get_object_or_404(Post, id=post_id, status = Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data = request.POST)
    if form.is_valid():
        comment = form.save(commit = False)
        comment.post = post
        comment.save()
    context={ 
        'post' : post,
        'form' : form,
        'comment' : comment,
        }
    return render(request,"forms/comment.html",context)




