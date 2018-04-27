import ast

from django.template.defaulttags import register


@register.filter(name='get_item')
def get_item(dictionary, key):
    if type(dictionary) == str and type(dictionary) != dict:
        dictionary = ast.literal_eval(dictionary)
    return dictionary.get(key)
