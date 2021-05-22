from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.youtube.com/") # l'url du site web à rechercher
time.sleep(5)
os.system("python click2.py")
elem = driver.find_element_by_name("search_query")
time.sleep(2)
elem.send_keys("AMCode") #on colle "Hello World"
elem.send_keys(Keys.RETURN) #ici on clique sur la touche entrer
time.sleep(3)
os.system("python click.py")