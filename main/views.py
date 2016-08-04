from django.shortcuts import render, redirect
from .forms import LogginForm
from django.contrib.auth import authenticate, login


def index(request):
    if request.method == 'POST':
        form = LogginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.username, password=form.password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/index.html', {'user': user})
    else:
        form = LogginForm()
        return render(request, 'main/index.html', {'form': form})


