#!/usr/bin/env python3


fill_char_len = 100
def harf_bul(input_data, search_char):

    index_list = []
    for i in range(len(input_data)):
        if input_data[i] == search_char:
            index_list.append(str(i +1) + '.')

    if len(input_data) == 0:
        return f'''Input not found.'''

    elif len(index_list) == 0:
        return f'''"{input_data}" not contains the "{str(search_char)}" character.\nCount: {len(index_list)}'''

    elif len(index_list) == 1:
        return f'''"{input_data}" contains the "{str(search_char)}" character on \
{', '.join(index_list)} array.\nCount: {len(index_list)}'''

    elif len(index_list) == 2:
        return f'''"{input_data}" contains the "{str(search_char)}" character on \
{str(index_list).replace("'", "").replace(",", " and ")[1:-1]} arrays.\nCount: {len(index_list)}'''

    elif len(index_list) > 2:
        return f'''"{input_data}" contains the "{str(search_char)}" character on \
{', '.join(index_list)} arrays.\nCount: {len(index_list)}'''

print(f'''
{'=' * fill_char_len}
{'Character Finder'.center(fill_char_len)}
{'-' * fill_char_len}
{"This program finds the index/indices of the given character's in the pattern.".center(fill_char_len, '-')}

-> Input: Write the pattern.
-> Looking for: Write the character to be searched.
-> Enter only 1 character.
-> Be careful about uppercase/lowercase.
{'-' * fill_char_len}
-> Type 0 (Zero) to exit.
{'=' * fill_char_len}''')
while True:
    input_ = input('Input      : ')
    if input_ == '0':
        exit('Goodbye.')
    char_ = input('Looking for: ')
    calistir = harf_bul(input_, char_)
    print(calistir)
    print('=' * fill_char_len)
