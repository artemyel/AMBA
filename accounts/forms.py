from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from django import forms
from registration.forms import RegistrationForm
from accounts.models import Profile
from main.models import Offer, CommunityProduct, Category


class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['title', 'description', 'short_description', 'price', 'meet_place']

        labels = {
            'title': 'Название объявления',
            'description': 'Описание объявления',
            'short_description': 'Краткое описание',
            'price': 'Цена',
            'meet_place': 'Место встречи',
        }


class CommunityProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория")

    class Meta:
        model = CommunityProduct
        fields = ['name', 'category']

        labels = {
            'name': 'Название прововаемого продукта',
        }


class MyCustomUserForm(RegistrationForm):
    username = forms.CharField(
        label='Имя пользователя',
    )
    email = forms.CharField(
        label='Email',
        error_messages={'blank': 'no data!'}
    )

    helper = FormHelper()
    helper.layout = Layout(
        Div('email', css_class='col-sm-12'),
        Div(
            Div('first_name', css_class="col-sm-6"),
            Div('last_name', css_class="col-sm-6"),
        ),
        Div(
            Div('password1', css_class='col-lg-6'),
            Div('password2', css_class='col-lg-6', ),
        ),
        Div('username', css_class='col-sm-12'),
        Div('city', css_class='col-sm-12'),
        Div('phone', css_class='col-sm-12'),
        Div('address', css_class='col-sm-12'),
        Div('birth_date', css_class='col-sm-12'),
        Div('gender', css_class='col-sm-12'),
        Div('info', css_class='col-sm-12'),
        Div('avatar', css_class='col-sm-12'),
        Div(
            Submit('submit', u'Зарегистрироваться', css_class='col-xs-12 btn btn-success'),
            css_class='col-sm-12 test_css',
        ),

    )

    class Meta:
        model = Profile
        fields = [
            Profile.USERNAME_FIELD,
            'email',
            'password1',
            'password2',
            'city',
            "username",
            'phone',
            'first_name',
            'last_name',
            'address',
            'gender',
            'birth_date',
            'info',
            'avatar'
        ]

        widgets = {
            'birth_date': forms.widgets.SelectDateWidget(
                years=range(2016, 1900, -1),
                attrs=({'style': 'width: 33%; display: inline-block'})
            )
        }
        labels = {
            'city': 'Город',
            'phone': 'Телефон',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'Адрес',
            'gender': 'Кто вы?',
            'birth_date': 'Дата рождения',
            'info': 'Дополнительная информация',
            'avatar': 'Аватар',

        }
