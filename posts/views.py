from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request,'index.html',context) 
    
def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)
    
    comments = post.comments.filter(active=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect("")
    else:
        form = CommentForm
                
    return render(request,'post_detail.html',{'post':post,'comments':comments, 'form':form }) 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado' )
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    context = {'form' : form }
    return render(request, 'templates/register.html', context)

def home(request):
    return render(request,'home.html') 

def inicio(request):
    return render(request,'inicio.html') 
