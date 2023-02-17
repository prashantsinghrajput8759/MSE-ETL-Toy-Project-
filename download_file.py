from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import base

def download_file(xpath1,xpath2):

    #object of ActionChains
    a = ActionChains(base.driver)
    #identify element
    m = base.driver.find_element(by="xpath", value=xpath1)
    #hover over element
    a.move_to_element(m)
    #identify sub menu element
    n =base.driver.find_element(by="xpath", value=xpath2)
    # hover over element and click
    a.move_to_element(n).click().perform()
