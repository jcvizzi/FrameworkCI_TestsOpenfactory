# -*-coding:Latin-1 -*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

browser.set_window_size(1200, 600)

browser.implicitly_wait(5)

browser.get('http://www.openfactory42.org')
assert 'OpenFactory' in browser.title

wait = WebDriverWait(browser, 10)

page_presentation = browser.find_element_by_partial_link_text('Présentation').click()

time.sleep(0.5)

url_test_result = browser.current_url

print(url_test_result)

if "http://www.openfactory42.org/presentation/" in url_test_result:

	message = 'La page de présentation a été trouvée !'

	print(message)
else:

	message = 'La page de présentation n\'a pas été trouvée !'

	print(message)

