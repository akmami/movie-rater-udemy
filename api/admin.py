from django.contrib import admin
from .models import Movie, Rating

# Register your models here.
# Will be visible in admin page
admin.site.register(Movie)
admin.site.register(Rating)