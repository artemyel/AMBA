from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import datetime
from django.utils import timezone

class ProfileManager(BaseUserManager):
    def create_user(self, email, city, username, phone, first_name, last_name, address, gender, birth_date, info,
                    avatar, rating, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            city=city,
            username=username,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            address=address,
            gender=gender,
            birth_date=birth_date,
            info=info,
            avatar=avatar,
            rating=rating,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, city, username, phone, first_name, last_name, address, gender, birth_date, info,
                         avatar, rating, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            city=city,
            username=username,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            address=address,
            gender=gender,
            birth_date=birth_date,
            info=info,
            avatar=avatar,
            rating=rating
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages={
            'blank': 'invalid',
            'uniqueness': "invalid",
        },
    )
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)

    MAN = 1
    WOMAN = 2
    GENDER_CHOICE = (
        (MAN, 'Мужчина'),
        (WOMAN, 'Женщина'),
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=MAN)
    # gender = models.BooleanField(null=False)
    birth_date = models.DateField(null=False)
    info = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars', null=True)
    rating = models.SmallIntegerField(default=0)

    object = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'city',
        'phone',
        'first_name',
        'last_name',
        'address',
        'gender',
        'birth_date',
        'info',
        'avatar',
        'rating',
    ]

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
