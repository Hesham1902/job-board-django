from django.http import Http404
from django.shortcuts import render
from job.models import Job

# Create your views here.

def job_list(request):
    jobs = Job.objects.all()
    for job in jobs:
        print(job)
    return render(request,'job/job_list.html',{"jobs": jobs})


def job_detail(request, id):
    try: 
        job = Job.objects.get(pk=id)
    except Job.DoesNotExist:
        raise Http404('Job not found')
    return render(request,'job/job_detail.html',{"job": job})
