#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

# Enter email address, password and POP3 server address:
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# Connect to POP3 server:
server = poplib.POP3(pop3_server)
# Debug information can be turned on or off:
server.set_debuglevel(1)
# Optional: Print the welcome text of the POP3 server:
print(server.getwelcome().decode('utf-8'))
# Authentication:
server.user(email)
server.pass_(password)
# stat() returns the number of messages and their occupied space:
print('Messages: %s. Size: %s' % server.stat())
# list() returns the numbers of all messages:
resp, mails, octets = server.list()
# You can view the returned list like [b'1 82923', b'2 2184', ...]
print(mails)
# Get the latest email, note that the index number starts at 1:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines stores each line of the raw text of the email,
# The raw text of the entire email can be obtained:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# Parse out the email later:
msg = Parser().parsestr(msg_content)
print_info(msg)
#Mail can be deleted directly from the server based on the mail index number:
# server.dele(index)
# Close the connection:
server.quit()