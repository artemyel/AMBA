from django.shortcuts import render
from .forms import LogginForm, QueryForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from main.models import Category, Offer
from django.views.generic import ListView


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
    if Category.objects.filter(short_name=category_name):
        return HttpResponse(category_name)
    else:
        return HttpResponse("NO SUCH CATEGORY ")


class CategoryView(ListView):
    model = Offer
    context_object_name = 'offers'
    template_name = 'main/offers.html'
    paginate_by = 2
    form = QueryForm()

    def get_queryset(self):
        self.form = QueryForm(self.request.GET)
        if self.form.is_valid():
            qs = Offer.objects.filter(price__lt=self.form.cleaned_data['price']).order_by()
        else:
            qs = Offer.objects.filter().order_by()
        if not self.request.user.is_authenticated():
            return qs.exclude()
        return qs

    def get_context_data(self, **kwargs):
        ctx = super(CategoryView, self).get_context_data(**kwargs)
        ctx['form'] = self.form
        ctx['qa'] = self.queryset
        return ctx


