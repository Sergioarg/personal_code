#!/usr/bin/env -S powershell.exe -c python3
""" Selenium module for automatization login and logout in tawk. """
# Selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime as date
from time import sleep

# Options for chrome ──────────────────────────────────────────────────────────
coptions = webdriver.ChromeOptions()
coptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=coptions)
wait = WebDriverWait(driver, 240)


def schedule_clases():
    # SchoolPack Url ─────────────────────────────────────────────────────────

    url = "https://schoolpack.smart.edu.co/idiomas/alumnos.aspx"
    # Open url. ────────────────────────────────────────────────────────────
    driver.get(url)

    user = '1000162785'
    password = 'SmartSchool'
    current_day = date.today().strftime("%A")

    # LOGIN ON SCHOOL PACK  ───────────────────────────────────────────────────
    input_user = '//*[@id="vUSUCOD"]'
    input_password = '//*[@id="vPASS"]'
    confirm_button = '//*[@id="BUTTON1"]'

    wait.until(EC.presence_of_element_located((By.XPATH, input_user)))

    driver.find_element(By.XPATH, input_user).send_keys(user)
    driver.find_element(By.XPATH, input_password).send_keys(password)
    driver.find_element(By.XPATH, confirm_button).click()

    # main_page = driver.current_window_handle

    # Change before click on button of programcion
    programcion_button = '//*[@id="IMAGE18"]'
    wait.until(EC.presence_of_element_located((By.XPATH, programcion_button)))
    driver.find_element(By.XPATH, programcion_button).click()

    # START TO SELECT SPECIFIC CLASS
    study_plan = '//*[@id="W0030Grid1ContainerRow_0001"]'
    wait.until(EC.presence_of_element_located((By.XPATH, study_plan)))
    driver.find_element(By.XPATH, study_plan).click()

    iniciar_button = '//*[@id="W0030BUTTON1"]'
    wait.until(EC.presence_of_element_located((By.XPATH, iniciar_button)))
    driver.find_element(By.XPATH, iniciar_button).click()

    # Swith to first pop-up "Programar clases"
    first_iframe = '//*[@id="gxp0_ifrm"]'
    wait.until(EC.presence_of_element_located((By.XPATH, first_iframe)))
    programar_clases_iframe = driver.find_element(By.XPATH, first_iframe)
    driver.switch_to.frame(programar_clases_iframe)

    # Boton de siguiente
    button_siguiente = '//*[@id="Grid1ContainerTbl"]/tfoot/tr/td/div/button[3]'
    sleep(5)
    wait.until(EC.presence_of_element_located((By.XPATH, button_siguiente)))
    driver.find_element(By.XPATH, button_siguiente).click()

    sleep(5)
    # Change this XPATH for every class
    clases = {
        'clase_19': '//*[@id="Grid1ContainerRow_0011"]/td[11]',
        'clase_20': '//*[@id="Grid1ContainerRow_0012"]/td[11]',
        'clase_21': '//*[@id="Grid1ContainerRow_0013"]/td[11]',
        'clase_22': '//*[@id="Grid1ContainerRow_0014"]/td[11]',
        'clase_23': '//*[@id="Grid1ContainerRow_0015"]/td[11]',
        'clase_24': '//*[@id="Grid1ContainerRow_0016"]/td[11]',
        'clase_25': '//*[@id="Grid1ContainerRow_0017"]/td[11]',
        'clase_26': '//*[@id="Grid1ContainerRow_0018"]/td[11]',
        'clase_27': '//*[@id="Grid1ContainerRow_0019"]/td[11]'
    }

    # Check day and select class
    if current_day == 'Monday':
        clase_row = clases['clase_20']
    elif current_day == 'Tuesday':
        clase_row = clases['clase_21']
    elif current_day == 'Wednesday':
        clase_row = clases['clase_22']
    elif current_day == 'Sunday':
        clase_row = clases['clase_19']
    else:
        driver.close()
        driver.quit()

    sleep(3)
    # Click on class selecte
    wait.until(EC.presence_of_element_located((By.XPATH, clase_row)))
    driver.find_element(By.XPATH, clase_row).click()

    sleep(5)
    # Click on 'Asignar' button
    asignar_button = '//*[@id="BUTTON1"]'
    driver.find_element(By.XPATH, asignar_button).click()

    # Return to main main page
    driver.switch_to.default_content()

    # SELECT sede, dia and hora of the class
    second_iframe = '//*[@id="gxp1_ifrm"]'
    wait.until(EC.presence_of_element_located((By.XPATH, second_iframe)))

    sleep(3)
    selecion_clases_iframe = driver.find_element(By.XPATH, second_iframe)
    driver.switch_to.frame(selecion_clases_iframe)

    # Display dropdown of sede
    sede_dropdown = '//*[@id="vREGCONREG"]'
    driver.find_element(By.XPATH, sede_dropdown).click()

    # Select CALIMA sede in the dropdown, change the number acording the class
    calima_option = '//*[@id="vREGCONREG"]/option[14]'
    driver.find_element(By.XPATH, calima_option).click()

    # Display dropdown of day
    dia_dropdown = '//*[@id="vDIA"]'
    driver.find_element(By.XPATH, dia_dropdown).click()

    dia_selection = '//*[@id="vDIA"]/option[2]'
    driver.find_element(By.XPATH, dia_selection).click()
    driver.find_element(By.XPATH, dia_selection).click()

    if current_day == 'Wednesday':
        ultima_clase = '//*[@id="Grid1ContainerRow_0011"]/td[3]'
    else:
        ultima_clase = '//*[@id="Grid1ContainerRow_0010"]/td[3]'

    wait.until(EC.presence_of_element_located((By.XPATH, ultima_clase)))
    driver.find_element(By.XPATH, ultima_clase).click()

    confirmar_button = '//*[@id="BUTTON1"]'
    driver.find_element(By.XPATH, confirmar_button).click()

    sleep(5)
    print('Class scheduled')

    # Close drivers
    driver.close()
    driver.quit()


if __name__ == '__main__':
    schedule_clases()
