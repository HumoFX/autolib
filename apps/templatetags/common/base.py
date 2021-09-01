from django import template

register = template.Library()


@register.simple_tag(name='base')
def get_base_informer(request):
    return {
        'request': request
    }
