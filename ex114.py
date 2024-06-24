import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/')
except urllib.error.URLError:
    print('O site Youtube não está acessível no momento.')
else:
    print('Consegui acessar o site Youtube com sucesso!')