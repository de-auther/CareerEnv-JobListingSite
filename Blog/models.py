from django.db import models
from django.urls import reverse

# Create your models here.




class Blog_category(models.Model):
    category = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.category


    def get_categ(self):
        return reverse('blog', args=[self.slug])






class Blog_main(models.Model):
    headpic = models.URLField(max_length=3000, null=True, blank=True)
    header = models.TextField(null=True, blank=True)
    h1 = models.CharField(max_length=100, null=True, blank=True)
    p1 = models.TextField(null=True, blank=True)
    qt1 = models.CharField(max_length=500, null=True, blank=True)
    pic1 = models.URLField(max_length=3000, null=True, blank=True)
    h2 = models.CharField(max_length=100, null=True, blank=True)
    p2 = models.TextField(null=True, blank=True)
    qt1 = models.CharField(max_length=500, null=True, blank=True)
    pic2 = models.URLField(max_length=3000, null=True, blank=True)
    h3 = models.CharField(max_length=100, null=True, blank=True)
    p3 = models.TextField(null=True, blank=True)
    qt3 = models.CharField(max_length=500, null=True, blank=True)
    pic3 = models.URLField(max_length=3000, null=True, blank=True)
    h4 = models.CharField(max_length=100, null=True, blank=True)
    p4 = models.TextField(null=True, blank=True)
    qt4 = models.CharField(max_length=500, null=True, blank=True)
    pic4 = models.URLField(max_length=3000, null=True, blank=True)
    h5 = models.CharField(max_length=100, null=True, blank=True)
    p5 = models.TextField(null=True, blank=True)
    qt5 = models.CharField(max_length=500, null=True, blank=True)
    pic5 = models.URLField(max_length=3000, null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    
    
    
    
    

    date = models.DateField()
    category = models.ForeignKey(Blog_category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.h1



    def get_blog(self):
        return reverse('blog_details', args=[self.category.slug, self.slug])




class Blog_comment(models.Model):
    blog = models.OneToOneField('Blog_main', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now=True, null=True)
    avatar = models.CharField(max_length=100, null=True, blank=True)