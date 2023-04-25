from django.contrib import admin
from .models import Resume, Experience, Template,User

# Register your models here.

admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Template)
admin.site.register(User)