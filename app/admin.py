from django.contrib import admin
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'phone')
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(Signup, SignupAdmin)