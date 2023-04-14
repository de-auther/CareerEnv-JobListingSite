from django.shortcuts import render, get_list_or_404
from .models import *

# Create your views here.


def blog(request, categ = None):
    if categ != None:
        category = Blog_category.objects.all()
        pk = get_list_or_404(category, slug = categ)
        blog = Blog_main.objects.all(category=pk)
        


    else:
        category = Blog_category.objects.all()
        blog = Blog_main.objects.all()

    return render(request, 'Blog/blog.html', {'blogs':blog, 'categories':category})










def blog_details(request, categ, blog):
    if categ != None and blog != None:
        blog = Blog_main.objects.get(category__slug = categ, slug = blog)
    return render(request, "Blog/blog-detail.html", {'blog':blog})