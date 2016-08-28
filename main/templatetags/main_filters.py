from django import template
from main.models import OfferImage

register = template.Library()


@register.filter(name='get_image_list_by_offer')
def get_image_list_by_offer(offerID):
    return OfferImage.objects.all().filter(offer=offerID)


@register.filter(name='get_main_image_by_offer')
def get_main_image_by_offer(offerID):
    return OfferImage.objects.all().filter(offer=offerID)[0]