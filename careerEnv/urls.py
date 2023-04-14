"""careerEnv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Main import views as Main_views
from Blog import views as Blog_views
from Dashboard import views as D_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('', Main_views.home, name='home'),
    path('job_list/all/', Main_views.job_list, name='job_list'),
    path('job_list/all/<slug:categ>/', Main_views.job_list, name='job_list'),
    
    path('job_details/<slug:categ>/<slug:job>/', Main_views.job_details, name='job_details'),
    path('view_res/<str:id>/', D_views.view_res, name='view_res'),
    path('page-not-found', Main_views.not_found, name='not_found'),
    path('you-Done/', Main_views.youDone, name='youDone'),
    path('blog/', Blog_views.blog, name='blog'),
    path('blog/<str:categ>/', Blog_views.blog, name='blog'),
    path('blog-content/<slug:categ>/<slug:blog>/', Blog_views.blog_details, name='blog_details'),
    path('job-seeker-registration/', Main_views.seeker_reg, name='seeker_reg'),
    path('employer-registration/', Main_views.employer_reg, name='employer_reg'),
    path('job-search/', Main_views.search, name="search")
    
]



if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 