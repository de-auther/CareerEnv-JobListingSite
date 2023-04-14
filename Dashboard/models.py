from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    experience = models.CharField(max_length=20, null=True, blank=True)
    first= models.CharField(max_length=100, null=True, blank=True)
    last= models.CharField(max_length=100, null=True, blank=True)
    dp = models.ImageField(upload_to='profilePic', default='default.jpg')
    status= models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    about = models.CharField(max_length=10000,null=True, blank=True)
    age = models.CharField(max_length=2, null=True, blank=True)
    phone = models.CharField(max_length=14,null=True, blank=True)
    postal = models.CharField(max_length=8,null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    city=models.CharField(max_length=100,null=True, blank=True)
    state=models.CharField(max_length=100, null=True, blank=True)
    country=models.CharField(max_length=50,null=True, blank=True)
    language = models.CharField(max_length=100,null=True, blank=True)
    yoursite = models.CharField(max_length=100, null=True, blank=True)
    photo1 = models.ImageField(upload_to='images', blank=True)
    photo2 = models.ImageField(upload_to='images', blank=True)


    is_company = models.BooleanField()
    ceo =models.CharField(max_length=100,null=True, blank=True)
    employee_no = models.CharField(max_length=100,null=True, blank=True)





    def __str__(self):
          return self.user.username

    




     

    def get_url(self):
        return reverse('view_res', args =[self.id])
    







class Skills(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     skill1 = models.CharField(max_length=100, blank=True)
     per1 = models.IntegerField(default=50, blank=True)
     skill2 = models.CharField(max_length=100, blank=True)
     per2 = models.IntegerField(default=50, blank=True)
     skill3 = models.CharField(max_length=100, blank=True)
     per3 = models.IntegerField(default=50, blank=True)
     skill4 = models.CharField(max_length=100, blank=True)
     per4 = models.IntegerField(default=50, blank=True)
     skill5 = models.CharField(max_length=100, blank=True)
     per5 = models.IntegerField(default=50, blank=True)
     skill6 = models.CharField(max_length=100, blank=True)
     per6 = models.IntegerField(default=50, blank=True)









class Education(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course1 = models.CharField(max_length=100, null=True, blank=True)
    stream1 = models.CharField(max_length=100, null=True, blank=True)
    university1 = models.CharField(max_length=100, null=True, blank=True)
    date1 = models.CharField(max_length=100, default=0, blank=True)
    discription1 = models.CharField(max_length=1000, null=True, blank=True)
    course2 = models.CharField(max_length=100, null=True, blank=True)
    stream2 = models.CharField(max_length=100, null=True, blank=True)
    university2 = models.CharField(max_length=100, null=True, blank=True)
    date2 = models.CharField(max_length=100, default=0, blank=True, null=True)
    discription2 = models.CharField(max_length=1000, null=True, blank=True)

















class Projects(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     name1 = models.CharField(max_length=100, null=True, blank=True)
     date1 = models.CharField(max_length=100, null=True, blank=True)
     discription1 = models.CharField(max_length=1000, null=True, blank=True)
     name2 = models.CharField(max_length=100, null=True, blank=True)
     date2 = models.CharField(max_length=100, null=True, blank=True)
     discription2 = models.CharField(max_length=1000, null=True, blank=True)



    










class Experience(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     name1 = models.CharField(max_length=100, null=True, blank=True)
     date1 = models.CharField(max_length=100, null=True, blank=True)
     discription1 = models.CharField(max_length=1000, null=True, blank=True)
     company1 = models.CharField(max_length=100, null=True, blank=True)
     name2 = models.CharField(max_length=100, null=True, blank=True)
     date2 = models.CharField(max_length=100, null=True, blank=True)
     discription2 = models.CharField(max_length=1000, null=True, blank=True)
     company2 = models.CharField(max_length=100, null=True, blank=True)
     salary1 = models.CharField(max_length=100, null=True, blank=True)
     salary2 = models.CharField(max_length=100, null=True, blank=True)













class Job_applied(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     job_applied = models.CharField(max_length=100, null=True)
     job_id = models.CharField(max_length=100, null=True)


     class Meta:
          ordering =['job_applied']



     def __str__(self):
          return self.job_applied














class Get_Res(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     job_id = models.CharField(max_length=100, null=True)
     seeker_name = models.CharField(max_length=100, null=True)
     resume = models.CharField(max_length=100, null=True)
     photo = models.CharField(max_length=100, null=True)
     status = models.CharField(max_length=100, null=True)
     experience = models.CharField(max_length=100, null=True)



     class Meta:
          ordering =['seeker_name']




     def __str__(self):
          return self.user.username



     


class Shortlisted(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE, null= True)
     resume = models.CharField(max_length=100, null=True)
     job_id = models.CharField(max_length=100, null=True)
     seeker_name = models.CharField(max_length=100, null=True)


     class Meta:
          ordering =['seeker_name']









class Message(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     job = models.CharField(max_length=100, null=True)
     company = models.CharField(max_length=100, null=True)
     job_id = models.CharField(max_length=100, null=True)



     class Meta:
          ordering =['job']
     








