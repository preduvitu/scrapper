import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_locals = []

response = requests.get('https://www.jobbol.com.br/busca?cargo=Programador&local=')

content = response.content

site = BeautifulSoup(content, 'html.parser')

locals = site.findAll('div', attrs={'class': 'loop'})

for local in locals:

    titulo = local.find('div', attrs={'class':'jobtitle'})

    #print(titulo.text)

    lista_locals.append([titulo.text])

    news = pd.DataFrame(lista_locals, columns=['Nome e Local da vaga'])

news.to_excel('vagas.xlsx', index=False)

print(news)