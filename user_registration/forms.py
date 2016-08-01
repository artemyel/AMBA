from registration.forms import RegistrationForm

from user_registration.models import Profile


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = Profile
        fields = [
            Profile.USERNAME_FIELD,
            'email',
            'password1',
            'password2',
            'city',
            'username',
            'phone',
            'first_name',
            'last_name',
            'address',
            'gender',
            'birth_date',
            'info',
        ]
