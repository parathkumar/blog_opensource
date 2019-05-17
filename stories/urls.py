from .views import stories_view
from .views import share_view
from .views import blog_number
from django.urls import path
from django.conf.urls import url
urlpatterns = [
    path('', stories_view , name = "stories_ref"),
    path('share/',share_view, name = "share_ref"),
    path('<int:number>',blog_number, name = "blog_number_ref")
]
