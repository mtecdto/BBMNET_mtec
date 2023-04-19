#Fazendo as importações e criando o navegador
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
servico = Service(ChromeDriverManager().install())
navegador=webdriver.Chrome(service=servico)
from time import sleep

#Página de login
navegador.get('https://www3.bbmnet.com.br/NovoPortalLogin/Login.aspx')

#Captura os inputs de credenciais
usuarioElement = navegador.find_element(By.XPATH,'//*[@id="txtUsuario"]')
senhaElement = navegador.find_element(By.XPATH,'//*[@id="txtSenha"]')

#Preenchendo inputs
usuarioElement.send_keys("microtecnica")
senhaElement.send_keys("microba23")

#Clicando do botão de login
btnLogin = navegador.find_element(By.XPATH,'//*[@id="ImgBtnEntrar"]')
btnLogin.click()

#Abrindo nova página e colocando o foco nela - opção Licitação Pública
pageLicitacaoOption = navegador.window_handles[0]
navegador.switch_to.window(pageLicitacaoOption)
navegador.implicitly_wait(5)
btnLicitacao = navegador.find_element(By.XPATH,'//*[@id="lst"]/option')
btnLicitacao.click()

sleep(5)

#Abrindo página de painel de controle e deixando em foco
pegePainelControle = navegador.window_handles[1]
navegador.switch_to.window(pegePainelControle)
navegador.implicitly_wait(5)
navegador.get('https://www2.bbmnet.com.br/BBMNET/licitacao/DetalharEdital.aspx?chaveEdital=68271&AdicionarItemVisualizar=true')

sleep(3)
#pegeLicitacaoInformations = navegador.window_handles[2]
#navegador.switch_to.window(pegeLicitacaoInformations)
#navegador.implicitly_wait(5)

#Clicanco no botão sala de negociação
btnEntrarPregao = navegador.find_element(By.XPATH,'//*[@id="ctl00_MasterCPH_grdLotes_ctl02_imbEntrarSalaNegociacao"]')
btnEntrarPregao.click()

sleep(10)
#Deixando a página do chat em foco
pegeChatPregao = navegador.window_handles[2]
navegador.switch_to.window(pegeChatPregao)
navegador.implicitly_wait(5)

paginaChatRender = BeautifulSoup(navegador.page_source,"html.parser")

chatMessages = paginaChatRender.find("div", {"id": "txtLog"})
print(chatMessages)






