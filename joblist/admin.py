from django.contrib import admin
from joblist.models import User, Occupation, Userhasoccupation


admin.site.register(User)
admin.site.register(Occupation)
admin.site.register(Userhasoccupation)
