from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserChangeForm, MyUserCreationForm

MyCustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyCustomUser
    list_display = ['email', 'username']


admin.site.register(MyCustomUser, CustomUserAdmin)
