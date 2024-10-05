from selenium.webdriver.common.by import By
from .base_page import BasePage  # Importamos la clase BasePage


class login_intu_page(BasePage):
    USERNAMEFIELD = (By.ID, 'username')
    PASSWORDFIELD = (By.ID, 'password')
    LOGINBUTTON =  (By.ID, 'loginbtn') 

    def login(self, username, password):
        self.enter_text(self.USERNAMEFIELD, username)
        self.enter_text(self.PASSWORDFIELD, password)
        self.click(self.LOGINBUTTON)
        return self.driver.current_url