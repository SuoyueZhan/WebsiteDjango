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
		# send_mail(
		# 	message_subject + 'from' + message_name, # subject and name
		# 	message, # message
		# 	message_email, # from email
		# 	['zhan114@uwindsor.ca'], # to email
		# 	)

		return render(request, 'contact.html',{'message_thx':message_thx})
	else:
		return render(request, 'contact.html',{})

def research(request):
	return render(request, 'research.html',{})

def resume(request):
	return render(request, 'resume.html',{})