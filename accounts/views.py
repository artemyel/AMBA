from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth import logout
from .models import Profile
from main.models import OfferImage
from .forms import OfferForm, CommunityProductForm, ImageForm
from django.forms import *


# Create your views here.
def profile(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)

    return render(request, 'profile/user_profile.html', {
        'user_profile': user,
        'document_root': settings.MEDIA_URL,
    })


def logout_view(request):
    logout(request)
    return redirect('/main/')


def add_offer(request):
    ImageFormSet = modelformset_factory(OfferImage, form=ImageForm, extra=3)
    if request.user.is_authenticated:
        if request.method == 'POST':
            offer_form = OfferForm(request.POST)
            formset = ImageFormSet(request.POST, request.FILES,
                                   queryset=OfferImage.objects.none())
            community_product_form = CommunityProductForm(request.POST)
            if offer_form.is_valid() and community_product_form.is_valid() and formset.is_valid():
                new_offer = offer_form.save(commit=False)
                new_offer.user = request.user
                new_offer.product = community_product_form.save()
                new_offer.save()
                new_community_product = community_product_form.save(commit=False)
                new_community_product.save()
                for form in formset.cleaned_data:
                    if form:
                        image = form['image']
                        photo = OfferImage(offer=new_offer, image=image, is_main=False)
                        # TODO продумать работу is_main
                        photo.save()
                return redirect('/main/')
            else:
                pass
                # TODO невалидная форма
        else:
            formset = ImageFormSet(queryset=OfferImage.objects.none())
            offer_form = OfferForm()
            community_product_form = CommunityProductForm()
            return render(request, 'accounts/addoffer.html', {
                'offer_form': offer_form,
                'community_product_form': community_product_form,
                'formset': formset,
            })
    else:
        return redirect('/main/')
        # TODO предложить войти или зарегестрироваться


