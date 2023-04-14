from django.contrib import admin
from Main.models import Categories, Job

# Register your models here.


class CategAd(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['category']}
admin.site.register(Categories, CategAd)



admin.site.register(Job)