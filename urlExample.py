import urllib.request
import os.path
import json

def get_html(url):
    req = urllib.request.urlopen(url)
    html = req.read()
    return html

if __name__ == '__main__':
    url = 'https://www.frikidelto.com/wp-content/uploads/2021/08/OFERTAS_DEL_DIA.png'
    f = open(os.path.basename(url), 'wb')
    f.write(get_html(url))
    f.close()
    print('End of Script')