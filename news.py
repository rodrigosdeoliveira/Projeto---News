import requests
import json
import pandas

def main():
    url = "https://content.guardianapis.com/search?api-key=11e6532a-ebc5-4b8b-a94e-e074781ea5c4"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print("Acessando a base de dados")
        dados = resposta.json()
        escolha = 4
        while escolha != 0:
            print("1 - Esportes")
            print("2 - Notícias")
            print("3 - Artes")
            print("4 - Todas as categorias")
            print("0 - Para sair")
            try:
                escolha = int(input("Digite o número correspondete a catergoria:  "))
            except:
                print("Por favor, digite apenas números")
            if escolha > 4 or escolha < 0:
                print("Categoria inexistente")
            elif escolha == 1:
                buscar_sports(dados)
            elif escolha == 2:
                buscar_news(dados)
            elif escolha == 3:
                buscar_arts(dados)
            elif escolha == 4:
                buscar_all(dados)
            elif escolha == 0:
                print("Obrigado por utilizar o programa")                 
    else:
        print("Há algum problema na URL")

def buscar_all(dados):
    titulo = []
    link = []
    for noticia in dados['response']['results']:
        titulo.append(noticia['webTitle'])
        link.append(noticia['webUrl'])
    if len(titulo) == 0:
        print('Não foram encotradas notícias nesta categoria')
    else:
        print("Exportando notícias tabela CSV...")
        exportar_csv(titulo, link, "todas")

def buscar_sports(dados):
    titulo = []
    link = []
    for noticia in dados['response']['results']:
        if noticia['pillarName'] == 'Sport':
            titulo.append(noticia['webTitle'])
            link.append(noticia['webUrl'])
    if len(titulo) == 0:
        print('Não fora encotradas notícias nesta categoria')
    else:
        print("Exportando notícias tabela CSV...")
        exportar_csv(titulo, link, "sport")

def buscar_news(dados):
    titulo = []
    link = []
    for noticia in dados['response']['results']:
        if noticia['pillarName'] == 'News':
            titulo.append(noticia['webTitle'])
            link.append(noticia['webUrl'])
    if len(titulo) == 0:
        print('Não fora encotradas notícias nesta categoria')
    else:
        print("Exportando notícias tabela CSV...")
        exportar_csv(titulo, link, "news")

def buscar_arts(dados):
    titulo = []
    link = []
    for noticia in dados['response']['results']:
        if noticia['pillarName'] == 'Arts':
            titulo.append(noticia['webTitle'])
            link.append(noticia['webUrl'])
    if len(titulo) == 0:
        print('Não fora encotradas notícias nesta categoria')
    else:
        print("Exportando notícias tabela CSV...")
        exportar_csv(titulo, link, "arts")

def exportar_csv(titulo, link, nome):
    tela = pandas.DataFrame({'Título':titulo, 'Link':link})
    tela.to_csv(nome+".csv", index=False, sep=";", encoding='utf-8-sig')
    print("Tabela exportada")

if __name__ == "__main__":
    main()

