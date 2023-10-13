from django.urls import path
from .views import HomeView, LoginView, RegisterView, AllUsersView, UserDetailView, BlogPostListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('all_users/', AllUsersView.as_view(), name='all_users'),
    path('user_detail/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
]
