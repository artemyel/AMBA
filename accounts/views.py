from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import logout
from .models import Profile
from .forms import OfferForm


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
            form = OfferForm(request.POST)
            if form.is_valid():
                new_offer = form.save(commit=False)
                new_offer.user = request.user
                new_offer.save()
                return redirect('/main/')
            else:
                pass
                # TODO невалидная форма
        else:
            form = OfferForm()
            return render(request, 'accounts/addoffer.html', {'offer_form': form})
    else:
        return redirect('/main/')
        # TODO предложить войти или зарегестрироваться
