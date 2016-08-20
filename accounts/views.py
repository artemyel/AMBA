from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth import logout
from .models import Profile
from .forms import OfferForm, CommunityProductForm


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
    if request.user.is_authenticated:
        if request.method == 'POST':
            offer_form = OfferForm(request.POST)
            community_product_form = CommunityProductForm(request.POST)
            if offer_form.is_valid() and community_product_form.is_valid():
                new_offer = offer_form.save(commit=False)
                new_offer.user = request.user
                new_offer.product = community_product_form.save()
                new_offer.save()
                new_community_product = community_product_form.save(commit=False)
                new_community_product.save()
                return redirect('/main/')
            else:
                pass
                # TODO невалидная форма
        else:

            offer_form = OfferForm()
            community_product_form = CommunityProductForm()
            return render(request, 'accounts/addoffer.html', {
                'offer_form': offer_form,
                'community_product_form': community_product_form,
            })
    else:
        return redirect('/main/')
        # TODO предложить войти или зарегестрироваться
