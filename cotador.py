import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib, urllib.parse

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
    
    def localizador_cotacao(self, dado_buscado, classe_buscada, ):
        self.dado_buscado = dado_buscado
        self.classe_buscada = classe_buscada
        self.precos = self.doc.find_all(dado_buscado, class_=classe_buscada)
    
    def localizador_variacao(self,dado_b_variacao, classe_b_variacao, dado_b_variacao_negativo, classe_b_variacao_negativo):
        
            self.dado_b_variacao = dado_b_variacao
            self.classe_b_variacao = classe_b_variacao
            self.precos_variacao = self.doc.find_all(dado_b_variacao, class_=classe_b_variacao)

            self.dado_b_variacao_negativo = dado_b_variacao_negativo
            self.classe_b_variacao_negativo = classe_b_variacao_negativo
            self.precos_variacao_negativo = self.doc.find_all(dado_b_variacao_negativo, class_=classe_b_variacao_negativo)

    
    def filtrador(self,l_cotacao, ):
        #qual das tags a ser filtrada
        self.l_cotacao = l_cotacao
        self.parentes_cotacao = self.precos[self.l_cotacao].parent
        self.local_cotacao = self.parentes_cotacao.find(self.dado_buscado)
        
    def filtrador_variacao(self,l_variacao):
        
        self.l_variacao = l_variacao
        try:
            self.parentes_variacao = self.precos_variacao[self.l_variacao].parent
            self.local_variacao = self.parentes_variacao.find(self.dado_b_variacao)
        #return print("O",self.moeda,"está sendo cotado por: ", "R$", self.local_cotacao.string)
        except:
            self.parentes_variacao = self.precos_variacao_negativo[self.l_variacao].parent
            self.local_variacao = self.parentes_variacao.find(self.dado_b_variacao_negativo)
            print(self.local_variacao)
        
    def criador_txt(self, txt_variacao):
        self.txt_variacao = txt_variacao
        if txt_variacao in ["tendo uma variacao de "]:
            self.p = txt_variacao, {self.local_variacao.string}
            
        else:
            self.p = ""
            
        self.saida_xl = pd.ExcelWriter(f'{self.moeda}.xlsx')  
        
        self.xlsx_moeda = pd.DataFrame({'Pessoa':["makako", "coloque o nome"],'Numero':["coloque o numero", "coloque o numero"], 'Mensagem':[f'{self.moeda} {self.txt_coin} {self.local_cotacao.string}', f'{self.moeda} {self.txt_coin} {self.local_cotacao.string}']})
        self.xlsx_moeda.to_excel(self.saida_xl, self.moeda)
        # df = pd.DataFrame.from_dict(self.xlsx_moeda, orient='index')
        # df = df.transpose()
        self.saida_xl.save()
        
        #pip install openpyxl xlsxwriter xlrd
        return print(self.moeda, 'feito' )
    
    def renomeie(self):
        self.ler_xls = pd.read_excel(f"{self.moeda}.xlsx")
        
        self.navegador = webdriver.Chrome()
        ('https://web.whatsapp.com/')
        
        
        for self.i, self.mensagem in enumerate(self.ler_xls['Mensagem']):
            self.pessoa = self.ler_xls.loc[self.i, "Pessoa"] 
            self.numero = self.ler_xls.loc[self.i, "Numero"]
            self.texto = urllib.parse.quote(f"Olá {self.pessoa}! {self.mensagem}")
            self.link = f"https://web.whatsapp.com/send?phone={self.numero}&text={self.texto}"
            
            self.navegador.get(self.link)
            
            while len(self.navegador.find_elements_by_id("side")) < 1:# O navegador vai aguardar o whats até que o elemento "side" seja renderizado após o logon
                time.sleep(1)

            self.navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)#Será feito a busca do elemento da mesagem e logo após apertará o enter

            
texto_cotacoes = "esta sendo cotado por: R$"    

urldolar = 'https://br.investing.com/currencies/usd-brl'
dolar_cotacao = moedas(urldolar, 'Dolar',texto_cotacoes )
dolar_cotacao.abridor_pagina()
dolar_cotacao.localizador_cotacao("span", "text-2xl")
dolar_cotacao.localizador_variacao("span","instrument-price_change-percent__19cas ml-2.5 text-negative-main", "span", "instrument-price_change-percent__19cas ml-2.5 text-positive-main"  )
dolar_cotacao.filtrador(0)
dolar_cotacao.filtrador_variacao(0)
dolar_cotacao.criador_txt("tendo uma variacao de ")
dolar_cotacao.renomeie()


# urlbtc = 'https://www.investing.com/crypto/bitcoin'
# btc_cotacao = moedas(urlbtc, 'Bitcoin',texto_cotacoes)
# btc_cotacao.abridor_pagina()
# btc_cotacao.localizador("span", "pid-1057391-last")
# btc_cotacao.filtrador(0)
# btc_cotacao.criador_txt()
# #btc_cotacao.renomeie()

# urleuro = 'https://br.investing.com/currencies/eur-brl'
# euro_cotacao = moedas(urleuro, 'Euro',texto_cotacoes)
# euro_cotacao.abridor_pagina()
# euro_cotacao.localizador("span", "text-2xl")
# euro_cotacao.filtrador(0)
# euro_cotacao.criador_txt()
# ##euro_cotacao.renomeie()

# urleth = 'https://br.investing.com/crypto/ethereum/eth-usd'
# eth_cotacao = moedas(urleth, 'Etherum',texto_cotacoes)
# eth_cotacao.abridor_pagina()
# eth_cotacao.localizador("span", "text-2xl")
# eth_cotacao.filtrador(0)
# eth_cotacao.criador_txt()
# eth_cotacao.renomeie()