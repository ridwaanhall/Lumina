from django import template
from django.conf import settings
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def canonical_url(context):
    """
    Menghasilkan tag <link rel="canonical" href="..."> untuk URL saat ini.
    """
    request = context.get('request')

    if not request:
        return ""

    canonical_url = request.build_absolute_uri(request.path)

    # Perubahan: Gunakan mark_safe untuk menandai output sebagai aman
    return mark_safe(f'<link rel="canonical" href="{canonical_url}" />')