from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Profile


# Create your views here.
def profile(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)

    return render(request,'profile/user_profile.html', {
        'user': user,
    })