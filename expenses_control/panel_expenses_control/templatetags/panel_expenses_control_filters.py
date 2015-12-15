from django import template

register = template.Library()

@register.filter(name='return_item')
def return_item(l, i):
        try:
                return l.filter(pk=i)
        except:
                return None
