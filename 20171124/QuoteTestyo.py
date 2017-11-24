#!/usr/bin/env python
# Attention:If we don't import module of python3 before module of python2, it doesn't work!!!
try:
    # python3
    import urllib.parse
except ImportError:
    # python2
    import urllib

name = 'ned zhang'
number = 7
base = 'http://nedzhang@njcb.com.cb/doc/x.py'

final = '%s&name=%s&num=%d' % (base, name, number)

print("The original sentence:")
print(final)

print("I'll use quote now:")
try:
    # python2
    quoteFinal = urllib.quote(final)
except AttributeError:
    # python3
    quoteFinal = urllib.parse.quote(final)
print(quoteFinal)
print("I'll undo the operate now:")
try:
    # python2
    print(urllib.unquote(quoteFinal))
except AttributeError:
    # python3
    print(urllib.parse.quote(final))

print("I'll use quote_plus now:")
try:
    # python2
    quotePlusFinal = urllib.quote_plus(final)
except AttributeError:
    # python3
    quotePlusFinal = urllib.parse.quote_plus(final)
print(quotePlusFinal)
print("I'll undo the operate now:")
try:
    # python2
    print(urllib.unquote_plus(quoteFinal))
except AttributeError:
    # python3
    print(urllib.parse.quote_plus(final))
