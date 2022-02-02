from time import sleep

def delay_until_show_text(driver, text):
  while(text not in driver.page_source):
    print("\tCargando página...")
    sleep(3)
  sleep(2)
  print("\t¡Página Cargada!")