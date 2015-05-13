from django.shortcuts import render
from .models import BlogsPost
# Create your views here.
def homepage(request):
	posts=BlogsPost.objects.all()
	context={'posts':posts}
	return render(request,'myblog/homepage.html',context)