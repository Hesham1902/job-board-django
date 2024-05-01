from django.http import JsonResponse, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from .models import Profile
from django.contrib.auth.decorators import login_required
from job.models import Application, Job
from django.shortcuts import get_object_or_404

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
            else:
                raise PermissionError("Invalid signing up, Try again later!")
            return redirect("/accounts/profile")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse("accounts:profile"))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/profile_edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


@login_required
def my_jobs(request):
    # jobs = Job.objects.filter(owner=request.user.id)
    jobs = request.user.posted_jobs.all()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # job_data = list(jobs.values())  # Convert QuerySet to list of dictionaries
    # return JsonResponse(job_data, safe=False)
    return render(
        request, "accounts/my_posted_jobs.html", {"jobs": page_obj, "count": jobs.count}
    )


@login_required
def my_job_applications(request, jobId):
    try:
        job = get_object_or_404(Job, id=jobId)
    except:
        raise Http404("Job not found")
    print(job.owner)
    print(request.user)
    if request.user == job.owner:
        applications = Application.objects.filter(job_id=jobId)
        applicatons_data = list(applications.values())
        # print(jobId)
        # print(applications)
        return JsonResponse(applicatons_data, safe=False)
    else:
        return JsonResponse({"error": "Unauthorized access"}, status=403)
