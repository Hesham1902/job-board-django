from django.shortcuts import render

from project import settings
from .models import Info

from django.core.mail import send_mail

# Create your views here.


def send_message(request):
    context = Info.objects.first()
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        email = request.POST.get("email")
        send_mail(
            subject,
            "[JOB-BOARD] You have a message from %s" % email,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        send_mail(
            subject,
            "Your message has been sent to %s thank you for contact with us"
            % settings.EMAIL_HOST_USER,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    return render(request, "contact/contact.html", {"my_info": context})
