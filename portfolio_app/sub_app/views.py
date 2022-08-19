from django.urls import path
from . import models
from django.shortcuts import render
from django.core.mail import send_mail
import requests
from django.http import JsonResponse,HttpResponse
import base64
import json
import random
import httpx
import re
#from django.core.files.storage import default_storage
#from io import BytesIO

def send_eamil(request):
	name=request.POST['name']
	email=request.POST['email']
	subject=request.POST['subject']
	message=request.POST['message']
	
	if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message):
		print("it's URL")
		return False
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


def demo_page(request):
	"just demo page to list all demos"
	return render(request, 'demo.html', {})


def nlp_demo(request):
	"""page for sentiment anaylis demo"""
	text=request.POST.get('textsentence', False)#MultiValueDictKey
	if text:
		sentiment=requests.get("https://brv3cigampej24dwf4xujkomhy0ewcwi.lambda-url.us-east-1.on.aws/{}".format(text))
		return JsonResponse(sentiment.json(),status=200)
		# return render(request, 'demo.html',sentiment.json())
	else:
		return render(request, 'demos/nlp.html',{})


def audio_demo(request):

	"""page for audio emotion anaylis demo"""

	if request.method=='POST':
		req=request.POST.get('data')
		d=req.split(",")[1]

	
		# file_content_io = BytesIO(base64.b64decode(d))
		# s3_path='audio/file_name_{}.ogg'.format(random.randint(0,99))
		# default_storage.save(s3_path, file_content_io)


		API_URL = "https://api-inference.huggingface.co/models/Talha/urdu-audio-emotions"
		headers = {"Authorization": "Bearer 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"}
		

		data=base64.b64decode(d)
		response = requests.post(API_URL, headers=headers, data=data)
		x=json.loads(response.content.decode("utf-8"))
		try:
			d={}
			for l in x:
				d.update({l['label']:round(l['score']*100)})
			return JsonResponse(d,safe=False)
		except Exception as e:
			print(x)
			return HttpResponse("Try again")

	else:
		return render(request, 'demos/audio.html',{})


def image_demo(request):
	
		return render(request, 'demos/image.html',{})