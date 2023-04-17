from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver del navegador
try:
    driver = webdriver.Firefox()
except Exception as e:
    print(f"{e}, Fall try in firefox")
    driver = webdriver.Edge()


# Abrir Outlook
driver.get('https://outlook.office.com/mail/')
print("All right here!")
time.sleep(200)

# Esperar a que se cargue la página y buscar los correos no leídos
unread_count = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".count.noselect"))).text

if unread_count != '0':
    # Notificar al usuario de que hay nuevos correos
    print(f'Tienes {unread_count} nuevos correos en tu bandeja de entrada')
else:
    print('No tienes nuevos correos en tu bandeja de entrada')