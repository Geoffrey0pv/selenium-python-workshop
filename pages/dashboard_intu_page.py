from selenium.webdriver.common.by import By
from .base_page import BasePage  # Importamos la clase BasePage


class dashboard_intu_page(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-action='search']")


    def is_search_field_displayed(self):
        return self.find_element(self.SEARCH_FIELD).is_displayed()

    def get_welcome_message(self):
        return self.find_element(self.WELCOME_MESSAGE).text

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
        return self.driver.current_url