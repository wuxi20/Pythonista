# coding: utf-8

# https://forum.omz-software.com/topic/3062/string-maketrans-method-not-working/4

import string

#str = 'map.html'
s = 'map.html'
i = 'abcdefghijklmnopqrstuvwxyz'
o = 'cdefghijklmnopqrstuvwxyzab'

table = string.maketrans(i, o)
print(str.translate(s, table))


