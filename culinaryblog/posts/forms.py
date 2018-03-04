from django import forms
from posts.models import Post 
from django.contrib.auth import get_user_model

# class PostForm(forms.ModelForm):
# 	class Meta():
# 		model = Post
# 		fields = ( "user", "title", "content")
# 		widgets = {
# 			"title": forms.TextInput(),
# 			"content": forms.TextInput()
# 		}
