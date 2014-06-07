from django import template

register = template.Library()


@register.inclusion_tag( 'exhibition-row.html' )
def exhibition_row( exhibition ):
    return {'e': exhibition}


@register.inclusion_tag( 'exhibition-list.html' )
def exhibition_list( title, elist ):
    return {
        'title': title,
        'list': elist,
    }

