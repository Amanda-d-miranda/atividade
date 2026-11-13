Dashboard Meteorológico

Projeto em Python que consulta dados meteorológicos de Jaraguá do Sul/SC e exibe as informações em um painel web feito com Streamlit. Também é possível consultar os dados por um menu no terminal.

Dados exibidos
Temperatura (°C)
Umidade relativa (%)
Velocidade do vento (km/h)
Elevação (m)

No menu de terminal também é possível consultar a latitude e a longitude.

Estrutura do projeto
.
├── front.py            # Dashboard web com Streamlit
├── teste_prova.py      # Funções de consulta à API e menu de terminal
├── app.py              # Versão inicial do script (consulta direta à Open-Meteo)
├── requirements.txt    # Dependências do projeto
├── .env                # Variáveis de ambiente
└── .gitignore
front.py: monta a interface do painel, com os indicadores em colunas e um botão para consultar novamente.
teste_prova.py: contém a função obter_dados_meteorologicos(), que faz a requisição à API e retorna os dados em JSON, e a função menu_terminal(), usada para consultar os dados pelo terminal.
app.py: primeira versão do projeto, mantida como referência. O código está comentado.
Requisitos
Python 3.10 ou superior
API meteorológica rodando em http://127.0.0.1:8000/v1/forecast
Instalação
Crie e ative um ambiente virtual (opcional):
bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
Instale as dependências:
bash
pip install -r requirements.txt
Se os arquivos estiverem como _env e _gitignore, renomeie para .env e .gitignore.
Como executar
Dashboard web

Com a API em execução, rode:

bash
streamlit run front.py

O painel abre no navegador, normalmente em http://localhost:8501.

Menu no terminal
bash
python teste_prova.py

Digite o número da opção desejada para consultar um dado. A opção 7 encerra o programa.

Como funciona
O teste_prova.py envia uma requisição GET para a API e recebe os dados em JSON.
O front.py importa a função obter_dados_meteorologicos() e mostra os valores na tela.
Se ocorrer algum erro na consulta, o painel exibe uma mensagem de erro.
Tecnologias
Python
Streamlit
Requests
Open-Meteo (fonte dos dados meteorológicos)
