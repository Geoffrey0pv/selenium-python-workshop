from behave import given, when, then
from selenium import webdriver
from pages.dashboard_intu_page import dashboard_intu_page
from pages.login_intu_page import login_intu_page  

@given('I am on the login page')
def step_user_is_in_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.icesi.edu.co/moodle/login/index.php')
    context.login_intu_page = login_intu_page(context.driver)

@when('Ingreso mis credenciales y presiono el boton para loguearme')
def step_user_logs_in(context):
    context.dashboard_intu_page = dashboard_intu_page(context.driver)
    context.dashboard_intu_page = context.login_intu_page.login('', '')


@Then('Then el logueo es exitoso y se redirige el usuario a la pagina del dashboard de mi usuario')
def step_user_is_logged_in(context):
    dashboard_intu_page = dashboard_intu_page(context.driver)
    assert context.dashboard_intu_page.is_search_field_displayed() == True
    context.driver.quit()