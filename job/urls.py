from django.urls import path
from . import views


urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("add", views.add_job, name="job_add"),
    path("<str:slug>", views.job_detail, name="job_detail"),
]
