#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

s = base64.b64encode('Using BASE 64 encoding in Python'.encode('utf-8'))
print(s)  #b'VXNpbmcgQkFTRSA2NCBlbmNvZGluZyBpbiBQeXRob24='
d = base64.b64decode(s).decode('utf-8')
print(d)  #Using BASE 64 encoding in Python

s = base64.urlsafe_b64encode('Using BASE 64 encoding in Python'.encode('utf-8'))
print(s)  #b'VXNpbmcgQkFTRSA2NCBlbmNvZGluZyBpbiBQeXRob24='
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d) #Using BASE 64 encoding in Python