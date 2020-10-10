# import webdriver 
from selenium import webdriver 
  
# import Action chains  
from selenium.webdriver.common.action_chains import ActionChains 
  
profile = webdriver.FirefoxProfile()

# Configurando Firefox para n~ao mostrar popup quando for salvar arquivo
profile.set_preference("browser.download.panel.shown", False)
profile.set_preference("browser.helperApps.neverAsk.openFile","text/csv,application/vnd.ms-excel")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", "/home/marcelo/datasprints/IBRAM")

    
# create webdriver object 
driver = webdriver.Firefox(firefox_profile=profile) 
  
# get geeksforgeeks.org 
driver.get("https://app.anm.gov.br/SIGBM/Publico/ClassificacaoNacionalDaBarragem") 
  
# get element  
element = driver.find_element_by_id("btnExportar") 

  
# create action chain object 
action = ActionChains(driver) 
  
# click the item 
action.click(on_element = element) 
  
# perform the operation 
action.perform() 