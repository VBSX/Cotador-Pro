import requests
from bs4 import BeautifulSoup

class moedas:
    def __init__(self, url, moeda):
        self.url = url
        self.moeda = moeda
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        self.page = requests.get(self.url,headers=self.headers)
        self.page.request.headers
        
    def abridor_pagina(self):    
        self.doc = BeautifulSoup(self.page.text, "html.parser")
    
    def localizador(self, dado_buscada, classe_buscada):
        self.dado_buscada = dado_buscada
        self.classe_buscada = classe_buscada
        self.precos = self.doc.find_all(dado_buscada, class_=classe_buscada)
        
    
    def filtrador(self,l):
        self.l = l
        self.parentes = self.precos[self.l].parent
        self.local = self.parentes.find("span") 
        return print("O",self.moeda,"está sendo cotado por: ", "R$", self.local.string)
        
        
urldolar = 'https://br.investing.com/currencies/usd-brl'
dolar_cotacao = moedas(urldolar, 'Dolar')
dolar_cotacao.abridor_pagina()
dolar_cotacao.localizador("span", "text-2xl")
dolar_cotacao.filtrador(0)

urlbtc = 'https://www.investing.com/crypto/bitcoin'
btc_cotacao = moedas(urlbtc, 'Bitcoin')
btc_cotacao.abridor_pagina()
btc_cotacao.localizador("span", "pid-1057391-last")
btc_cotacao.filtrador(0)

urleuro = 'https://br.investing.com/currencies/eur-brl'
euro_cotacao = moedas(urleuro, 'Euro')
euro_cotacao.abridor_pagina()
euro_cotacao.localizador("span", "text-2xl")
euro_cotacao.filtrador(0)


urleth = 'https://br.investing.com/crypto/ethereum/eth-usd'
eth_cotacao = moedas(urleth, 'Etherum')
eth_cotacao.abridor_pagina()
eth_cotacao.localizador("span", "text-2xl")
eth_cotacao.filtrador(0)
