from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def canonical_url(context):
    request = context.get('request')

    if not request:
        return ""

    canonical_url = request.build_absolute_uri(request.path)

    return mark_safe(f'<link rel="canonical" href="{canonical_url}" />')