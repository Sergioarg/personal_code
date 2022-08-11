#!/usr/bin/env python3
""" Selenium module for automatization login and logout in tawk. """
# Selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
# Python
from time import sleep

# Agent ids ───────────────────────────────────────────────────────────────────

url = "https://schoolpack.smart.edu.co/idiomas/alumnos.aspx"

# Options for chrome ──────────────────────────────────────────────────────────
coptions = webdriver.ChromeOptions()
coptions.add_argument('--ignore-certificate-errors')
# coptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=coptions)
wait = WebDriverWait(driver, 240)

# Open url. ────────────────────────────────────────────────────────────
driver.get(url)

sleep(3)
# Get diff in seconds
# time_now = datetime.now()
# end_hour = time_now.replace(hour=21, minute=00, second=00)
# print('\033[94mStart time: \033[0m', time_now,
#       '\n\033[94mEnd time: \033[0m', end_hour)
# diff_seconds = (end_hour - time_now).total_seconds()

user = 'change_user'
password = 'change correct'

# wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))

# LOGIN

input_user = '//*[@id="vUSUCOD"]'
input_password = '//*[@id="vPASS"]'
confirm_button = '//*[@id="BUTTON1"]'

driver.find_element(By.XPATH, input_user).send_keys(user)
driver.find_element(By.XPATH, input_password).send_keys(password)
driver.find_element(By.XPATH, confirm_button).click()
# wait to charge page


main_page = driver.current_window_handle

sleep(3)

programcion_button = '//*[@id="IMAGE18"]'
driver.find_element(By.XPATH, programcion_button).click()

sleep(5)
study_plan = '//*[@id="W0030Grid1ContainerRow_0001"]'

driver.find_element(By.XPATH, study_plan).click()

iniciar_button = '//*[@id="W0030BUTTON1"]'

driver.find_element(By.XPATH, iniciar_button).click()

sleep(5)
# Swith to first pop-up "Programar clases"
programar_clases_iframe = driver.find_element(By.XPATH, '//*[@id="gxp0_ifrm"]')
driver.switch_to.frame(programar_clases_iframe)

clase_2_button = '//*[@id="Grid1ContainerRow_0010"]/td[6]'
driver.find_element(By.XPATH, clase_2_button).click()

asignar_button = '//*[@id="BUTTON1"]'
driver.find_element(By.XPATH, asignar_button).click()

sleep(5)

# Return to main main page
driver.switch_to.default_content()

selecion_clases_iframe = driver.find_element(By.XPATH, '//*[@id="gxp1_ifrm"]')
driver.switch_to.frame(selecion_clases_iframe)

sede_dropdown = '//*[@id="vREGCONREG"]'
driver.find_element(By.XPATH, sede_dropdown).click()

calima_option = '//*[@id="vREGCONREG"]/option[14]'
driver.find_element(By.XPATH, calima_option).click()


sleep(5)

dia_dropdown = '//*[@id="vDIA"]'
driver.find_element(By.XPATH, dia_dropdown).click()

dia_dos = '//*[@id="vDIA"]/option[2]'
driver.find_element(By.XPATH, dia_dos).click()

sleep(5)

# Close drivers
driver.close()
driver.quit()
