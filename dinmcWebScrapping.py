from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

# dynamic web scrapping using selenium
def createDriver():
    # define route
    route = ChromeDriverManager(path="./chromedriver").install()

    # define service
    serv = Service(route)

    # define options
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    chr_options.add_argument(f"user-agent={user_agent}")
    chr_options.add_argument("--start-maximized")
    
    # disable same-origin-policy
    chr_options.add_argument("--disable-web-security") 
    chr_options.add_argument("--disable-extensions")
    chr_options.add_argument("--disable-notifications")

    # ignore secure connection modal    
    chr_options.add_argument("--ignore-certificate-errors")
    chr_options.add_argument("--no-sandbox")
    chr_options.add_argument("--log-level=3")
    chr_options.add_argument("--allow-running-insecure-content")
    chr_options.add_argument("--no-default-browser-check")

    # avoid unnecessary first time tasks
    chr_options.add_argument("--no-first-run")

    # direct connection
    chr_options.add_argument("--no-proxy-server")
    chr_options.add_argument("--disable-blink-features=AutomationControlled")

    except_opt = [
        'enable_automation',
        'ignore-certificate-errors',
        'enable-logging'
    ]

    pref = {
        "profile.default_content_setting_values.notifications": 2,
        "intl.accept_languages": ["es-ES", "es"],
        "credentials_enable_service": False
    }

    chr_options.add_experimental_option("excludeSwitches", except_opt)
    chr_options.add_experimental_option("prefs", pref)

    # instantiate driver
    driver = webdriver.Chrome(service=serv, options=chr_options)

    return driver

if __name__ == '__main__':
    url = "https://www.amazon.es/Elgato-Facecam-videoconferencia-enfoque-fijo-Zoom/dp/B0973DV11T/ref=psdc_937753031_t1_B08LVNYYZH"
    
    # initiate driver in url
    mydriver = createDriver()
    mydriver.get(url)
    mydriver.implicitly_wait(7)

    # get relevant data
    productName = mydriver.find_element(By.CSS_SELECTOR, "span#productTitle").text
    realPrice = mydriver.find_element(By.CSS_SELECTOR, "div#corePrice_feature_div").text.replace(",", ".")
    discount = mydriver.find_element(By.XPATH, "//div[@class='a-section a-spacing-none aok-align-center']/span[1]").text
    nReviews = mydriver.find_element(By.CSS_SELECTOR, "div#averageCustomerReviews").text

    print(nReviews)
