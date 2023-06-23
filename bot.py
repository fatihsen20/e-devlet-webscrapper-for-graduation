import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from dotenv import load_dotenv
from mail_send import send_mail
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

def chrome_options(WINDOW_SIZE):
    """
    This function creates chrome options for headless mode.

    Args:
        WINDOW_SIZE (str): Window size for headless mode.

    Returns:
        Object: Chrome options for headless mode.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    return chrome_options

def create_driver(WINDOW_SIZE):
    """
    This function creates chrome driver.

    Args:
        WINDOW_SIZE (str): Window size for headless mode.

    Returns:
        Object: Chrome driver.
    """
    options = chrome_options(WINDOW_SIZE)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def main():
    WINDOW_SIZE = "1920,1080"
    driver = create_driver(WINDOW_SIZE)
    # driver getting url
    driver.get("https://giris.turkiye.gov.tr/Giris/gir")
    # driver getting elements
    tc = driver.find_element(By.ID, "tridField")
    password = driver.find_element(By.ID, "egpField")
    login_button = driver.find_element(By.NAME, "submitButton")
    # I'm fetching os elements from .env file
    tc_value = os.environ.get("tc")
    password_value = os.environ.get("e_password")
    # I'm sending values to elements
    tc.send_keys(tc_value)
    password.send_keys(password_value)
    # I'm clicking login button
    login_button.click()
    # driver getting grad. url
    driver.get("https://www.turkiye.gov.tr/yuksekogretim-mezun-belgesi-sorgulama")
    # The reason for adding sleep here is that the page can take a long time to load.
    time.sleep(30)
    try:
        # I'm getting warning container text
        driver.find_element(By.CLASS_NAME, "warningContainer").text
    except:
        # If there is no warning container, it means that the certificate is ready.
        subject = "Mezuniyet Belgesi Durumu"
        message = "Tebrikler, Mezun Oldunuz!"
        # I'm sending mail
        send_mail(os.environ.get("from_mail"), os.environ.get("mail_password"), os.environ.get("to_mail"), subject, message)
    # I'm closing driver
    driver.close()

if __name__ == "__main__":
    main()

