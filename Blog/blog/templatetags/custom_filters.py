from django import template
from num2words import num2words
import re

register = template.Library()

@register.filter
def nums_to_text(data_text):

    try:
        pattern = r'(\d+)'
        list_nums = [ item for item in re.split(pattern, data_text) if item.isdigit()]
        
        for num in list_nums:
            data_text = data_text.replace(num, num2words(int(num), lang='ru'))
    except TypeError as err:
        print(f'Ошибка {err}!')
        return None

    return data_text
