from django import template
from num2words import num2words


register = template.Library()

@register.filter
def nums_to_text(data_text):
    data_list = data_text.split(' ')
    
    for item in data_list:
        if item.isdigit():
            data_text = data_text.replace(item, num2words(int(item), lang='ru'))
        elif ':' in item:
            two_num = item.split(':')
            if two_num[0].isdigit() and two_num[0].isdigit():
                data_text = data_text.replace(two_num[0], num2words(int(two_num[0]), lang='ru'))
                data_text = data_text.replace(two_num[1], num2words(int(two_num[1]), lang='ru'))
        elif '.' in item:
            two_num = item.split(',')
            if two_num[0].isdigit() and two_num[0].isdigit():
                data_text = data_text.replace(two_num[0], num2words(int(two_num[0]), lang='ru'))
                data_text = data_text.replace(two_num[1], num2words(int(two_num[1]), lang='ru'))
        elif ',' in item:
            two_num = item.split(',')
            if two_num[0].isdigit() and two_num[0].isdigit():
                data_text = data_text.replace(two_num[0], num2words(int(two_num[0]), lang='ru'))
                data_text = data_text.replace(two_num[1], num2words(int(two_num[1]), lang='ru'))
            
    return data_text
