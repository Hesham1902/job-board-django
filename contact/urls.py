from django.urls import path
from . import views

urlpatterns = [path("send-meesage/", views.send_message, name="contact")]
