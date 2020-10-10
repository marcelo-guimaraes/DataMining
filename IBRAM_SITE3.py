# import webdriver 
from selenium import webdriver 
  
# import Action chains  
from selenium.webdriver.common.action_chains import ActionChains 
  
# create webdriver object 
driver = webdriver.Firefox() 
  
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