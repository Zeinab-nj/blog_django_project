from django.urls import path 
from . import views

app_name ="blog"

urlpatterns = [
    path('' , views.index , name ="index"),
    #path('posts/' , views.post_list , name = "post_list"),
    path('posts/' , views.PostListView.as_view() , name = "post_list"),
    path('posts/<pk>/' , views.post_detail , name = "post_details"),
    path('posts/<post_id>/comment' , views.post_comment , name = "post_comment"),
    path('ticket' , views.ticket , name = "ticket"),

]
