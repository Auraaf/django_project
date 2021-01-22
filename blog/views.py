from django.shortcuts import render
from .models import Post


posts = [
    {
        'author':'CoreyMS',
        'title' : 'Blog Post 1',
        'content': 'First Post content',
        'date_posted' : 'Aug 25 , 2018'
    },

{
        'author':'Azeez',
        'title' : 'Blog Post 2',
        'content': '2nd Post content',
        'date_posted' : 'Aug 30 , 2018'
    },
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    #calling from blog.urls
    return render(request, 'blog/home.html' , context) #already know template is second argument
def about(request):
    return render(request , 'blog/about.html', {'title':'About'})
#to avoid writting whole html code in this ()
#we will create template directory in blog
#also to make it available in the project
#open apps.py and copy BlogConfig name class
#and paste it in settings.imp
# Create your views here.
