from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'index.html',{})

def contact(request):
	if request.method == "POST":

		# post thank you info

		message_name    = request.POST['message_name']
		message_email   = request.POST['message_email']
		message_subject = request.POST['message_subject']
		message         = request.POST['message']
		message_thx  = 'Thank you! ' + message_name

		# send an email


		return render(request, 'contact.html',{'message_thx':message_thx})
	else:
		return render(request, 'contact.html',{})