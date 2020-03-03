from django.shortcuts import render
from django.http import HttpResponse

posts=[{
    'author':"faiz hameed",
    'title':"django dev",
    'content':"django content for new website",
    'date_posted':"March 03 2020"
},
{
    'author':"muhammed saif",
    'title':"dbackend",
    'content':"django content said",
    'date_posted':"April 13 2020"
}]

def home(request):
    context={
       "posts":posts
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html")
# Create your views here.
