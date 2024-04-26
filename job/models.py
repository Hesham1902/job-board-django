from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE = (
('Full Time','Full Time'),
    ('Part Time','Part Time')
)

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extension)


class Job(models.Model):
    owner = models.ForeignKey(User,related_name='posted_jobs',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    categrory = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Need {self.Vacancy} {self.title} for {self.job_type} Job '
    

class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self): 
        return self.name
    

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letteer = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name