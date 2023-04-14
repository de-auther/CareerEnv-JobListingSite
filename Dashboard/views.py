from django.shortcuts import render, redirect
from .models import Profile, Projects, Education, Experience, Skills, Job_applied, Get_Res, Message, Shortlisted
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Main.models import Job, Categories
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.




@login_required(login_url='account_login')
def dashboard(request):
    user=User.objects.get(username=request.user.username)

    if Profile.objects.filter(user=user):
        user_details= Profile.objects.get(user=user)



    else:
        
        return render(request, 'Main/user_type.html')
        
        
            


    count_job_posted = Job.objects.filter(company=request.user.username).count()
    count_job_applied = Job_applied.objects.filter(user = User.objects.get(username=request.user.username)).count()
    
    posted = Job.objects.filter(company=request.user.username)
    category = Categories.objects.all()
    shortlstd = Shortlisted.objects.filter(user = User.objects.get(username = request.user.username)).count()
    no_selected = Message.objects.filter(user = User.objects.get(username = request.user.username), job__startswith = "You're not selected for").count()
    selected = Message.objects.filter(user = User.objects.get(username = request.user.username), job__startswith = "You're Shortlisted for").count()
    applications = Get_Res.objects.filter(user=User.objects.get(username=request.user.username)).count()
    if Message.objects.filter(user = User.objects.get(username = request.user.username)):
        msg = Message.objects.filter(user = User.objects.get(username = request.user.username))
    else:
        msg =None

    return render(request, 'Dashboard/dashboard.html', {'categories':category, 'user_details':user_details, 'count_posted':count_job_posted, 'count_applied':count_job_applied,   'posted':posted, 'message':msg, 'shrtlstd':shortlstd, 'not_slctd':no_selected, 'slctd':selected, 'applctions':applications })







