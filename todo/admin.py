from django.contrib import admin
from .models import Todo, Tag, User
# Register your models here.

admin.site.register(Todo)
admin.site.register(Tag)
admin.site.register(User)