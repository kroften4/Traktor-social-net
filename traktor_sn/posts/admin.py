from django.contrib import admin
from .models import Post
import flag

# Register your models here.

admin.site.register(Post)

admin.site.index_title = "CONGRATS! Here's your flag{" + flag.get_flag() + "}"
