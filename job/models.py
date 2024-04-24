from django.db import models

# Create your models here.

JOB_TYPE = (
('Full Time','Full Time'),
    ('Part Time','Part Time')
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    

    def __str__(self) -> str:
        return f'Need {self.Vacancy} {self.title} for {self.job_type} Job '