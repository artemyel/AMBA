from django.shortcuts import render, redirect
from .forms import LogginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = LogginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/index.html', {'user': user})


    else:
        if request.user.is_authenticated:
            return render(request, 'main/index.html', {'user': request.user})
        else:
            form = LogginForm()
            return render(request, 'main/index.html', {'user_form': form})



def logout_view(request):
    logout(request)
    return redirect('/main/')
