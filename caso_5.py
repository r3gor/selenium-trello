from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from utils import delay_until_show_text

PRELOGIN_URL = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fpruebas781%252Fhome%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D61f771d7369ed463cf1f3b78206bd902%26migrateGoogle%3D%26ssoVerified%3D&email=roger.ramos5%40unmsm.edu.pe&errorCode&login_hint=roger.ramos5%40unmsm.edu.pe&restrict=true"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.get(PRELOGIN_URL)

sleep(2)

driver.find_element(By.ID, "password")\
  .send_keys("VandV2022")
driver.find_element(By.ID, "login-submit")\
  .click()

delay_until_show_text(driver, "Tableros")

driver.get("https://trello.com/search")

find_ipt = driver.find_element(By.CSS_SELECTOR , '#content > div:nth-child(1) > div > input')
find_ipt.send_keys("Exam Final")

delay_until_show_text(driver, "Tableros")

els = driver.find_elements(By.CSS_SELECTOR, '.compact-board-tile')
cantidad_els = len(els)

if cantidad_els == 2:
  print("Test Exitoso")
else:
  print("Test Fallo")