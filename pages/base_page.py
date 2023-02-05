from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotInteractableException

class BasePage:
    
    EXPLICIT_WAIT_TIMEOUT = 20
    IMPLICIT_WAIT_TIMEOUT = 10

    def __init__(self, browser) -> None:
        self.browser = browser

    def _wait(self):
        return WebDriverWait(self.browser, self.EXPLICIT_WAIT_TIMEOUT)
    
    def wait_until_element_located(self, elem):
        return self._wait().until(EC.presence_of_element_located(elem))

    def wait_until_element_clickable(self,elem):
        return self._wait().until(EC.element_to_be_clickable(elem))

    def wait_until_elements_visible(self,elem):
        return self._wait().until(EC.visibility_of_all_elements_located(elem))
    
    def wait_until_element_visible(self,elem):
        return self._wait().until(EC.visibility_of_element_located(elem))

    # def is_element_invisible(self,elem):
    #     return self._wait().until(EC.invisibility_of_element_located(elem))
    
    def wait_until_element_selected_status(self,elem,tf):
        return self._wait().until(EC.element_selection_state_to_be(elem,is_selected=tf))
    
    def load(self, pageurl):
            self.browser.get(pageurl)
            self.browser.implicitly_wait(self.IMPLICIT_WAIT_TIMEOUT)

    def get_text(self,elem):
        return self.wait_until_element_located(elem).text

    def click_on_elem(self,elem):
        self.wait_until_element_clickable(elem).click()
    
    def is_element_disappeared(self, elem):
        is_disappeared = WebDriverWait(self.browser, self.EXPLICIT_WAIT_TIMEOUT, 1, (ElementNotVisibleException,ElementNotInteractableException)).until_not(lambda x: x.find_element(*elem).is_displayed())
        return is_disappeared

    

