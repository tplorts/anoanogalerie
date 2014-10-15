from django import template

register = template.Library()

ML_CONTEXT_KEY = "ml_active_language"


@register.inclusion_tag( 'exhibition-row.html', takes_context=True )
def exhibition_row( context, exhibition ):
    return {
        ML_CONTEXT_KEY: context[ML_CONTEXT_KEY],
        'e': exhibition,
    }


@register.inclusion_tag( 'exhibition-list.html', takes_context=True )
def exhibition_list( context, elist, **mlTitles ):
    return {
        ML_CONTEXT_KEY: context[ML_CONTEXT_KEY],
        'mlTitles': mlTitles,
        'list': elist,
    }

