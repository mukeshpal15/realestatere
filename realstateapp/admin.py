from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(myaccount)
admin.site.register(user_account)
admin.site.register(agent_account)
admin.site.register(blog_table)
admin.site.register(OrderData)
admin.site.register(CartData)
admin.site.register(PropertyData)
admin.site.register(PropertyImagesData)