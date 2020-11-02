from django import template
import emojiflag as ef


register = template.Library()


@register.simple_tag
def emojiflag(country):
    return ef.get(country)
