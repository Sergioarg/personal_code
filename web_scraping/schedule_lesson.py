#!/usr/bin/env -S powershell.exe -c python3
""" Selenium module for automatization login and logout in tawk. """
# Selenium
from datetime import datetime as date
from time import sleep

from selenium import webdriver
from send_email import send_emial
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

    # ! ───────────────────────────────────────────────────────────────────────
    # ! Code to close advice of simulation
    try:
        id_iframe = "gxp0_ifrm"
        wait.until(EC.presence_of_element_located((By.ID, id_iframe)))
        iframe = driver.find_element(By.ID, id_iframe)
        driver.switch_to.frame(iframe)

        sleep(5)
        id_button_regresar = 'BUTTON1'
        wait.until(EC.presence_of_element_located((By.ID, id_button_regresar)))
        driver.find_element(By.ID, id_button_regresar).click()

        driver.switch_to.default_content()
    except RuntimeError:
        print('Ya no esta el Aviso despues de loggin. :)')
    # ! ───────────────────────────────────────────────────────────────────────

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
    wait.until(EC.presence_of_element_located((By.XPATH, button_siguiente)))
    sleep(5)
    driver.find_element(By.XPATH, button_siguiente).click()

    # Double click of siguiente button
    sleep(5)
    driver.find_element(By.XPATH, button_siguiente).click()

    sleep(5)
    # Change this XPATH for every class
    clases = {
        'clase_37': '//*[@id="Grid1ContainerRow_0013"]/td[6]',
        'clase_38': '//*[@id="Grid1ContainerRow_0014"]/td[6]',
        'clase_39': '//*[@id="Grid1ContainerRow_0015"]/td[11]',
        'clase_40': '//*[@id="Grid1ContainerRow_0016"]/td[11]',
        'clase_41': '//*[@id="Grid1ContainerRow_0017"]/td[11]',
        'clase_42': '//*[@id="Grid1ContainerRow_0018"]/td[11]',
        'clase_43': '//*[@id="Grid1ContainerRow_0019"]/td[11]',
        'clase_44': '//*[@id="Grid1ContainerRow_0020"]/td[11]',
        'clase_45': '//*[@id="Grid1ContainerRow_0021"]/td[6]'
    }

    # Check day and select class
    if current_day == 'Monday':
        # Lunes
        clase_row = clases['clase_40']
    elif current_day == 'Tuesday':
        # Martes
        clase_row = clases['clase_41']
    elif current_day == 'Wednesday':
        # Miercoles
        clase_row = clases['clase_38']
    elif current_day == 'Sunday':
        # Domingo
        clase_row = clases['clase_39']
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

    # Check if class could be scheduled.
    # try:
    #     warning_message = '//*[@id="TABLE2"]/tbody/tr[3]/td/div/span/div'
    #     wait.until(EC.presence_of_element_located((By.XPATH, warning_message)))
    #     print('Class could not be scheduled.')
    #     send_emial(text_file)
    # except RuntimeError:
    #     print('Class successfully scheduled.')

    sleep(5)
    # Close drivers
    driver.close()
    driver.quit()


if __name__ == '__main__':
    schedule_clases()
