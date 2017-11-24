#!/usr/bin/env python

# python2
import urllib

# python3
# import urllib.parse

name = 'ned zhang'
number = 7
base = 'http://nedzhang@njcb.com.cb/doc/x.py'

final = '%s&name=%s&num=%d' % (base, name, number)

print("The original sentence:")
print(final)

print("I'll use quote now:")
# python2
quoteFinal = urllib.quote(final)
print(quoteFinal)
print("I'll undo the operate now:")
print(urllib.unquote(quoteFinal))
# python3
# print(urllib.parse.quote(final))


print("I'll use quote_plus now:")
# python2
quotePlusFinal = urllib.quote_plus(final)
print(quotePlusFinal)
print("I'll undo the operate now:")
print(urllib.unquote_plus(quotePlusFinal))
# python3
# print(urllib.parse.quote_plus(final))
