from django.shortcuts import render
from django.http import HttpResponse

posts=[{
    'author':"faiz hameed",
    'title':"Blog post 1",
    'content':"django content for new website",
    'date_posted':"March 03 2020"
},
{
    'author':"muhammed saif",
    'title':"Blog post 2",
    'content':"django content said",
    'date_posted':"April 13 2020"
}]

def home(request):
    context={
       "posts":posts
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html",{"title":"about"})
# Create your views here.
