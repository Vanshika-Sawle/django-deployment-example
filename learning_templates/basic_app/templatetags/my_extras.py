from django import template

register=template.Library()
@register.filter(name='vans')
def vans(value,arg):
    """
    This function cuts arg from string
    """

    return value.replace(arg,'')
