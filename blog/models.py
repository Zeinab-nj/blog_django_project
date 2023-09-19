from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# manager 
class PublishedManager(models.Manager) :
    def get_queryset(self) :
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)

# Create your models here.
class Post(models.Model) :
   
    #relational
    author = models.ForeignKey(User , on_delete =models.CASCADE ,related_name = 'user_posts')
    class Status(models.TextChoices) :
        DRAFT = 'DR' , 'Draft'
        PUBLISHED = 'PB' ,'published'
        REJECTED =  'RJ' , 'rejected'
        
    #data fields
    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250)
    
    #date 
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    published = PublishedManager()
    #choice fields
    status = models.CharField(max_length = 2 , choices=Status.choices , default=Status.DRAFT )

    class Meta :
        ordering = ['-publish']
        indexes = [
            models.Index(fields = ['-publish'])
        ]

    def __str__ (self) :
        return self.title
