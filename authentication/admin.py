from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication import models, forms

 # Register your models here.
class UserAdmin(BaseUserAdmin):
 # The forms to add and change user instances
 	add_form = forms.UserCreationForm
 	form = forms.UserChangeForm

 	# The custom user model we are going to use
 	model = models.User

admin.site.register(models.User, UserAdmin)
