#!/usr/bin/env -S powershell.exe -c python3
""" Selenium module for automatization login and logout in tawk. """
# Selenium
from datetime import datetime as date
from time import sleep

from functions import create_clases_dictionary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Options for chrome ──────────────────────────────────────────────────────────
coptions = webdriver.ChromeOptions()
coptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=coptions)
wait = WebDriverWait(driver, 240)


def click_element(xpath_button: str):
    """Click on specific button of HTML with XPATH.

    Args:
        xpath_button (str): XPATH of page to click
    """
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_button)))
    driver.find_element(By.XPATH, xpath_button).click()


def schedule_clases(user: str, password: str, next_reps: int):
    """Schedule class in SchoolPack in CALIMA at 7:30 PM

    Args:
        user (str): user in SchoolPack
        password (str): password's user of SchoolPack
        next_reps (int): number of repetitions to click on next button
    """

    Green, Yellow, Red, Reset = '\033[92m', '\033[93m', '\033[91m', '\033[0m'

    # SchoolPack Url ──────────────────────────────────────────────────────────
    url = "https://schoolpack.smart.edu.co/idiomas/alumnos.aspx"

    # Open url. ───────────────────────────────────────────────────────────────
    driver.get(url)

    # LOGIN ON SCHOOL PACK  ───────────────────────────────────────────────────
    input_user = '//*[@id="vUSUCOD"]'
    input_password = '//*[@id="vPASS"]'
    confirm_button = '//*[@id="BUTTON1"]'

    wait.until(EC.presence_of_element_located((By.XPATH, input_user)))

    driver.find_element(By.XPATH, input_user).send_keys(user)
    driver.find_element(By.XPATH, input_password).send_keys(password)
    driver.find_element(By.XPATH, confirm_button).click()

    # main_page = driver.current_window_handle
    # ? Close notice of simulation ────────────────────────────────────────────
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
        print(f'{Yellow}The login notice is no longer displayed.{Reset}')
    # ? ───────────────────────────────────────────────────────────────────────

    # Change before click on button of programcion
    programcion_button = '//*[@id="IMAGE18"]'
    click_element(programcion_button)

    # START TO SELECT SPECIFIC CLASS
    study_plan = '//*[@id="W0030Grid1ContainerRow_0001"]'
    click_element(study_plan)

    iniciar_button = '//*[@id="W0030BUTTON1"]'
    click_element(iniciar_button)

    # Swith to first pop-up "Programar clases"
    first_iframe = '//*[@id="gxp0_ifrm"]'
    wait.until(EC.presence_of_element_located((By.XPATH, first_iframe)))
    programar_clases_iframe = driver.find_element(By.XPATH, first_iframe)
    driver.switch_to.frame(programar_clases_iframe)

    # Boton de siguiente
    button_siguiente = '//*[@id="Grid1ContainerTbl"]/tfoot/tr/td/div/button[3]'
    wait.until(EC.presence_of_element_located((By.XPATH, button_siguiente)))

    # ? Repetir veces que se repite dar clink en siguiente
    for repetition in range(next_reps):
        sleep(5)
        driver.find_element(By.XPATH, button_siguiente).click()

    sleep(5)

    # ? Create dict comprenhention to clases
    # ? Note: Change range number as needed

    clases = create_clases_dictionary(3, 9, 3, 9)

    for clase_name, clase_xpath in clases.items():

        clase = wait.until(EC.presence_of_element_located((By.XPATH, clase_xpath)))

        if clase.text == 'Pendiente':
            print(f'Clase: {clase_name}')
            clase_row = driver.find_element(By.XPATH, clase_xpath)
            break

    clase_row.click()
    sleep(5)

    # Click on 'Asignar' button
    asignar_button = '//*[@id="BUTTON1"]'
    driver.find_element(By.XPATH, asignar_button).click()

    fail_schedule = None
    # ! Close in case of class may not have been scheduled.
    try:
        warning_message = '//*[@id="TABLE2"]/tbody/tr[1]/td/div/span/div'
        fail_schedule = wait.until(EC.presence_of_element_located((By.XPATH, warning_message)))
        print(f'{Red}Class could not be scheduled.{Reset}')
        driver.close()
        driver.quit()
    except RuntimeError:
        print(f'{Green}Class successfully scheduled.{Reset}')

    if fail_schedule is not None:
        return (1)

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

    # if current_day == 'Wednesday':
    #     ultima_clase = '//*[@id="Grid1ContainerRow_0011"]/td[3]'
    ultima_clase = '//*[@id="Grid1ContainerRow_0010"]/td[3]'
    click_element(ultima_clase)

    confirmar_button = '//*[@id="BUTTON1"]'
    driver.find_element(By.XPATH, confirmar_button).click()

    sleep(5)
    # Close drivers
    driver.close()
    driver.quit()
