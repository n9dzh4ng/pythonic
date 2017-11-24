# from urllib.parse import urlencode
try:
    # Python 2.X
    from urllib import urlencode
except ImportError:
    # Python 3+
    from urllib.parse import urlencode

aDict = {'name': 'Ned Zhang', 'hmdir': '~ggarcia'}
print(urlencode(aDict))
