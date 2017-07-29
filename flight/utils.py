# -*- coding: utf-8 -*-
from string import digits, ascii_uppercase
from transliterate import translit
import random


def code_generation(bad_text=None, text=''):
    if bad_text:
        text = ''
    while len(text) < 6:
        text += random.choice(list(digits + ascii_uppercase))

    return text

def route_name_generation(airpotr_out, airpotr_in, code_name=''):
    code_name += airpotr_out.name[0:1]
    code_name += airpotr_in.name[0:1]
    code_name = (translit(code_name, reversed=True))
    while len(code_name) < 6:
        code_name += random.choice(list(digits))
    return code_name.upper()
