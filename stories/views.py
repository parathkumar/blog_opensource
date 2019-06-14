from django.shortcuts import render,get_object_or_404
from .models import stories,Rating
# Create your views here.
#from django.http import HttpResponse,Http404
from forms import CreateForm
def stories_view(request):
    allblogs = stories.objects.all()
    context = {'allblogs': allblogs}
    return render(request, "stories.html", context)

def blog_number(request,number):

    blog = get_object_or_404(stories, id = number)
    rank = get_object_or_404(Rating,id = number)
    return render(request,"Details.html",{'blog' : stories.objects.get(id=number),'rank' : Rating.objects.get(id=number)})


def share_view(request):
    return render(request,"share.html",{})

def Home_View(request):
    return render(request,"Home.html",{})

def CreateBlog(request):
    form = CreateForm()
    return render(request,"create.html",{'form' : form})