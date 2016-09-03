from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LogginForm, QueryForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from main.models import Category, Offer, OfferImage, CommunityProduct, Product, Parameter, ParameterValue, \
    ParameterFilter
from django.views.generic import ListView
import json
import re


# TODO пофиксить/добавить else к if
def index(request):
    if request.method == 'POST':
        form = LogginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/index.html', {'user': user, 'categories': Category.objects.filter()})
    # TODO отделить log_in view от main view
    else:
        if request.user.is_authenticated:
            return render(request, 'main/index.html', {'user': request.user, 'categories': Category.objects.filter()})
        else:
            form = LogginForm()
            return render(request, 'main/index.html', {'user_form': form, 'categories': Category.objects.filter()})


class CategoryView(ListView):
    model = Offer
    context_object_name = 'offers'
    template_name = 'main/offers.html'
    paginate_by = 12

    def get_queryset(self):
        category = self.kwargs['category_name']
        self.form = QueryForm(self.request.GET, category=Category.objects.get(short_name=category))
        qs = []
        products = Product.objects.filter(category=Category.objects.get(short_name=category))
        if self.form.is_valid():  # valid
            offers = Offer.objects.filter(product__category__short_name=category)
            for field in self.form.cleaned_data:
                if self.form.cleaned_data[field]:
                    filter = ParameterFilter.objects.get(id=field[7:])
                    if filter.data_type == ParameterFilter.CHECKBOX:
                        db_qs = Q()
                        for p in self.form.cleaned_data[field]: # string parameter
                            # name = ParameterValue.objects.filter(parameter=filter.parameter)[0].value
                            db_qs.add(Q(['value__icontains', p]), 'OR')
                        parameter = ParameterValue.objects.filter(db_qs, parameter=filter.parameter)
                        offers = offers.filter(product_id__in=parameter.values('product_id'))
                    elif filter.data_type == ParameterFilter.BOOLEAN:
                        parameter = ParameterValue.objects.filter(parameter=filter.parameter, value='Yes')
                        offers = offers.filter(product_id__in=parameter.values('product_id'))
            for offer in offers:
                qs.append(offer)

        else:
            for product in products:
                try:
                    qs.append(Offer.objects.get(product=product))
                except Offer.DoesNotExist:
                    pass
        return qs

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        self.form = QueryForm(self.request.GET, category=Category.objects.get(short_name=self.kwargs['category_name']))
        context['form'] = self.form
        context['image_list'] = OfferImage.objects.all()
        context['categories'] = Category.objects.filter()
        context['category'] = Category.objects.get(short_name=self.kwargs['category_name']).name
        return context

    def get(self, request, *args, **kwargs):
        category = self.kwargs['category_name']
        if not Category.objects.filter(short_name=category):
            return redirect('/main/')
        else:
            return super(CategoryView, self).get(request, *args, **kwargs)


def offer_view(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    offer_image_list = OfferImage.objects.filter(offer=offer.pk)
    return render(request, 'offer/offer.html', {
        'offer': offer,
        'offer_image_list': offer_image_list,
    })


def test_ajax(request):
    if request.is_ajax():
        query = re.sub(r'\s+', ' ', request.GET['q'])
        data = []
        #items = Product.objects.filter(name__icontains=request.GET['q'])
        lq = query.split(' ')
        qs = Q()
        for i in lq:
            qs.add(Q(['name__icontains', i]), 'AND')
        sq = Product.objects.filter(qs)
        for item in sq:
            parameters = ParameterValue.objects.filter(product=item)
            param = []
            for parameter in parameters:
                param.append({'name': parameter.parameter.name, 'value': parameter.value})
            data.append({'id': item.pk, 'name': item.name, 'parameters': param})
        data = {'items': data}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")