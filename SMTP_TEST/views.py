
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse

def send_email(request):
    subject = "Django_SMTP_TEST"
    
    # 수신자
    to = settings.EMAIL_RECIPIENTS
    
    # 발신자
    from_email = settings.EMAIL_HOST_USER
    message = "SMTP Transfer Test"

    email = EmailMessage(subject=subject, body=message, to=to, from_email=from_email)
    email.send()

    return HttpResponse("Message Sent!")
