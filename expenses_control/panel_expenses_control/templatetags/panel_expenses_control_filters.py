#coding: utf-8

from django import template

register = template.Library()

# pomocniczy filtr umożliwiający wyświetlenie w template zadanego elementu listy przekazanej uprzednio w słowniku do template
@register.filter(name='return_item')
def return_item(l, i):
        try:
                return l.filter(pk=i)
        except:
                return None
