from .views import stories_view
from .views import share_view
from .views import blog_number
from django.urls import path
from .views import CreateBlog
from django.conf.urls import url
app_name = 'stories'
urlpatterns = [
    path('', stories_view , name = "stories_home_ref"),
    path('share/',share_view, name = "share_ref"),
    path('<int:number>',blog_number, name = "blog_number_ref"),
    path('create/',CreateBlog,name = "CreateBlog_ref")
]