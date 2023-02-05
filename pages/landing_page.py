from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LandingPage(BasePage):
    
    LANDING_PAGE_URL = "https://paulcamper.com/rent-camper/"

    COOKIE_TITLE = (By.ID,"onetrust-policy-title")
    NECESSARY_COOKIES = (By.ID,"onetrust-reject-all-handler")

    VEHICLE_FILTER = (By.XPATH,"//span[@data-test-id='FilterCamperType']")
    SELECT_ALL_CHECKBOX = (By.XPATH,"//div[contains(text(),'Select all')]")
    BODY_STYLES_ALL_DESCRIPTIONS = (By.XPATH,"//div[contains(@class, 'typeDesc')]")
    BODY_STYLES_ALL_CHECKBOXES = (By.XPATH,"//input[@name='camper_type']")

    TOTAL_SEARCH_RESULTS = (By.XPATH,"//div[@data-test-id='camper-counter']/span")
    SEARCH_RESULTS_BUTTON = (By.XPATH,"(//button[@data-test-id='apply-filter'])[2]")
    
    def __init__(self, browser) -> None:
        super().__init__(browser)
    
    def accept_and_close_cookie_window(self):
        self.click_on_elem(self.COOKIE_TITLE)
        self.click_on_elem(self.NECESSARY_COOKIES)
        return self.is_element_disappeared(self.NECESSARY_COOKIES)
        
    def select_vehicle_dropdown_filter(self):
        self.click_on_elem(self.VEHICLE_FILTER)

    def check_select_all_option(self):
        self.click_on_elem(self.SELECT_ALL_CHECKBOX)

    def checkboxes_status(self, selected=True):
        cb_statuses = [self.wait_until_element_selected_status(ckbx, selected) for ckbx in self.browser.find_elements(*self.BODY_STYLES_ALL_CHECKBOXES)]
        return all(cb_statuses)
    
    def descriptions_status(self, selected=True):
        if selected:
            desc_statuses = bool(self.wait_until_elements_visible(self.BODY_STYLES_ALL_DESCRIPTIONS))
            return desc_statuses
        else:
            return None

    def get_search_count(self, elem):
        count = self.get_text(elem)
        count = count.split()[-3]
        count= str.replace(count,'.','',-1)
        return count


    
