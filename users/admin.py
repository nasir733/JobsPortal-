from django.contrib import admin
from users.models import User,UserDeviceInfo

# Register your models here.
admin.site.register(User)
admin.site.register(UserDeviceInfo)
