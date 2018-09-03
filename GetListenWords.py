# -*- coding: utf-8 -*-
import re, os

with open('E:\\notes\words.txt', 'rb') as f:
    file = f.read().decode('utf-8')

words = '\n'.join(re.findall('[a-z]+', file))
with open('E:\\notes\words-listen.txt', 'w') as f:
    f.write(words)