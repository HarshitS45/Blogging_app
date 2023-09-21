from django.template import Library

register = Library()

def placeholder(value, token):
    """To generate the placeholder of an input form its name"""
    value.field.widget.attrs["placeholder"] = token.title()
    return value

register.filter(placeholder)