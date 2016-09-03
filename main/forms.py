from django import forms
from main.models import ParameterFilter, ParameterValue

class LogginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class QueryForm(forms.Form):
    # cb = forms.MultipleChoiceField(choices=((1, 'a'), (2, 'b')), widget=widgets.CheckboxSelectMultiple(), required=False)

    def __init__(self, *args, category, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        filters = ParameterFilter.objects.filter(category=category)
        for filter in filters:
            if filter.data_type == ParameterFilter.BOOLEAN:
                self.fields['filter_{}'.format(filter.id)] = forms.BooleanField(required=False)
            if filter.data_type == ParameterFilter.CHECKBOX:
                parameterValues = []
                for parameterValue in ParameterValue.objects.filter(parameter=filter.parameter):
                    if parameterValue.value not in parameterValues:
                        parameterValues.append(parameterValue.value)
                try:
                    parameterValues.remove('')
                except ValueError:
                    print('ValueError')
                choices = ((x, x) for x in parameterValues)
                # i = 1
                # for parameterValue in parameterValues:
                #     choices.append((i, parameterValue))
                #     i += 1
                # print(choices)
                self.fields['filter_{}'.format(filter.id)] = forms.MultipleChoiceField(choices=choices,
                                                                                        widget=forms.widgets.CheckboxSelectMultiple(),
                                                                                        required=False)
            if filter.data_type == ParameterFilter.RANGE:
                pass

