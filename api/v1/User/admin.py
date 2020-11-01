from django import forms

from .models import Users, Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rest_framework import permissions
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django_registration.forms import RegistrationForm


# from .models import MyUser

#
# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = MyUser
#         fields = ('email', 'date_of_birth')
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = MyUser
#         fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin', 'university_id')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]
#
#
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'date_of_birth', 'is_admin', 'university_id')
#     list_filter = ('is_admin', 'university_id')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('date_of_birth',)}),
#         ('Permissions', {'fields': ('is_admin', 'university_id')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'date_of_birth', 'password1', 'password2', 'university_id'),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()

# def get_queryset(self, request):
#     qs = super().get_queryset(request)
#     if request.user.is_superuser:
#         user = MyUser.university_id
#         return qs.filter(BookAdmin.get_queryset(request.user.id))


# class MyModelAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             # return qs
#             return qs.filter(BookAdmin.get_queryset(BookAdmin,))


# Now register the new UserAdmin...

# admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('full_name', 'email', 'university_id', 'faculty')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


@admin.register(Profile)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm
    fieldsets = (
        ('Основные данные', {'fields': ('username', 'email', 'password', 'role')}),
        ('Персональные данные', {'fields': ('full_name',
                                            'university_id', 'faculty', 'group_name','avatar', 'kafedra', 'position',
                                            'passport_serial_id','tel_num',)}),
        ('Уровень доступа', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': ('username', 'full_name', 'university_id', 'email', 'faculty', 'password1', 'password2',
                       'group_name','avatar', 'kafedra', 'position','passport_serial_id','tel_num',),
        }),
    )
    list_display = ('username', 'is_staff', 'date_joined', 'university_id','role',)
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('username',)

# @admin.register(Profile)
# class UserAdmin(BaseUserAdmin):
#     pass


# admin.site.register(User, UserAdmin)

# Register your models here.
# admin.site.register(MyUser, UserAdmin)
# admin.site.register(Users)
# admin.site.register(Profile, UserAdmin)
