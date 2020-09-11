from django.urls import path
from blogposts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),

]