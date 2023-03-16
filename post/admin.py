from django.contrib import admin
from .models import *
from userApp.models import CustomUser
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Discussion)
admin.site.register(Notification)
admin.site.register(CustomUser)