from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def send_test_mail(request):
    subject = "hai welcome to django email configuration session"
    message = "this is the test email sent using django"
    from_email = 'test@gmail.com'
    recipient_list = ['arathi.ams@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('test mail successfully')

# def index(request):
#     if request.method == 'POST':
#         message = request.POST['message']
#         email = request.POST['email']
#         name = request.POST['name']
#         send_mail(
#             'Contact form',#title
#             message, #message
#             'settings.EMAIL_HOST_USER', #sender if not available
#             ['arathi.ams@gmail.com'], #receiver mail
#             fail_silently=False)
#     return render(request,'index.html')
#

