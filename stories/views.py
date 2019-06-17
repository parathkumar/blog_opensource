from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
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
    #rank = get_object_or_404(Rating,id = number)'rank' : Rating.objects.get(id=number)
    return render(request,"Details.html",{'blog' : stories.objects.get(id=number),})


def share_view(request):
    return render(request,"share.html",{})

def Home_View(request):
    return render(request,"Home.html",{})

class CreateBlog(TemplateView):
    TemplateName = 'create.html'
    def get(self,request):
        form = CreateForm()
        return render(request,self.TemplateName,{'form' : form})
    def post(self,request):
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            content = form.cleaned_data['content']
            return redirect('stories:CreateBlog_ref')


