from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from utils import delay_until_show_text

PRELOGIN_URL = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fpruebas781%252Fhome%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D61f771d7369ed463cf1f3b78206bd902%26migrateGoogle%3D%26ssoVerified%3D&email=roger.ramos5%40unmsm.edu.pe&errorCode&login_hint=roger.ramos5%40unmsm.edu.pe&restrict=true"

def delay_until_show_text(driver, text):
  while(text not in driver.page_source):
    print("\tCargando página...")
    sleep(3)
  sleep(2)
  print("\t¡Página Cargada!")

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

# Click board
driver.find_element(By.CSS_SELECTOR , '#content > div > div.js-boards-page > div > div > div > div > div.all-boards > div > div > div > div.boards-page-board-section.mod-no-sidebar > div:nth-child(2) > ul > li:nth-child(1) > a > div')\
  .click()

delay_until_show_text(driver, "Test 1")

# Click filtrar
driver.find_element(By.CSS_SELECTOR , '#content > div > div.board-main-content > div.board-header.u-clearfix.js-board-header > div.board-header-btns.mod-right > span.js-brita-board-filter-btn-container.board-header-btn-react-container > div > div > button')\
  .click()

delay_until_show_text(driver, "Palabra clave")

filter_ipt = driver.find_element(By.CSS_SELECTOR, 'body > div.atlaskit-portal-container > div > section > div > div:nth-child(2) > input')
filter_ipt.send_keys("Prueba")

sleep(2)

els_todos = driver.find_elements(By.CSS_SELECTOR, '.list-card.js-member-droppable.ui-droppable')
els_hidden = driver.find_elements(By.CSS_SELECTOR, '.list-card.js-member-droppable.ui-droppable.hide')
cantidad_els_mostrandose = len(els_todos) - len(els_hidden)
print(f"Cantidad elementos mostrandose: {cantidad_els_mostrandose}")
if cantidad_els_mostrandose==3:
  print("Test Exitoso")
else:
  print("Test Fallo")