from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.openfactory42.org')
assert 'OpenFactory' in browser.title

elem = browser.find_element_by_class_name('icon-salient-search')  # Find the search link

elem = browser.find_element_by_class_name('icon-salient-search').click()

elem = browser.find_element_by_id('s') # Find the search box

elem.click()

elem.send_keys('imprimante' + Keys.RETURN)
