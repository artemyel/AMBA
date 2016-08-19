from django.contrib import admin

from .models import Category, Parameter, Product, ParameterValue, Offer, OfferImage

admin.site.register(Category)
admin.site.register(Parameter)
admin.site.register(Product)
admin.site.register(ParameterValue)
admin.site.register(Offer)
admin.site.register(OfferImage)
