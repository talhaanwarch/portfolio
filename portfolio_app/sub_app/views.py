from django.urls import path
from . import models
from django.shortcuts import render
from django.core.mail import send_mail


def send_eamil(request):
	name=request.POST['name']
	email=request.POST['email']
	subject=request.POST['subject']
	message=request.POST['message']
	send_mail(
			subject=subject,
			message=name +'\n'+ message +'\n'+ email,
			from_email=email,
			recipient_list=['aiengr.talha@gmail.com'],
			fail_silently=False,
		)

def home(request):
	posts = models.Post.objects.all()[:3]
	if request.method=='POST':
		send_eamil(request)
		return render(request,'index.html',{'context':posts,'mail_msg':'Email received'})

	return render(request,'index.html',{'context':posts})

def blog_page(request):
	posts = models.Post.objects.all()
	# print(posts.values_list('slug', flat=True))
	return render(request,'blog.html',{'context':posts})
	
def single_post(request, slug):
    post = models.Post.objects.get(slug=slug)
    return render(request, 'post.html', {'context': post})


def demo_page(request):
    return render(request, 'demo.html', {'context': 'post'})

# def contact(request):
# 	if request.method=='POST':
# 		print(request)
# 	return render(request,'index.html',{})
		# name=
		# email=
		# subject=
		# message=