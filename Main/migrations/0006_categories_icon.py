# Generated by Django 4.1.3 on 2023-02-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_rename_location_job_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='icon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
