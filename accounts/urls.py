from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("myjobs", views.my_jobs, name="my_posted_jobs"),
    path("proflile/edit/", views.profile_edit, name="profile_edit"),
    path(
        "<int:jobId>/applications",
        views.my_job_applications,
        name="my_posted_job_applications",
    ),
]
