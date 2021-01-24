from django.shortcuts import render, get_object_or_404      #it will get an object from database or show 404 error
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

from .models import blog
# Create your views here.


def allblogs(request):
    blogs = blog.objects.order_by('-pub_date')
    return render(request, 'blog/allblogs.html', {'blogs' : blogs})


def details(request, blog_id):
    detailblog = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
