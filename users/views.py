from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) ##create data within that form
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return  render(request,'users/register.html',{'form':form})
@login_required  ##user must be logged in 
def profile(request):
    return render(request,'users/profile.html')