from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class element_has_disappear(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, locator, xpath):
    self.locator = locator
    self.xpath = xpath

  def __call__(self, driver):
    try:
        print "Searching for ", self.xpath
        element = driver.find_element_by_xpath(self.xpath)
        return False
    except:
        return True

count=1
for i in range(0,count):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://int-196-pos9cokkies-flow.api.development.2delivery.co/bogota')
    driver.maximize_window()
    driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")


#try:

    elem = '/html/body/div[6]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    elem = '//*[@id="terminos_fb"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    ######Datos Usuario#################
    elem = '//*[@id="UsuarioEmail"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.send_keys("jrodriguez@clickdelivery.com")

    elem = '//*[@id="UsuarioPassword"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.send_keys("jrodriguez@clickdelivery.com")


    elem = '//*[@id="UsuarioLoginForm"]/button'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()
    driver.get('http://int-196-pos9cokkies-flow.api.development.2delivery.co/bogota')

    ###Ingresar Direccion Restauran###

    elem = '//*[@id="Buscar"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )

    elem = '//*[@id="dir1"]/option[2]'
    element = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.XPATH, elem))
    )

    elem = '//*[@id="dir2"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.send_keys("94")

    elem = '//*[@id="dir3"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.send_keys("16")

    elem = '//*[@id="dir4"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.send_keys("60")

    elem = '//*[@id="Buscar"]/input[5]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()
################################################################################
######Don Chihuhua
################################################################################
    #Escoger establecimeinto
    elem = '//*[@id="establecimiento-19308"]/li/div[3]/div[1]/div/div'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    ## Haga click sobre comida
    elem = '//*[@id="187851"]/div[2]/div[1]/div[2]'
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    #Selccionar Ingredientes###
    elem = '//*[@id="255596"]'
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    elem = '//*[@id="menuConfigModal"]/div/div/div[2]/div[2]/div'
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    ## Confirmar Pedido
    elem = '//*[@id="cart"]/div[2]/div/div'
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()
###############################################################################
###Mr Broos
################################################################################
    #Escoger establecimeinto
    #elem = '//*[@id="establecimiento-19980"]/li/div[3]/div[1]/div/div'
    #element = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, elem))
    #)
    #element.click()

    ## Haga click sobre comida
    #elem = '//*[@id="293899"]/div[2]/div[1]/div[2]'
    #element = WebDriverWait(driver, 30).until(
    #    EC.element_to_be_clickable((By.XPATH, elem))
    #)
    #element.click()

    ## Confirmar Pedido
    #elem = '//*[@id="cart"]/div[2]/div/div'
    #element = WebDriverWait(driver, 30).until(
    #    EC.element_to_be_clickable((By.XPATH, elem))
    #)
    #element.click()
###############################################################################
    ##Ingresar Comentario
    elem = '//*[@id="site"]/div/div/div[2]/div/div[5]/textarea'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.send_keys("Prueba NUNCA PREPARAR")

    #Pago EN casa   #
    elem = '//*[@id="ProductoCarritoForm"]/div[3]/div[2]/label[1]'
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    elem = '//*[@id="ProductoBillete"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.send_keys("200000")

    elem = '//*[@id="ProductoTerminos"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    elem = '//*[@id="EnviarFormulario"]'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )
    element.click()

    elem = '//*[@id="site"]/div/div[1]/div/div/h1'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, elem))
    )

    #n=raw_input("Hola bb")
    driver.save_screenshot('screenshot.png')


#finally:
#    driver.quit()
    #n=raw_input("Hola bb")
