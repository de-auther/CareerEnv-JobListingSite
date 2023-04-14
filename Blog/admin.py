from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Blog_category)
admin.site.register(Blog_main)
admin.site.register(Blog_comment)