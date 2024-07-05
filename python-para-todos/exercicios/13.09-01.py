'''
Exercício 1: Altere um dos arquivos geojson.py ou geoxml.py para que a saída do programa mostre os dois caracteres referentes ao código do país dos dados recebidos. Adicione teste(s) de erro para que o programa não retorne um traceback em caso de não haver código de país. Uma vez que o programa esteja funcionando, procure por “Atlantic Ocean” e confirme que o programa pode lidar com localizações que não pertencem a nenhum país.
'''


# SOlução 01:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    '''try:
        country_id = js['results'][0]['address_components'][3]['short_name']
        print('Código do país: ', country_id)
    except:
        print('Local não pertence a nenhum país.)'''
    
    location = js['results'][0]['address_components']
    count = -1
    encontrou = False
    for loc in location:
        count += 1
        if (js['results'][0]['address_components'][count]['types'] == ['country', 'political']):
            print('País: ', js['results'][0]['address_components'][count]['short_name'])
            encontrou = True
            break
        else:
            continue

    if not encontrou:
        print('País não encontrado.')