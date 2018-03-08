from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
# from posts.models import Post
from . import forms
# Create your views here.
class PostListView(SelectRelatedMixin, ListView):
	model = models.Post
	select_related = ['user']

	def get_query_set(self):
		return models.Post.objects.filter(created_at__lte= timezone.now()).order_by(self.created_at)


class PostDetail(DetailView):
	model = models.Post
	select_related = ["user"]
	# def get_queryset(self):
	# 	queryset = super().get_queryset()
	# 	return queryset.filter(user__username__iexact=self.kwargs.get('username'))


# class NewPost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
class NewPost(LoginRequiredMixin, CreateView):
	fields = ('title', 'content')
	model = models.Post
	# form_class = forms.PostForm
	# redirect_field_name = "posts/post_detail.html"
	success_url = reverse_lazy('posts:post_list')
	# success_url = '/posts'
	# success_url = reverse_lazy('posts/post_list')
	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)

# class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
# 	select_related = ["user"]
# 	model = models.Post
# 	success_url = reverse_lazy("posts:post_list")

# 	def get_queryset(self):
# 		queryset = super().get_queryset()
# 		return queryset.filter(user_id = self.request.user.id)

# 	def delete(self):
# 		messages.success(self.request, "Post was deleted!")
# 		return super().delete()

@login_required
def upvote(request, pk):
  if request.method == "POST":
    post = models.Post.objects.get(pk=pk)
    post.points +=1
    post.save()
    return redirect('posts:post_list')

@login_required
def delete(request, pk):
	post = models.Post.objects.get(pk=pk)
	post.delete()
	return redirect('posts:post_list')

@login_required
def downvote(request, pk):
  if request.method == "POST":
    post = models.Post.objects.get(pk=pk)
    post.points -=1
    post.save()
    return redirect('posts:post_list')
