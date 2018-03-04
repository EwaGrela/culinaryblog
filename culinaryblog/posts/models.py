from django.db import models
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
# import misaka
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User, related_name = "posts")
	title = models.CharField(max_length=56)
	content = models.TextField(unique=False)
	content_html = models.TextField(editable=True)
	created_at = models.DateTimeField(auto_now=True)
	points = models.IntegerField(default=1)

	def __str__(self):
		return self.title


	# def save(self, *args, **kwargs):
	# 	self.content_html = misaka.html(self.content)
	# 	self.points = self.points
	# 	super().save(self, *args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('posts:post_detail')

	class Meta:
		ordering = ['-points']
		# unique_together = ['user', 'content']