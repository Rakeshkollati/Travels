from django.shortcuts import render,redirect
from django.http import HttpResponse
from ApTravels import settings
from Myway.forms import UsReg
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def home(request):
	return render(request,'html/home.html')

	
def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def bookticket(request):
	return render(request,'html/bookticket.html')

def register(request):
	if request.method == "POST":
		t = UsReg(request.POST)
		if t.is_valid():
			user=t.save()
			messages.success(request,"User registered Successfully")
			#return redirect('/lg')
			adml = user.email
			pas = user.password
			msg = "Hi {} {}, your registeration is completed successfully your username is {} and password is {}. Don't share your passwords to any annoymous persons".format(user.first_name,user.last_name,user.username,user.password)
			sub = "Mail from Indian Travels"
			sd = settings.EMAIL_HOST_USER
			to = send_mail(sub,msg,sd,[adml])
			if to == 1:
				return redirect('/login')
				messages.primary("A mail sent to your account don't share your password to anyone")
			messages.warning(request,'mail not sent')
		messages.error(request,'Registation failed')
	t = UsReg()
	return render(request,'html/register.html',{'y':t})