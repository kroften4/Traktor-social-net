from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)

# TODO: generate an actual flag later
admin.site.site_header = 'Congrats! flag{asdfyao8wefga8734yr2ykr783rgk84384tg}'
