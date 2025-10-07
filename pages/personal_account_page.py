import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import USER_ACCOUNT_PAGE
import data



class PersonalAccountPage(BasePage):
    @allure.step('Переход на страницу аккаунта')
    def navigate_to_account_page(self):
        self.navigate_to_page(USER_ACCOUNT_PAGE)
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step('Авторизация в системе')
    def login_to_system(self, email, password):
        self.navigate_to_account_page()
        self.fill_field(AccountPageLocators.INPUT_EMAIL, email)
        self.fill_field(AccountPageLocators.INPUT_PASSWORD, password)
        self.click_on_element(AccountPageLocators.SIGNIN_BUTTON_FORM)
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)