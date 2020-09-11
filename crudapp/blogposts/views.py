from django.shortcuts import render
from django.views.generic import (ListView, 
	DetailView, 
	CreateView, 
	DeleteView,
	UpdateView)
from .models import Post

class PostListView(ListView):
	model = Post
	context_object_name = 'posts'


class PostDetailView(DetailView):
	model = Post


class PostCreateView(CreateView):
	model = Post
	fields = '__all__'
	success_url = '/'

	# def form_valid(self, form):
 #        form.instance.author = self.request.user
 #        return super().form_valid(form)


class PostDeleteView(DeleteView):
	model = Post
	success_url = '/'


class PostUpdateView(UpdateView):
	model = Post
	fields = '__all__'
	success_url = '/'