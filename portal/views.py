from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def StartPage(request):
    return  render(request, 'portal/start.html')

class PostPage(ListView):
    model = Post
    template_name = 'portal/home.html'
    context_object_name = 'Posts'

def create(request):
    if request.method == "POST":
        person = Post()
        person.body = request.POST.get("title")
        person.body = request.POST.get("body")
        person.body = request.POST.get("author")
        person.save()
    return HttpResponseRedirect("/")



class UserPage(ListView):
    model = Post
    template_name = 'portal/user.html'
    def get_user(self,request):
        username = User.objects.all()
        if username is not None:
            context_object_name = Post.objects.filter(author=request.user)
            return context_object_name



