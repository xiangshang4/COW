from django import template

register=template.Library()

def remove_us(value,arg):
    return value.replace(arg," ")

register.filter('remove_underscore',remove_us)