@login_required(login_url='account_login')
def create_job(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = Categories.objects.get(id=category_id)
        
            

        jobs =   Job(
                category = category,
                company = request.user.username,
                photo = request.FILES.get('photo'),
                photourl = request.POST.get('photourl'),
                name = request.POST.get('name'),
                city = request.POST.get('city'),
                availability = request.POST.get('availability'),
                mail = request.POST.get('mail'),
                phone = request.POST.get('phone'),
                vaccancy = request.POST.get('vaccancy'),
                salary = request.POST.get('salary'),
                experience = request.POST.get('experience'),
                qualification = request.POST.get('education'),
                gender = request.POST.get('gender'),
                job_disc = request.POST.get('discription'),
                skill = request.POST.get('skill'),
                skills = request.POST.get('skill_discription'),
                edu_experience = request.POST.get('edu_discription'),
                facebook = request.POST.get('facebook'),
                twitter = request.POST.get('twitter'),
                instagram = request.POST.get('instagram'),
                linkedin = request.POST.get('linkedin'),
                yoursite = request.POST.get('yoursite'),
                Age = request.POST.get('age'),
                Fresher = request.POST.get('fresher'),
                slug = slugify(request.POST.get('name'))
                    )


        
        
        jobs.save()


        msg = Message(

        user = User.objects.get(username = request.user.username),
        job ="You've posted"+' '+Job.objects.get(mail = request.POST.get('mail'), name = request.POST.get('name'), phone = request.POST.get('phone')).name,
        company ="by"+' '+request.user.username,
        job_id = Job.objects.get(mail = request.POST.get('mail'), name = request.POST.get('name'), phone = request.POST.get('phone')).id


        )
        msg.save()

        return redirect('list_job')
    else:



        categories = Categories.objects.all()
        return render(request, 'Dashboard/create_job.html', {'categories':categories})





def view_res(request,  id):


    user=Profile.objects.get(id=id).user
    user_details = Profile.objects.get(user=user)
    user_details1 = Skills.objects.get(user=user)
    user_details2 = Education.objects.get(user=user)
    user_details3 = Projects.objects.get(user=user)
    user_details4 = Experience.objects.get(user=user)
    if user_details.status:
        return render(request, 'Dashboard/profile_res.html', {'user_details':user_details, 'user_details1':user_details1, 'user_details2':user_details2, 'user_setails3': user_details3, 'user_details4': user_details4})
    else:
        if user != request.user:
            return redirect('not_found')

        else:
            return render(request, 'Dashboard/create_res.html')




@login_required(login_url='account_login')
def create_res(request):
    user=User.objects.get(username=request.user.username)
    user_details = Profile.objects.get(user=user)
    user_details1 = Skills.objects.get(user=user)
    user_details2 = Education.objects.get(user=user)
    user_details3 = Projects.objects.get(user=user)
    user_details4 = Experience.objects.get(user=user)






    if request.method == 'POST':



                if request.FILES.get('dp') == Profile.objects.get(user=user).dp:
                    pass
        
                elif request.FILES.get('dp'):
                    user_details.dp = request.FILES.get('dp')
                else:
                    user_details.dp = Profile.objects.get(user=user).dp

                




                user_details.first = request.POST.get('first')
                user_details.last = request.POST.get('last')
                user_details.status = request.POST.get('status')
                user_details.about = request.POST.get('about')
                user_details.mail = request.POST.get('mail')
                user_details.phone = request.POST.get('phone')
                user_details.address = request.POST.get('address')
                user_details.age = request.POST.get('age')
                user_details.facebook = request.POST.get('facebook')
                # twitter = request.POST.get('twitter'),
                user_details.instagram = request.POST.get('instagram')
                user_details.linkedin = request.POST.get('linkedin')
                user_details.yoursite = request.POST.get('yoursite')
                user_details.photo1 = request.FILES.get('photo1')
                user_details.photo2 = request.FILES.get('photo2')

        


        
                
                user_details1.skill1 = request.POST.get('skill1')
                user_details1.per1 = request.POST.get('per1')
                user_details1.skill2 = request.POST.get('skill2')
                user_details1.per2 = request.POST.get('per2')
                user_details1.skill3 = request.POST.get('skill3')
                user_details1.per3 = request.POST.get('per3')
                user_details1.skill4 = request.POST.get('skill4')
                user_details1.per4 = request.POST.get('per4')
                user_details1.skill5 = request.POST.get('skill5')
                user_details1.per5 = request.POST.get('per5')
                user_details1.skill6 = request.POST.get('skill6')
                user_details1.per6 = request.POST.get('per6')

             


        
            
                user_details2.course1 = request.POST.get('course1')
                user_details2.stream1 = request.POST.get('stream1')
                user_details2.university1 = request.POST.get('university1')
                user_details2.date1 = request.POST.get('edu_date1')
                user_details2.discription1 = request.POST.get('edu_discription1')
                user_details2.course2 = request.POST.get('course2')
                user_details2.stream2 = request.POST.get('stream2')
                user_details2.university2 = request.POST.get('university2')
                user_details2.date2 = request.POST.get('edu_date2')
                user_details2.discription2 = request.POST.get('edu_discription2')



        


        
            
                user_details3.name1 = request.POST.get('pro1')
                user_details3.date1 = request.POST.get('prodate1')
                user_details3.discription1 = request.POST.get('prodisc1')
                user_details3.name2 = request.POST.get('pro2')
                user_details3.date2 = request.POST.get('prodate2')
                user_details3.discription2 = request.POST.get('prodisc2')

        





        
            
                user_details4.name1 = request.POST.get('exp1')
                user_details4.date1 = request.POST.get('expdate1')
                user_details4.company1 = request.POST.get('expcom1')
                user_details4.salary1 = request.POST.get('expsal1')
                user_details4.discription1 = request.POST.get('expdisc1')
                user_details4.name2 = request.POST.get('exp2')
                user_details4.date2 = request.POST.get('expdate2')
                user_details4.company2 = request.POST.get('expcom2')
                user_details4.salary2 = request.POST.get('expsal2')
                user_details4.discription2 = request.POST.get('expdisc2')



        



                user_details.save()
                user_details1.save()
                user_details2.save()
                user_details3.save()
                user_details4.save()


                return redirect('view_res', id = user_details.id)
                # return render(request, 'Dashboard/profile_res.html', {'user_details':user_details, 'user_details1':user_details1, 'user_details2':user_details2, 'user_setails3': user_details3, 'user_details4': user_details4})
    else:
        return render(request, 'Dashboard/create_res.html', {'user_details':user_details})
    







@login_required(login_url='account_login')
def edit_profile(request):
    user=User.objects.get(username=request.user.username)
    user_details = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        
        
        user_details.first = request.POST.get('first')
        user_details.last = request.POST.get('last')
        user_details.phone = request.POST.get('phone')
        user_details.postal = request.POST.get('postal')
        user_details.city = request.POST.get('city')
        
        user_details.mail = request.POST.get('mail')
        user_details.city = request.POST.get('city')
        user_details.state = request.POST.get('state')
        user_details.country = request.POST.get('country')  
        user_details.about = request.POST.get('about')
        user_details.address = request.POST.get('address')
        if request.FILES.get('dp'):
            user_details.dp = request.FILES.get('dp')
        user_details.save()


        if user_details.status:
            return redirect('dashboard')
        else:
            return redirect('create_res')



        

    else:
        return render(request, 'Dashboard/edit_profile.html', {'user_details':user_details})

    


@login_required(login_url='account_login')
def create_com(request):
    user=User.objects.get(username=request.user.username)
    user_details = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        user_details.first = request.POST.get('first')
        user_details.last = request.POST.get('last')
        user_details.status = request.POST.get('status')
        user_details.phone = request.POST.get('phone')
        user_details.postal = request.POST.get('postal')
        user_details.city = request.POST.get('city')
        user_details.mail = request.POST.get('mail')
        user_details.city = request.POST.get('city')
        user_details.state = request.POST.get('state')
        user_details.country = request.POST.get('country')  
        user_details.about = request.POST.get('about')
        user_details.address = request.POST.get('address')
        user_details.yoursite = request.POST.get('yoursite')
        user_details.facebook = request.POST.get('facebook')
        user_details.twitter = request.POST.get('twittwr')
        user_details.instagram = request.POST.get('instagram')
        user_details.linkedin = request.POST.get('linkedin')
        if request.FILES.get('dp'):
            user_details.dp = request.FILES.get('dp')
        user_details.save()
        return redirect('dashboard')


    else:
        return render(request, 'Dashboard/create_com.html', {'user_details':user_details})

    










def list_job(request, categ=None,):

    if categ != None:
        categories = Categories.objects.all()
        pk = get_object_or_404(categories,slug=categ)
        jobs = Job.objects.filter(category=pk)
        


    else:
        categories = Categories.objects.all()
        jobs = Job.objects.all()

    cities = Job.objects.values_list('city', flat=True).distinct()
    p = Paginator(jobs, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')

    
        
    
    
    return render(request, 'Dashboard/job_list.html', {'categories':categories, 'jobs':page, 'cities':cities})




 







@login_required(login_url='account_login')
def job_details(request, categ=None, id=None, job=None):



    if categ == None and job == None and id==id:

        if  Job_applied.objects.filter(job_id = request.POST.get('job_id')):

            
            return redirect('youDone')







        else:


            
            applied = Job_applied(
                
                user = User.objects.get(username=request.user.username),
                job_applied = request.POST.get('job_name'),
                job_id = request.POST.get('job_id')
                

            )
            
            applied.save()


            msg = Message(

            user = User.objects.get(username = request.user.username),
            job ="You've applied for"+' '+Job.objects.get(id = request.POST.get('job_id')).name,
            company ="at"+' '+request.POST.get('company'),
            job_id = request.POST.get('job_id')


            )
            msg.save()

            
            msgs = Message(

            user = User.objects.get(username = Job.objects.get(id=request.POST.get('job_id')).company),
            job ="You've got one application for"+' '+Job.objects.get(id = request.POST.get('job_id')).name,
            company ="from"+' '+request.user.username,
            job_id = request.POST.get('job_id')


            )

            msgs.save()

            resume = Get_Res(
                
                
                
                user = User.objects.get(username=request.POST.get('company')),
                job_id =  request.POST.get('job_id'),
                seeker_name = request.user.username,
                resume = Profile.objects.get(user=User.objects.get(username=request.user.username)).id,
                status = Profile.objects.get(user=User.objects.get(username=request.user.username)).status,
                photo = Profile.objects.get(user=User.objects.get(username=request.user.username)).dp.url,
                experience = Profile.objects.get(user=User.objects.get(username=request.user.username)).experience
                
            )
            

            
            resume.save()
            return render(request, 'Dashboard/job_details.html', {'job':job, 'applied':applied})


    else:

        
        job = Job.objects.get(category__slug=categ, id=id, slug=job)

        

        if Job_applied.objects.filter(user=User.objects.get(username=request.user.username), job_id = id):
            applied = Job_applied.objects.get(job_id = id).job_id
            
        else:
            applied = None
        return render(request, 'Dashboard/job_details.html', {'job':job, 'applied':applied})
    









@login_required(login_url='account_login')
def job_posted(request):

    if request.method == 'POST':
        
        job_posted = Job.objects.filter(company=request.user.username, category = Categories.objects.get(category= request.POST.get('categ')))
        category = set()
        for items in Job.objects.filter(company=request.user.username):
            category.add(items.category)


    else:


        job_posted = Job.objects.filter(company=request.user.username)
        category = set()
        for items in Job.objects.filter(company=request.user.username):
            category.add(items.category)

        
    p = Paginator(job_posted, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')




    return render(request, 'JOB_POSTED/job_posted.html', {'job_post':page, 'categories':category})






@login_required(login_url='account_login')
def job_applied(request):


    if request.method =="POST":

 
        query = set()
        for items in  Job_applied.objects.filter(user = User.objects.get(username = request.user.username)):
            query.add(items.job_id)
        applied = Job.objects.filter(id__in =query, category = Categories.objects.get(category= request.POST.get('categ')))


        category = set()
        for items in Job.objects.filter(id__in =query):
            category.add(items.category)
        


    else:

    
        query = set()
        for items in  Job_applied.objects.filter(user = User.objects.get(username = request.user.username)):
            query.add(items.job_id)
        applied = Job.objects.filter(id__in =query)



        category = set()
        for items in Job.objects.filter(id__in =query):
            category.add(items.category)



    p = Paginator(applied, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')

    return render(request, 'JOB_APPLIED/applied.html', {'job_post':page, 'categories':category} ) 



@login_required(login_url='account_login')
def selected(request):
    if request.method == "POST":

    
        query = set()
        for items in  Message.objects.filter(user = User.objects.get(username = request.user.username), job__startswith = "You're Shortlisted for"):
            query.add(items.job_id)
        jobs = Job.objects.filter(id__in =query, category = Categories.objects.get(category= request.POST.get('categ')))

            

        category = set()
        for items in Job.objects.filter(id__in =query):
            category.add(items.category)


    else:

        query = set()
        for items in  Message.objects.filter(user = User.objects.get(username = request.user.username), job__startswith = "You're Shortlisted for"):
            query.add(items.job_id)
        jobs = Job.objects.filter(id__in =query)

            

        category = set()
        for items in Job.objects.filter(id__in =query):
            category.add(items.category)


    p = Paginator(jobs, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')





    return render(request, 'JOB_SELECTED/selected.html', {'job_post':page, 'categories':category} ) 




@login_required(login_url='account_login')
def not_selected(request):
    if request.method == "POST":

    
        query = set()
        for items in  Message.objects.filter(user = User.objects.get(username = request.user.username), job__startswith = "You're not selected for"):
            query.add(items.job_id)
        jobs = Job.objects.filter(id__in =query, category = Categories.objects.get(category= request.POST.get('categ')))

            

        category = set()
        for items in Job.objects.filter(id__in =query):
            category.add(items.category)


    else:

        query = set()
        for items in  Message.objects.filter(user = User.objects.get(username = request.user.username), job__startswith = "You're not selected for"):
            query.add(items.job_id)
        jobs = Job.objects.filter(id__in =query)

            

        category = set()
        for items in Job.objects.filter(id__in =query):
            category.add(items.category)


    p = Paginator(jobs, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')





    return render(request, 'JOB_NOT_SELECTED/not_selected.html', {'job_post':page, 'categories':category} ) 















@login_required(login_url='account_login')
def browse_res(request, job_id):

    if request.method == 'POST':
        


        msg = Message(

        user = User.objects.get(username = request.POST.get('seeker')),
        job ="You're Shortlisted for"+' '+Job.objects.get(id = job_id).name,
        company ="by"+' '+request.user.username,
        job_id = job_id


        )

        msg.save()

        shrtlst = Shortlisted(

            user = User.objects.get(username = request.user.username),
            job_id = job_id,
            resume = request.POST.get('resume'),
            seeker_name = request.POST.get('seeker')



        )

        shrtlst.save()
        
        send_mail(
            subject='You are ShortListed',
            message= f"Hello {request.POST.get('seeker')},\n\n\n You are You're Shortlisted for {Job.objects.get(id = job_id).name} by {request.user.username}\n\n\n\n Regards careerEnv",
            from_email = 'support.careerenv.com',
            recipient_list= [User.objects.get(username = request.POST.get('seeker')).email,]
        )
        
        res = Get_Res.objects.get(seeker_name = request.POST.get('seeker'), job_id = job_id, resume = request.POST.get('resume') )
        res.delete()
        browse_res = Get_Res.objects.filter(user = User.objects.get(username = request.user.username), job_id = job_id )
        job_name = Job.objects.get(id = job_id)
    else:
        job_id = job_id
        job_name = Job.objects.get(id = job_id)
        browse_res = Get_Res.objects.filter(user = User.objects.get(username = request.user.username), job_id = job_id )





    p = Paginator(browse_res, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')

    return render(request, 'JOB_POSTED/browse-resume.html', {'resumes':page, 'job_id':job_id, 'job_name':job_name})




@login_required(login_url='account_login')
def delete_res(request, job_id):
    
    

    res = Get_Res.objects.filter(seeker_name = request.POST.get('seeker'), job_id = job_id, resume = request.POST.get('resume') )
    res.delete()

    msg = Message(

        user = User.objects.get(username = request.POST.get('seeker')),
        job ="You're not selected for"+' '+Job.objects.get(id = job_id).name,
        company ="by"+' '+request.user.username,
        job_id = job_id


        )
    msg.save()
    send_mail(
            subject='You are Rejected',
            message= f"Hello {request.POST.get('seeker')},\n\n\n You are Your application for {Job.objects.get(id = job_id).name} was  Rejected by {request.user.username}\n\n\n\n Regards careerEnv",
            from_email = 'support.careerenv.com',
            recipient_list= [User.objects.get(username = request.POST.get('seeker')).email,]
        )
    job_id = job_id
    return redirect('browse_res', job_id)











@login_required(login_url='account_login')
def application(request):

    if request.method == 'POST':
        
        job_posted = Job.objects.filter(company=request.user.username, category = Categories.objects.get(category= request.POST.get('categ')))
        category = set()
        for items in Job.objects.filter(company=request.user.username):
            category.add(items.category)


    else:


        job_posted = Job.objects.filter(company=request.user.username)
        category = set()
        for items in Job.objects.filter(company=request.user.username):
            category.add(items.category)

        
    p = Paginator(job_posted, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')




    return render(request, 'JOB_POSTED/application.html', {'job_post':page, 'categories':category})










@login_required(login_url='account_login')
def short_listed(request):
    if request.method == 'POST':
        job = set()
        for items in Shortlisted.objects.filter(user=User.objects.get(username=request.user.username)):
            job.add(items.job_id)
        jobs = Job.objects.filter(id__in = job, category=Categories.objects.get(category= request.POST.get('categ')))

        
        category = set()
        for items in Shortlisted.objects.filter(user=User.objects.get(username=request.user.username)):
            category.add(items.job_id)
        categories = set()
        for items in Job.objects.filter(id__in = category):
            categories.add(items.category)


    else:
        job = set()
        for items in Shortlisted.objects.filter(user=User.objects.get(username=request.user.username)):
            job.add(items.job_id)
        jobs = Job.objects.filter(id__in = job)

        
        category = set()
        for items in Shortlisted.objects.filter(user=User.objects.get(username=request.user.username)):
            category.add(items.job_id)
        categories = set()
        for items in Job.objects.filter(id__in = category):
            categories.add(items.category)

        
    p = Paginator(jobs, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')




    return render(request, 'JOB_POSTED/shortlisted.html', {'job_post':page, 'categories':categories})



@login_required(login_url='account_login')
def shrtlstd_res(request, job_id):
    job_id = job_id
    job_name = Job.objects.get(id = job_id)
    browse_res = Shortlisted.objects.filter(user = User.objects.get(username = request.user.username), job_id = job_id )





    p = Paginator(browse_res, 2)
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        redirect('not_found')

    return render(request, 'JOB_POSTED/browse-resume.html', {'resumes':page, 'job_id':job_id, 'job_name':job_name})