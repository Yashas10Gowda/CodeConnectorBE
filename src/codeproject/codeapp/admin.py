from django.contrib import admin
from .models import USER,Developer,Experience,Education,Post
# Register your models here.
admin.site.register(USER)
admin.site.register(Developer)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Post)