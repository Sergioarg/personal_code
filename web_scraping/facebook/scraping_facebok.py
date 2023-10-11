""" Selenium module for automatization login and logout in tawk. """
# Selenium
from datetime import datetime as date
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Options for chrome ──────────────────────────────────────────────────────────
coptions = webdriver.ChromeOptions()
coptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=coptions)
wait = WebDriverWait(driver, 240)


def login_facebook(user: str, password: str):

    facebook_url = "https://www.facebook.com/"

    driver.get(facebook_url)

    input_user = '//*[@id="email"]'
    input_password = '//*[@id="pass"]'

    # Login
    driver.find_element(By.XPATH, input_user).send_keys(user)
    driver.find_element(By.XPATH, input_password).send_keys(password)
    driver.find_element(By.NAME, "login").click()

    # Click en market place
    driver.find_element(By.XPATH, '//*[@id="mount_0_0_I4"]/div/div[1]/div/div[2]/div[4]/div/div[1]/div[1]/ul/li[3]/span/div/a').click()

    search = 'Honda CB650R'
    input_marketplace = driver.find_element(By.XPATH, '//*[@id="mount_0_0_I4"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/span/div/div/div/div/label/input')
    input_marketplace.send_keys(search)
    input_marketplace.send_keys(Keys.RETURN)

    # Results
    grid_results = '//*[@id="mount_0_0_I4"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]'
    results = driver.find_element(By.XPATH, grid_results)

    # Close drivers
    driver.close()
    driver.quit()


if __name__ == '__main__':
    user = 'correo_falso@gmail.com'
    password = 'constraseña'
    login_facebook(user, password)
