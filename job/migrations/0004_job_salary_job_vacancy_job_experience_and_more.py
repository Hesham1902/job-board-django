# Generated by Django 5.0.4 on 2024-04-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
