from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.


class Categories(models.Model):
    category = models.CharField(max_length=100, null=True)
    icon = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.category


    def get_url(self):
        return reverse('job_list', args =[self.slug])

    def get_db_url(self):
        return reverse('list_job', args = [self.slug])


    






class Job(models.Model):
    is_ad = models.BooleanField(default=False)
    varified = models.BooleanField(default=False, blank=True)
    Fresher = models.BooleanField(default=False, null=True)
    name = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    vaccancy = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='job_images',default='default.jpg', null=True, blank=True)
    photourl = models.URLField(max_length=3000, null=True, blank=True)
    availability = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True) 
    Age = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=50, null=True, blank=True)
    facebook =models.URLField(null=True, blank=True)
    instagram =models.URLField(null=True, blank=True)
    twitter =models.URLField(null=True, blank=True)
    linkedin =models.URLField(null=True, blank=True)
    yoursite =models.URLField(null=True, blank=True)
    job_disc = models.TextField(null=True, blank=True)
    skill = models.CharField(max_length=30, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    edu_experience = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True)
    mail = models.EmailField(null=True, blank=True)
    date = models.DateField(auto_now=True, null=True)
    salary = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    applyurl = models.URLField(max_length=3000, null=True, blank=True)
    




    def __str__(self):
        if (datetime.date.today() - self.date).days == 30 :
            return 'Expired'
        else:
            print(datetime.date.today() - self.date)
            return self.name


    def get_url(self):
        return reverse('job_details', args=[self.category.slug, self.slug, self.id])


    def get_job_id(self):
        return reverse('browse_res', args=[self.id])


    def get_job_id_shrt(self):
        return reverse('shrtlstd_res', args=[self.id])

    class Meta:
        ordering = ['date']