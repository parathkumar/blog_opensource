from django.contrib import admin

# Register your models here.
from .models import stories
from .models import Rating

admin.site.register(stories)
admin.site.register(Rating)