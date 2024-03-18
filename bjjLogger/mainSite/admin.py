from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from mainSite.models import Trening, Zawody, CompFight, MyUser


# Register your models on the admin site
admin.site.register(Trening)
admin.site.register(Zawody)
admin.site.register(CompFight)


class UserCreationForm(forms.ModelForm):
    # Creating new user form
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ["email", "username", "belt", "date_of_birth"]

    def clean_password2(self):
        # Check if the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # Form for updating user account
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ["email", "password", "date_of_birth", "username", "belt", "is_active", "is_admin"]


class UserAdmin(BaseUserAdmin):
    # Custom User Admin class
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["email", "username", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["date_of_birth", "username", "belt"]}),
        ("Permissions", {"fields": ["is_active", "is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "belt", "date_of_birth", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "username"]
    ordering = ["email", "username"]
    filter_horizontal = []

# Register the UserAdmin for the MyUser model
admin.site.register(MyUser, UserAdmin)

# Unregister the Group model from the admin (we don't need it for our custom user model)
#admin.site.unregister(Group)
