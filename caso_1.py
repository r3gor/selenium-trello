from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


PRELOGIN_URL = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fpruebas781%252Fhome%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D61f771d7369ed463cf1f3b78206bd902%26migrateGoogle%3D%26ssoVerified%3D&email=roger.ramos5%40unmsm.edu.pe&errorCode&login_hint=roger.ramos5%40unmsm.edu.pe&restrict=true"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.get(PRELOGIN_URL)

sleep(2)

pwd_ipt = driver.find_element(By.ID, "password")
pwd_ipt.send_keys("VandV2022")
login_btn = driver.find_element(By.ID, "login-submit")
login_btn.click()

while("Tableros" not in driver.page_source):
  print("\tCargando...")
  sleep(3)
sleep(3)
print("Cargado!")

tablero = driver.find_element(By.CSS_SELECTOR , '#content > div > div.js-boards-page > div > div > div > div > div.all-boards > div > div > div > div.boards-page-board-section.mod-no-sidebar > div:nth-child(2) > ul > li:nth-child(1) > a > div')
tablero.click()

while("Test 1" not in driver.page_source):
  print("\tCargando...")
  sleep(3)
sleep(3)
print("Cargado!")

tarjeta = driver.find_element(By.CSS_SELECTOR, '#board > div.js-list.list-wrapper > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > a:nth-child(1) > div.list-card-details.js-card-details > span')
action.context_click(tarjeta).perform()

archivar = driver.find_element(By.CSS_SELECTOR, '#chrome-container > div.quick-card-editor > div > div.quick-card-editor-buttons.fade-in > a.quick-card-editor-buttons-item.js-archive > span.quick-card-editor-buttons-item-text')
archivar.click()

sleep(2)
try:
  tarjeta.text
  print("Test Fallo")
except StaleElementReferenceException:
  print("Test Exitoso")

