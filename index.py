import requests

# Substitua 'YOUR_API_KEY' pela sua chave de API da NASA
Link_API = '1GoawY9Z0fSpPrfmYebi8fFcTjfhKe8Udqy6T6ve'

# URL da API APOD
url = f'https://api.nasa.gov/planetary/apod?api_key=[1GoawY9Z0fSpPrfmYebi8fFcTjfhKe8Udqy6T6ve]'

# Faz a solicitação à API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    title = data['title']
    explanation = data['explanation']
    url = data['url']

    print(f'Título: {title}')
    print(f'Explicação: {explanation}')
    print(f'URL da Imagem: {url}')

    # Agora você pode exibir a imagem ou realizar análises adicionais das estrelas visíveis na imagem.
else:
    print('Erro ao acessar a API da NASA');
#Perguntas ao usuário sobre astronomia
# Perguntas do quiz sobre astronomia
perguntas = [
    {
        'pergunta': 'Qual é o planeta mais próximo do Sol?',
        'opcoes': ['Vênus', 'Marte', 'Mercúrio'],
        'resposta': 'Mercúrio'
    },
    {
        'pergunta': 'Qual é a maior lua de Júpiter?',
        'opcoes': ['Io', 'Europa', 'Ganimedes'],
        'resposta': 'Ganimedes'
    },
    {
        'pergunta': 'O que é uma estrela que explode violentamente, liberando uma grande quantidade de energia?',
        'opcoes': ['Cometa', 'Asteróide', 'Supernova'],
        'resposta': 'Supernova'
    }
]

# Função para executar o quiz
def executar_quiz(perguntas):
    pontuacao = 0

    for pergunta in perguntas:
        print(pergunta['pergunta'])
        for opcao in pergunta['opcoes']:
            print(f"- {opcao}")
        
        resposta = input("Sua resposta: ")

        if resposta.lower() == pergunta['resposta'].lower():
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta é: {pergunta['resposta']}\n")

    print(f"Sua pontuação total: {pontuacao} de {len(perguntas)}.")

# Iniciar o quiz
print("Bem-vindo ao Quiz de Astronomia!")
executar_quiz(perguntas)
