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
estado = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdComparacao_3") 
recolhimento = driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdOrdenacao_1")
gera = driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnGera")


  
# create action chain object 
action = ActionChains(driver) 
  
# click the item 
#ano.selectByVisibleText('2020')
estado.click()
recolhimento.click() 
gera.click() 
  
# perform the operation 
action.perform() 

dados = driver.page_source.encode('utf-8')
soup = bs.BeautifulSoup(dados, 'lxml')

table = soup.find_all('table', class_= "tabelaRelatorio")
df = pd.read_html(str(table))[0]

df.to_csv('dados11Maiores.csv', index = False)