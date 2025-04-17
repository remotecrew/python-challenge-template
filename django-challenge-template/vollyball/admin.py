from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Stadium, Match, Seat

admin.site.register(Stadium)
admin.site.register(Match)
admin.site.register(Seat)