from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    data={'name':'nitin','location':'Mumbai'}
    return render(request,'index.html',data)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,mobile=mobile,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Sent..!')
    return render(request,'contact.html')
