from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        subject = request.POST['subject']
        message = request.POST['message']
        
        send_mail(
            subject,
            message,
            mail,
            ['osarobovictors@gmail.com'],
            fail_silently=False
        )
        
        return render(request, 'index.html', {'name':name})
    else: 
        return render(request, 'index.html', {})