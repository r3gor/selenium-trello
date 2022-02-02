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

driver.find_element(By.CSS_SELECTOR , '#content > div > div.js-boards-page > div > div > div > div > div.all-boards > div > div > div > div.boards-page-board-section.mod-no-sidebar > div:nth-child(2) > ul > li:nth-child(1) > a > div')\
  .click()

delay_until_show_text(driver, "Test 1")

driver.find_element(By.CSS_SELECTOR , '#content > div > div.board-main-content > div.board-header.u-clearfix.js-board-header > div.board-header-btns.mod-right > a.board-header-btn.mod-show-menu.js-show-sidebar > span.board-header-btn-text')\
  .click()

sleep(1)

driver.find_element(By.CSS_SELECTOR, '#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > ul:nth-child(2) > li:nth-child(5) > a')\
  .click()

sleep(1)

driver.find_element(By.CSS_SELECTOR, '#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > ul:nth-child(1) > li:nth-child(4) > a')\
  .click()

sleep(1)

els_archivados = driver.find_elements(By.CLASS_NAME, 'archived-list-card')
cantidad_els = len(els_archivados)

print(f"Cantidad de archivados {els_archivados}")
if cantidad_els >= 1:
  print("Test Exitoso")
else:
  print("Test Fallo")



