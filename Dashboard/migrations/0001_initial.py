# Generated by Django 4.1.3 on 2022-12-29 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(blank=True, max_length=100)),
                ('per1', models.IntegerField(blank=True, default=50)),
                ('skill2', models.CharField(blank=True, max_length=100)),
                ('per2', models.IntegerField(blank=True, default=50)),
                ('skill3', models.CharField(blank=True, max_length=100)),
                ('per3', models.IntegerField(blank=True, default=50)),
                ('skill4', models.CharField(blank=True, max_length=100)),
                ('per4', models.IntegerField(blank=True, default=50)),
                ('skill5', models.CharField(blank=True, max_length=100)),
                ('per5', models.IntegerField(blank=True, default=50)),
                ('skill6', models.CharField(blank=True, max_length=100)),
                ('per6', models.IntegerField(blank=True, default=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shortlisted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.CharField(max_length=100, null=True)),
                ('job_id', models.CharField(max_length=100, null=True)),
                ('seeker_name', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['seeker_name'],
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, max_length=100, null=True)),
                ('date1', models.CharField(blank=True, max_length=100, null=True)),
                ('discription1', models.CharField(blank=True, max_length=1000, null=True)),
                ('name2', models.CharField(blank=True, max_length=100, null=True)),
                ('date2', models.CharField(blank=True, max_length=100, null=True)),
                ('discription2', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('experience', models.CharField(blank=True, max_length=20, null=True)),
                ('first', models.CharField(blank=True, max_length=100, null=True)),
                ('last', models.CharField(blank=True, max_length=100, null=True)),
                ('dp', models.ImageField(default='default.jpg', upload_to='profilePic')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('about', models.CharField(blank=True, max_length=10000, null=True)),
                ('age', models.CharField(blank=True, max_length=2, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
                ('postal', models.CharField(blank=True, max_length=8, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('yoursite', models.CharField(blank=True, max_length=100, null=True)),
                ('photo1', models.ImageField(blank=True, upload_to='images')),
                ('photo2', models.ImageField(blank=True, upload_to='images')),
                ('is_company', models.BooleanField()),
                ('ceo', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_no', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('job_id', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['job'],
            },
        ),
        migrations.CreateModel(
            name='Job_applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_applied', models.CharField(max_length=100, null=True)),
                ('job_id', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['job_applied'],
            },
        ),
        migrations.CreateModel(
            name='Get_Res',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=100, null=True)),
                ('seeker_name', models.CharField(max_length=100, null=True)),
                ('resume', models.CharField(max_length=100, null=True)),
                ('photo', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['seeker_name'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, max_length=100, null=True)),
                ('date1', models.CharField(blank=True, max_length=100, null=True)),
                ('discription1', models.CharField(blank=True, max_length=1000, null=True)),
                ('company1', models.CharField(blank=True, max_length=100, null=True)),
                ('name2', models.CharField(blank=True, max_length=100, null=True)),
                ('date2', models.CharField(blank=True, max_length=100, null=True)),
                ('discription2', models.CharField(blank=True, max_length=1000, null=True)),
                ('company2', models.CharField(blank=True, max_length=100, null=True)),
                ('salary1', models.CharField(blank=True, max_length=100, null=True)),
                ('salary2', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course1', models.CharField(blank=True, max_length=100, null=True)),
                ('stream1', models.CharField(blank=True, max_length=100, null=True)),
                ('university1', models.CharField(blank=True, max_length=100, null=True)),
                ('date1', models.CharField(blank=True, default=0, max_length=100)),
                ('discription1', models.CharField(blank=True, max_length=1000, null=True)),
                ('course2', models.CharField(blank=True, max_length=100, null=True)),
                ('stream2', models.CharField(blank=True, max_length=100, null=True)),
                ('university2', models.CharField(blank=True, max_length=100, null=True)),
                ('date2', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('discription2', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]