from django.contrib import admin
from .models import Setting, Like, UserPhoto, Match, Dislike, Inbox, Profile

admin.site.register(Dislike)
admin.site.register(UserPhoto)
admin.site.register(Match)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Inbox)
admin.site.register(Setting)

# Register your models here.
