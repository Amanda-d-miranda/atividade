import requests


def obter_dados_meteorologicos():
    URL = 'http://127.0.0.1:8000/v1/forecast'
    
    parametros = {
        'latitude': '-26.4851',
        'longitude': '-49.0713'
    }
    
    resposta = requests.get(URL, params=parametros)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        resposta.raise_for_status()

def menu_terminal():
    dados = obter_dados_meteorologicos()
    
    if dados:
        clima = dados['current']
        
        while True:
            print('============= MENU ============')
            print('Digite 1/ para consultar a Temperatura')
            print('Digite 2/ para consultar a Umidade')
            print('Digite 3/ para consultar a Velocidade do Vento')
            print('Digite 4/ para consultar a Elevação')
            print('Digite 5/ para Sair')
            
            ver = input('Digite o que você quer consultar: ')
            
            if ver == '1':
                print('Temperatura:', clima['temperature_2m'], '°C')
            elif ver == '2':
                print('Umidade:', clima['relative_humidity_2m'], '%')
            elif ver == '3':
                print('Velocidade do Vento:', clima['wind_speed_10m'], 'km/h')
            elif ver == '4':
                print('Elevação:', dados['elevation'])
            elif ver == '5':
                print('Encerrando a consulta')
                break
            else:
                print('Opção inválida!')

if __name__ == "__main__":
    menu_terminal()




