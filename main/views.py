from django.shortcuts import render, get_object_or_404, get_list_or_404
from .forms import LogginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from main.models import Category, Offer, OfferImage


# TODO пофиксить/добавить else к if
def index(request):
    if request.method == 'POST':
        form = LogginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/index.html', {'user': user})
    # TODO отделить log_in view от main view
    else:
        if request.user.is_authenticated:
            return render(request, 'main/index.html', {'user': request.user})
        else:
            form = LogginForm()
            return render(request, 'main/index.html', {'user_form': form})


def category_view(request, category_name):
    categories_list = Category.objects.all()
    categories_list = [str(category).lower().replace(" ", "") for category in categories_list]
    output = ', '.join([c for c in categories_list])
    if category_name in categories_list:
        return HttpResponse(category_name)
    else:
        return HttpResponse("NO SUCH CATEGORY " + output)


def offer_view(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    offer_image_list = OfferImage.objects.filter(offer=offer.pk)
    return render(request, 'offer/offer.html', {
        'offer': offer,
        'offer_image_list': offer_image_list,
    })
