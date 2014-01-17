from django import template

register = template.Library()

@register.inclusion_tag('multilingual.html', takes_context=True)
def ml(context, *args, **kwargs):
    return {
        'multilingual_text': kwargs,
        'selected_language': context["language"]
    }

