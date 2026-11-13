"""

import requests

URL = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,wind_speed_10m,surface_pressure'

resposta = requests.get(URL)

dados = resposta.json

print(resposta.status_code)

if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)

clima = dados['current']
print(clima)


while True:

    print('============== MENU =============')
    print('Digite 1 / para consultar a Temperatura:')
    print('Digite 2 / para consultar a Umidade:')
    print('Digite 3 / para consultar a Velocidade do vento:')
    print('Digite 4 / para consultar a Elevação:')
    print('Digite 5 / para consultar a Longitude:')
    print('Digite 6 / para consultar a Latitude:')
    print('Digite 7 / para Sair:')

    ver = input('Digite o que você quer consultar:')

    if ver == '1':
        print('Temperatura', clima['temperature_2m'], '°C')

    elif ver == '2':
        print('Temperatura', clima['relative_humidity_2m'], '')

    elif ver == '3':
        print('Temperatura', clima['wind_speed_10m'], 'km/h')

    if ver == '4':
        print('Temperatura', dados['elevation'])

    if ver == '5':
        print('Temperatura', dados['longitude'], '°C')

    if ver == '6':
        print('Temperatura', dados['latitude'], '°C')

    if ver == '7':
        print('Encerrando a consulta!!!')
        break
"""

