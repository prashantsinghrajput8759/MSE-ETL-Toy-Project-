import selenium
import time
import downloaded
import download_2
from selenium.webdriver.common.keys import Keys
import os
import rename
import page_loaded
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()

#download dirctory change
def download_directory_set(path):
    dir="G:\toy_etl_project\masters_data"
    prefs = {"download.default_directory" : r"G:\toy_etl_project\masters_data","directory_upgrade": True}
    
    options.add_experimental_option("prefs" , prefs)
    driver = webdriver.Chrome(service=Service(), options=options)
   # dir=os.path.join("G:\toy_etl_project\masters_data",path)
    
    



options.add_experimental_option("detach", True)
    



driver = webdriver.Chrome(service=Service(), options=options)