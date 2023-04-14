from django.shortcuts import render, redirect
from django.db.models import Q
from Dashboard.models import Message
from .models import Categories, Job
from Dashboard.models import Profile, Skills, Education, Projects, Experience
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def home(request):
    categories = Categories.objects.all()
    jobs = Job.objects.all()
    job_count = Job.objects.all().count()
    user_count = User.objects.all().count()
    cities = Job.objects.values_list('city', flat=True).distinct()
    if request.user.username:
        user=User.objects.get(username=request.user.username)
        user_details = Profile.objects.get(user=user)
    else:
        user_details = None
    if User.objects.filter(username=request.user.username):
        
        if Profile.objects.filter(user=User.objects.get(username=request.user.username)):
            profile = Profile.objects.filter(user=User.objects.get(username=request.user.username))
        else:
            return redirect('dashboard')
        
    else:
        profile = None
    return render(request, 'Main/index.html', {'categories':categories, 'jobs':jobs, 'job_count':job_count, 'user_count':user_count, 'profile':profile, 'user_details':user_details, 'cities':cities})







def seeker_reg(request):
    user=User.objects.get(username=request.user.username)
    if request.method == 'POST':
        user_details = Profile.objects.create(user=user, is_company=False).save()
        user_details1 = Skills.objects.create(user=user).save()
        user_details2 = Education.objects.create(user=user).save()
        user_details3 = Projects.objects.create(user=user).save()
        user_details4 = Experience.objects.create(user=user).save()

        return redirect('edit_profile')

        send_mail(
            subject='Seeker Account Created',
            message= f"Hello {request.user.username},\n\n\n You have successfully created a Seeker Account on careerEnv\n\n\n\n Regards careerEnv",
            from_email = 'support.careerenv.com',
            recipient_list= [request.user.email,]
        )

    else:
        return render(request, 'Main/user_type')




def employer_reg(request):
    user=User.objects.get(username=request.user.username)
    if request.method == 'POST':
        user_details = Profile.objects.create(user=user, is_company=True).save()


        return redirect('create_com')
        send_mail(
            subject='Employer Account Created',
            message= f"Hello {request.user.username},\n\n\n You have successfully created an Employer Account on careerEnv\n\n\n\n Regards careerEnv",
            from_email = 'support.careerenv.com',
            recipient_list= [request.user.email,]
        )

    else:
        return render(request, 'Main/user_type')







def search(request):
    key = request.GET.get('keyword')
    city = request.GET.get('cityselect')
    cat = request.GET.get('categoryselect')
    
    
    categories = Categories.objects.all()
    cities = Job.objects.values_list('city', flat=True).distinct()
    key_job = Job.objects.filter(Q(name__contains = key))
    city_job = Job.objects.filter(city = city)
    cat_job = Job.objects.filter(category__category= cat)

    if key_job.exists() and city_job.exists() and cat_job.exists():
        jobs = ( key_job & city_job & cat_job)
    else:
        messages.error(request,'You should fill all fields')
        return redirect('/')

    
        
    p = Paginator(jobs, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        return redirect('not_found')

    
        
    
    
    return render(request, 'Dashboard/job_list.html', {'categories':categories, 'jobs':page, 'cities':cities})



























def job_list(request, categ=None):
    if categ != None:
        categories = Categories.objects.all()
        pk = get_object_or_404(categories,slug=categ)
        jobs = Job.objects.filter(category=pk)
        
    else:
        categories = Categories.objects.all()
        jobs = Job.objects.all()

    p = Paginator(jobs, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        return redirect('not_found')

    return render(request,'Main/job_list.html',{'jobs':page, 'categories': categories})



































def job_details(request,categ, job):
    job = Job.objects.get(category__slug=categ, slug=job)

    return render(request, 'Dashboard/job_details.html', {'job':job})













def not_found(request):
    return render(request, 'Main/not_found.html')


def youDone(request):
    return render(request,  'Main/youDone.html')









