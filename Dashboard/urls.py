from django.urls import path
from . import views




urlpatterns =[

    path('', views.dashboard, name='dashboard'),
    path('create_job/',views.create_job, name='create_job'),
    path('create_res/', views.create_res, name='create_res'),
    # path('/view_res/<str:id>/', views.view_res, name='view_res'),
    path('create-profile/', views.edit_profile, name='edit_profile'),
    path('create-company/', views.create_com, name='create_com'),
    path('list_job/', views.list_job, name='list_job'),
    path('list_job/<slug:categ>', views.list_job, name = 'list_job'),


    path('job_details/', views.job_details,name='job_details'),


    path('job_details/<slug:categ>/<slug:job>/<str:id>/', views.job_details, name='job_details'),

    path('job_posted/', views.job_posted, name='job_posted'),
    path('get_resume/<str:job_id>/', views.browse_res, name='browse_res'),
    path('shrtlstd/<str:job_id>/', views.shrtlstd_res, name='shrtlstd_res'),
    path('delete_resume/<str:job_id>/', views.delete_res, name='delete_res'),
    path('applied-jobs/', views.job_applied, name='job_applied'),
    path('selected/', views.selected, name='selected'),
    path('not-selected/', views.not_selected, name='not_selected'),
    path('applications/', views.application, name='application'),
    path('applications/short-listed/', views.short_listed, name='shortlisted'),
    




]