#Importing necessary libraries

import base
#wait for page load function
def seleniumPageLoad(self,path):
    #creating a webdriver object
    
    try:
        ele = base.WebDriverWait(base.driver, 10).until( #using explicit wait for 2 seconds
        base.EC.presence_of_element_located((base.By.XPATH, path)) #checking for the element with xpath 
    )
        print("Page is loaded within 10 seconds.")
    except:

        print("Timeout Exception: Page did not load within 10 seconds.")
        

