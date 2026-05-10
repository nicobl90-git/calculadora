import pytest

#fixtures

#acá traigo los fixtures que trabajé en selenium_test.py, ya que son datos fijos 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture 
def chrome_driver(): #esta funcion estara ligada al driver
    #instalo el servicio del driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #como toda funcion retorna algo, le digo que me retorne el driver
    yield driver #yield es como un return, pero no corta o interrumpe la funcion, sino que sigue ejecutando el codigo que esta debajo del yield. Es decir, el codigo que esta debajo del yield se ejecuta despues de que se termine de usar el driver
    driver.quit()
     
