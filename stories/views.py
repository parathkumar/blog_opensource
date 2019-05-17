from django.shortcuts import render
from .models import stories
# Create your views here.
from django.http import HttpResponse
def stories_view(request):

    return render(request,"stories.html",{})
def blog_number(request,number):
    return HttpResponse("<h1> the blog number is "+str(number)+"<h2>")
def share_view(request):
    return render(request,"share.html",{})
def Home_View(request):
    html=''
    for i in stories.objects.all():
        html+='<a href="/stories/'+str(i.id)+'">'+i.title+'</a><br>'
    return HttpResponse(html)
