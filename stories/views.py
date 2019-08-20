from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
from .models import stories,Rating
from django.core.mail import send_mail
from blogapp import settings
# Create your views here.
#from django.http import HttpResponse,Http404
from forms import CreateForm,SearchForm

def stories_view(request):
    allblogs = stories.objects.all()
    context = {'allblogs': allblogs}
    return render(request, "stories/stories.html", context)

def blog_number(request,number):

    blog = get_object_or_404(stories, id = number)
    #rank = get_object_or_404(Rating,id = number)'rank' : Rating.objects.get(id=number)
    return render(request,"stories/Details.html",{'blog' : stories.objects.get(id=number),})


def share_view(request):
    return render(request,"stories/share.html",{})

def Home_View(request):
    return render(request,"stories/Home.html",{})

class CreateBlog(TemplateView):
    TemplateName = 'stories/create.html'
    def get(self,request):
        form = CreateForm()
        return render(request,self.TemplateName,{'form' : form})
    def post(self,request):
        userinstance = stories(author = request.user)
        form = CreateForm(request.POST or None,request.FILES,instance = userinstance,)
        if form.is_valid():
            form.save(commit=True)
            title = form.cleaned_data['title']
            '''description = form.cleaned_data['description']
            content = form.cleaned_data['content']'''
            send_mail(subject="blog created!!",
                      message="congrats your post: "+title+" has been published successfully",
                      from_email="bloghost@yahoo.com",
                      recipient_list=[request.user.email],
                      fail_silently=False,
                      auth_user=settings.EMAIL_HOST_USER,
                      auth_password=settings.EMAIL_HOST_PASSWORD,
                      )
            return redirect('/stories/')
            #return redirect('stories:CreateBlog_ref')


