from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class ProfileManager(BaseUserManager):
    def create_user(self, email, city, MyUsername, phone, first_name, last_name, address, gender, birth_date, info,
                    avatar, rating, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            city=city,
            MyUsername=MyUsername,
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
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, city, MyUsername, phone, first_name, last_name, address, gender, birth_date, info,
                         avatar, rating, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            city=city,
            MyUsername=MyUsername,
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
    )
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    MyUsername = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    gender = models.BooleanField(null=False)
    birth_date = models.DateField(null=False)
    info = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars', null=True)
    rating = models.SmallIntegerField(default=0)

    object = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'MyUsername',
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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
