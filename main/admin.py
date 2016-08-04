from django.contrib import admin

from .models import Category, Parameter, Product, ParameterValue, Lot, LotImages

admin.site.register(Category)
admin.site.register(Parameter)
admin.site.register(Product)
admin.site.register(ParameterValue)
admin.site.register(Lot)
admin.site.register(LotImages)
