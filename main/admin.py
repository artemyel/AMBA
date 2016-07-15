from django.contrib import admin

from .models import Category, Parameter, Product, ParameterValue

admin.site.register(Category)
admin.site.register(Parameter)
admin.site.register(Product)
admin.site.register(ParameterValue)
