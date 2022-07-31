from django.urls import path
from . import models
from django.shortcuts import render
from django.core.mail import send_mail
import requests
from django.http import JsonResponse,HttpResponse

def send_eamil(request):
	name=request.POST['name']
	email=request.POST['email']
	subject=request.POST['subject']
	message=request.POST['message']
	if (len(name)>3 and len(email)>8 and len(subject)>5 and len(message) >25):
		send_mail(
				subject=subject,
				message=name +'\n'+ message +'\n'+ email,
				from_email=email,
				recipient_list=['aiengr.talha@gmail.com'],
				fail_silently=False,
			)
		return True
	else:
		return False
def home(request):
	posts = models.Post.objects.all()[:3]
	papers = models.Papers.objects.all()
	if request.method=='POST':
		bools=send_eamil(request)
		if bools:
			return HttpResponse('Email Sent!')
		else:
			return HttpResponse('Email Not Sent!')

	return render(request,'index.html',{'blogs':posts,"papers":papers})

def blog_page(request):
	posts = models.Post.objects.all()
	# print(posts.values_list('slug', flat=True))
	return render(request,'blog.html',{'context':posts})
	
def single_post(request, slug):
	post = models.Post.objects.get(slug=slug)
	return render(request, 'post.html', {'context': post})


def nlp_demo(request):
	text=request.POST.get('textsentence', False)#MultiValueDictKey
	if text:
		sentiment=requests.get("https://brv3cigampej24dwf4xujkomhy0ewcwi.lambda-url.us-east-1.on.aws/{}".format(text))
		return JsonResponse(sentiment.json(),status=200)
		# return render(request, 'demo.html',sentiment.json())
	else:
		return render(request, 'demo.html',{})
