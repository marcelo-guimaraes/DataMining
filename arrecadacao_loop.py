import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import bs4 as bs
  
# create webdriver object 
driver = webdriver.Firefox() 
  
# get geeksforgeeks.org 
url = 'https://sistemas.anm.gov.br/arrecadacao/extra/relatorios/cfem/maiores_arrecadadores.aspx'
driver.get(url) 
  
# get element  
ano = driver.find_element_by_id("ctl00_ContentPlaceHolder1_nu_Ano") 
#Arrecadação por:	
#Subs_Agrupadora = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdComparacao_0") 
#Substância = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdComparacao_1") 
#Região = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdComparacao_2") 
#Estado = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdComparacao_3")
#Município = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdComparacao_4") 
#Empresa = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdComparacao_5") 

arrecadacao_filters = ["ctl00_ContentPlaceHolder1_rdComparacao_0", "ctl00_ContentPlaceHolder1_rdComparacao_1", "ctl00_ContentPlaceHolder1_rdComparacao_2", "ctl00_ContentPlaceHolder1_rdComparacao_3", "ctl00_ContentPlaceHolder1_rdComparacao_4", "ctl00_ContentPlaceHolder1_rdComparacao_5"]

#Ordenado por:	
Operação = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdOrdenacao_0") 
Recolhimento = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdOrdenacao_1")

Ordernar_buttons = [Operação, Recolhimento]
  
# create action chain object 
action = ActionChains(driver) 
  
# click the item 
#ano.selectByVisibleText('2020')
Recolhimento.click() 

for arrecadacao_filter in arrecadacao_filters:
    arrecadacao_button = driver.find_element_by_id(arrecadacao_filter)
    arrecadacao_button.click()
    #get data
    gera = driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnGera")
    gera.click()
    dados = driver.page_source.encode('utf-8')

    
    
soup = bs.BeautifulSoup(dados, 'lxml')
table = soup.find_all('table', class_= "tabelaRelatorio")
df = pd.read_html(str(table))[0]
df