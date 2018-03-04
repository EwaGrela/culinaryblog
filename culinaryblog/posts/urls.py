from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "posts"

urlpatterns = [
url(r'^$',views.PostListView.as_view(), name='post_list'),
url(r'^post/(?P<pk>\d+)$', views.PostDetail.as_view(), name='post_detail'),
url(r'^new/$', views.NewPost.as_view(), name ='new_post'),
url(r'^post/(?P<pk>\d+)/delete', views.DeletePost.as_view(), name ='delete'), 
url(r'^post/(?P<pk>\d+)/upvote', views.upvote, name='upvote'),
url(r'^post/(?P<pk>\d+)/downvote', views.downvote, name='downvote'),

]