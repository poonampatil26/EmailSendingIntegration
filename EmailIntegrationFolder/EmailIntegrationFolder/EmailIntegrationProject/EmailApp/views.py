from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def sendEmailView(request):
    print('in sendEmailView')
    send_mail(
        'Django Email Sending Demo',
        'This is my message, it worked.',
        'poonamnilpatil1912@gmail.com',
        ['nileshpatil4545@gmail.com'],
        fail_silently= False,
    )
    return HttpResponse('Mail sent')
