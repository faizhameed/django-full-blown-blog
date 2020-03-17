from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    DeleteView
    )
from .models import Post


def home(request):
    context={
       "posts":Post.objects.all(),
       "title":"bloghome"
    }
    return render(request,"blog/home.html",context)

class PostListView(ListView):# working with a class based view
    model = Post
    template_name = "blog/home.html"
    context_object_name ="posts"
    ordering = ['-date_posted']
    paginate_by =5

class UserPostListView(ListView):# working with a class based view
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name ="posts"
    ordering = ['-date_posted']
    paginate_by =5

    def get_queryset(self):
        user =get_object_or_404(User,username =self.kwargs.get('username'))
        return Post.objects.filter(auth=user).order_by('-date_posted')
    
class PostDetailView(DetailView):   #<app>/<model>_<viewtype>.html
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields =['title','content']
    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model =Post
    fields =['title','content']
    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object() #to check the post editor is the same user that created the post
        if self.request.user == post.auth:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post=self.get_object() #to check the post deleter is the same user that created the post
        if self.request.user == post.auth:
            return True
        return False


def about(request):
    return render(request,"blog/about.html",{"title":"about"})
# Create your views here.
