from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pyperclip as clipboard
driver = webdriver.Chrome("./chromedriver")

#varaibles de entorno

nombre = "user"
contrasena = "Upercase123@"
nuevacontrasena = "Lowercase123@"
#Obtener correo
driver.get("https://www.fakemail.net/")
driver.set_window_size(1920,1080)
time.sleep(10)
#correo_generado = driver.find_element_by_id('click-to-copy').click()
correo_generado = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/a')
time.sleep(15)
correo_generado.click()
time.sleep(5)
correo_generado_usuario = clipboard.paste()

#registro
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://suscripciones.eljueves.es/id/register?continue=https://suscripciones.eljueves.es/id/register?continue=https://www.eljueves.es/")
time.sleep(10)

email = driver.find_element_by_xpath('//*[@id="email"]')
password=driver.find_element_by_xpath('//*[@id="password"]')
password_repeat=driver.find_element_by_xpath('//*[@id="password-confirm"]')
registrar = driver.find_element_by_xpath('//*[@id="form"]/div/div/div/div[1]/div[2]/div[6]/button')

time.sleep(5)
email.send_keys(correo_generado_usuario)
password.send_keys(contrasena)
password_repeat.send_keys(contrasena)
time.sleep(10)
registrar.click()

#confirmar corre0
driver.switch_to.window(driver.window_handles[0])
time.sleep(10)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.fakemail.net/window/id/2")
time.sleep(10)

#iniciar sesion
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get("https://suscripciones.eljueves.es/id/login?continue=https://suscripciones.eljueves.es/id/register?continue=https://suscripciones.eljueves.es/id/register?continue=https://www.eljueves.es/")
time.sleep(10)

email_ingreso = driver.find_element_by_xpath('//*[@id="email"]')
password_ingreso=driver.find_element_by_xpath('//*[@id="password"]')
ingresar = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[2]/form/div[3]/button')

time.sleep(5)
email_ingreso.send_keys(correo_generado_usuario)
password_ingreso.send_keys(contrasena)
time.sleep(10)
ingresar.click()

#cambiar contrasena
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])
driver.get("https://suscripciones.eljueves.es/id/perfil/cambiar-contrase%C3%B1a")
time.sleep(10)

password_change=driver.find_element_by_xpath('//*[@id="password"]')
password_change_confirm=driver.find_element_by_xpath('//*[@id="password-confirm"]')
cambiar=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[5]/button')
time.sleep(5)

password_change.send_keys(nuevacontrasena)
password_change_confirm.send_keys(nuevacontrasena)
time.sleep(5)

cambiar.click()

#recuperar contrasena
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[5])
driver.get("https://suscripciones.eljueves.es/id/password/reset?continue=https://www.eljueves.es/")
time.sleep(10)

correo_change=driver.find_element_by_xpath('//*[@id="email"]')
recuperar=driver.find_element_by_xpath('//*[@id="form"]/div[2]/button')
time.sleep(5)

correo_change.send_keys(correo_generado_usuario)
time.sleep(5)

recuperar.click()
time.sleep(5)


'''
#confirmar correo
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
acces_email = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a/span[2]')
confirm = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a')
'''
