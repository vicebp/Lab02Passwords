from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pyperclip as clipboard
driver = webdriver.Chrome("./chromedriver")

#varaibles de entorno
nombre='user'
apellido='user'
genero='Male'
dia='01'
mes='01'
anio='1997'
celular = '72014478'
contrasena='useruser'

#Obtener correo
driver.get("https://www.fakemail.net/")
time.sleep(5)
correo_generado = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/a[5]')
time.sleep(5)
correo_generado.click()
time.sleep(3)
correo_generado_usuario = clipboard.paste()


#Obtener rut valido
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://validarutchile.cl/generador-rut-validos.php')
time.sleep(3)
rut = driver.find_element_by_xpath('/html/body/div/div/div[1]/table/tbody/tr[5]/td[2]').text


#registro

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get('https://www.cinemark.cl/registro')

time.sleep(3)
usuario_name = driver.find_element_by_name("firstname")
usuario_apellido_pat = driver.find_element_by_name('lastname')
usuario_genero = Select(driver.find_element_by_xpath('//*[@id="form-elitegold"]/div/div/div[3]/div[1]/div/p/select'))
usuario_rut = driver.find_element_by_name('docu1')
usuario_dia = Select(driver.find_element_by_xpath('//*[@id="form-elitegold"]/div/div/div[4]/div[1]/div/div[1]/select'))
usaurio_mes = Select(driver.find_element_by_xpath('//*[@id="form-elitegold"]/div/div/div[4]/div[1]/div/div[2]/select'))
usuario_anio = Select(driver.find_element_by_xpath('//*[@id="form-elitegold"]/div/div/div[4]/div[1]/div/div[3]/select'))
usuario_celular = driver.find_element_by_name('phone')
usuario_correo = driver.find_element_by_name('email1')
usuario_correo_confirm = driver.find_element_by_name('email2')
usuario_pass = driver.find_element_by_name('pass1')
usuario_pass_confir = driver.find_element_by_name('pass2')
button = driver.find_element_by_xpath('//*[@id="modal-cookies-template"]/div[1]/div/button')
registrar = driver.find_element_by_xpath('//*[@id="form-elitegold"]/div/div/div[10]/button') 
button.click()
usuario_name.send_keys(nombre)
usuario_apellido_pat.send_keys(apellido)
usuario_genero.select_by_value(genero)
usuario_rut.send_keys(rut)
usuario_dia.select_by_value(dia)
time.sleep(3)
usaurio_mes.select_by_value(mes)
time.sleep(3)
usuario_anio.select_by_value(anio)
time.sleep(3)
usuario_celular.send_keys(celular)
usuario_correo.send_keys(correo_generado_usuario)
usuario_correo_confirm.send_keys(correo_generado_usuario)
usuario_pass.send_keys(contrasena)
usuario_pass_confir.send_keys(contrasena)
time.sleep(3)

registrar.click()

time.sleep(5)

#iniciarsesion
driver.execute_script("window.open('');")
time.sleep(3)
driver.switch_to.window(driver.window_handles[3])

driver.get('https://www.cinemark.cl/#signin')

time.sleep(3)
usuario_name = driver.find_element_by_name("username")
usuario_pass = driver.find_element_by_name('password')
ingresar = driver.find_element_by_name('commit')
usuario_name.send_keys(correo_generado_usuario)
usuario_pass.send_keys(contrasena)

ingresar.click()

time.sleep(5)

#recuperar y cambiar contrasena

driver.execute_script("window.open('');")
time.sleep(3)
driver.switch_to.window(driver.window_handles[4])

driver.get('https://www.cinemark.cl/reset-password')

time.sleep(5)
correo_cambiar = driver.find_element_by_xpath('//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/p/input')
cambiar = driver.find_element_by_xpath('//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[1]/div[3]/button')

time.sleep(5)
correo_cambiar.send_keys(correo_generado_usuario)
cambiar.click()

time.sleep(5)