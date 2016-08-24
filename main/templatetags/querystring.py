from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    querystring = context['request'].GET.copy()
    for key, value in kwargs.items():
        if key in querystring.dict():
            querystring.pop(key)
        querystring.appendlist(key, value)
    return '?' + querystring.urlencode()
