from django.contrib import admin
from .models import Welcome


class MemberAdmin(admin.ModelAdmin):
  list_display = ("name", "age",)
  
admin.site.register(Welcome, MemberAdmin)
