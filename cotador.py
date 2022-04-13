import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class moedas:
    def __init__(self, url, moeda, txt_coin):
        self.url = url
        self.moeda = moeda
        self.txt_coin = txt_coin
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
        #return print("O",self.moeda,"está sendo cotado por: ", "R$", self.local.string)
    
    def criador_txt(self):
        self.dados_txt = open(f'{self.moeda}.txt','w+')
        self.dados_txt.writelines(f'O {self.moeda} {self.txt_coin} {self.local.string}\n manito \n numero do celular')
        self.dados_txt.close()
        return print('feito')
    
    def renomeie(self):
        self.navegador = webdriver.Chrome()
        self.navegador.get('https://web.whatsapp.com/')
        while len(self.navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        
        for i, mensagem in enumerate(self.dados_txt['mensagem']):
        pessoa = 
    
texto_cotacoes = "esta sendo cotado por:"    

urldolar = 'https://br.investing.com/currencies/usd-brl'
dolar_cotacao = moedas(urldolar, 'Dolar',texto_cotacoes )
dolar_cotacao.abridor_pagina()
dolar_cotacao.localizador("span", "text-2xl")
dolar_cotacao.filtrador(0)
dolar_cotacao.criador_txt()
#dolar_cotacao.renomeie()


urlbtc = 'https://www.investing.com/crypto/bitcoin'
btc_cotacao = moedas(urlbtc, 'Bitcoin',texto_cotacoes)
btc_cotacao.abridor_pagina()
btc_cotacao.localizador("span", "pid-1057391-last")
btc_cotacao.filtrador(0)
btc_cotacao.criador_txt()
#btc_cotacao.renomeie()

urleuro = 'https://br.investing.com/currencies/eur-brl'
euro_cotacao = moedas(urleuro, 'Euro',texto_cotacoes)
euro_cotacao.abridor_pagina()
euro_cotacao.localizador("span", "text-2xl")
euro_cotacao.filtrador(0)
euro_cotacao.criador_txt()
##euro_cotacao.renomeie()

urleth = 'https://br.investing.com/crypto/ethereum/eth-usd'
eth_cotacao = moedas(urleth, 'Etherum',texto_cotacoes)
eth_cotacao.abridor_pagina()
eth_cotacao.localizador("span", "text-2xl")
eth_cotacao.filtrador(0)
eth_cotacao.criador_txt()
eth_cotacao.renomeie()