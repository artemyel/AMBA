from django.db import models
from user_registration.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    option_name = models.CharField(max_length=200, default="")
    tag_line = models.CharField(max_length=200, default="")
    SKU = models.SmallIntegerField()
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ParameterValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.parameter


class Lot(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    short_description = models.CharField(max_length=255, null=True)
    price = models.SmallIntegerField()
    meet_place = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class LotImages(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='LotImages/')
    is_main = models.BooleanField(null=False)

    def __str__(self):
        return self.image



