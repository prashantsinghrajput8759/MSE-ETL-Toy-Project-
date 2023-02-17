import base

# function to wait until page is loaded 
def seleniumPageLoad(self, path):
    

    try:

        ele = base.WebDriverWait(base.driver, 10).until(  # using explicit wait for 10 seconds
            base.EC.presence_of_element_located((base.By.XPATH, path)))  # checking for the element with xpath
        # print("Page is loaded within 10 seconds.")

    except Exception as error:
        print("Timeout Exception: Page did not load within 10 seconds.")
