from django.core.validators import RegexValidator
from django.db import models

from api.v1.University.models import University, Faculty
# from Order.models import BookInUse
from django.contrib.auth.models import (
    AbstractUser)


# Create your models here.

class Profile(AbstractUser):
    ROLE_CHOICES = (
        ("S", "Student"),
        ("T", "Teacher"),
        ("L", "Librarian"),
    )
    # username = None
    email = models.EmailField(unique=True, null=True, blank=True)
    role = models.TextField(choices=ROLE_CHOICES)
    full_name = models.TextField(verbose_name='ФИО')
    avatar = models.ImageField(verbose_name='Аватар', upload_to='img/users', null=True, blank=True)
    university_id = models.ForeignKey(University, on_delete=models.PROTECT, related_name='Университет')
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name='Факультет', null=True)
    group_name = models.TextField(verbose_name='Номер группы', null=True, blank=True)
    course = models.PositiveSmallIntegerField(verbose_name='Курс', null=True, blank=True)
    application_id = models.CharField(verbose_name="ID пользователя в другом приложении", null=True, blank=True,
                                      help_text="ID пользовалтеля для интеграции с Autolib", max_length=36)
    passport_serial_id = models.CharField(max_length=9, verbose_name='Серийный номер пасспорта', blank=True, null=True)
    tel_num = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name='Номер телефона',
                               null=True, blank=True)
    kafedra = models.TextField(verbose_name='Кафедра', null=True, blank=True)
    position = models.TextField(verbose_name='Должность', null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role', 'full_name', 'university_id']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return "{}".format(self.username)


class Users(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="profile")
    logo = models.ImageField(name="Аватар", upload_to='img/users')
    birth_date = models.DateField(null=True, blank=True)
    qr_number = models.CharField(max_length=16)

    # university = models.ForeignKey('University.University', on_delete=models.PROTECT, related_name='Университет')
    # USERNAME_FIELD = 'full_name'

    # reading_books = models.ManyToManyField(Book, name='Полученные книги')

    # used_books = models.ManyToManyField(Book, name='Сданные книги', default='')
    # time_of_get_book = models.ManyToManyField(BookInUse)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user.full_name

    def __unicode__(self):
        return self.user.full_name

#
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             date_of_birth=date_of_birth,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             date_of_birth=date_of_birth,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField()
#     is_superuser = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     university_id = models.ForeignKey('User.User', on_delete=models.PROTECT, related_name='Университет')
#     objects = MyUserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth', 'university_id', ]
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin

#
