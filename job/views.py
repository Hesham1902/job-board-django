import json
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from job.models import Job
from django.core.paginator import Paginator
from .forms import JobForm, ApplicationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "job/job_list.html", {"jobs": page_obj, "count": jobs.count})


def job_detail(request, slug):
    try:
        job = Job.objects.get(slug=slug)
    except Job.DoesNotExist:
        raise Http404("Job not found")

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
    else:
        form = ApplicationForm()

    return render(request, "job/job_detail.html", {"job": job, "form": form})


@login_required
def add_job(request):

    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse("jobs:job_list"))
    else:
        form = JobForm()

    return render(request, "job/add_job.html", {"form": form})


