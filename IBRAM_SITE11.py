import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.gov.br/anm/pt-br")

# aguarda carregamento
time.sleep(12)

#busco o elemento que irei clicar
next_page = driver.find_element_by_partial_link_text("https://www.gov.br/anm/pt-br/assuntos/arrecadacao