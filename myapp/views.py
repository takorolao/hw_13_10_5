from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, BlogPost
from django.db import models


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username, password=password)
            return redirect('home')
        except CustomUser.DoesNotExist:
            return redirect('register')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        CustomUser.objects.create(username=username, password=password)
        return redirect('login')
    
class AllUsersView(View):
    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, 'all_users.html', {'users': users})
    
class UserDetailView(View):
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        return render(request, 'user_detail.html', {'user': user})


class BlogPostListView(View):
    def get(self, request):
        posts = BlogPost.objects.order_by('-pub_date')  
        return render(request, 'blog_post_list.html', {'posts': posts})

