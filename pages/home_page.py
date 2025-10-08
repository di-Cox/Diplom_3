import allure
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import USER_ACCOUNT_PAGE, SITE_URL




class HomePage(BasePage):
    @allure.step('Переход на страницу аккаунта')
    def navigate_to_account_page(self):
        self.navigate_to_page(USER_ACCOUNT_PAGE)
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TAB)


    @allure.step('Переход на главную страницу')
    def navigate_to_main_page(self):
        self.navigate_to_page(SITE_URL)
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TAB)


    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_tab(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_TAB)


    @allure.step('Проверка отображения раздела "Конструктор"')
    def check_construction_section_displayed(self):
        return self.check_element_displayed(MainPageLocators.CONSTRUCTOR_TITLE)


    @allure.step('Клик по кнопке Лента заказов')
    def click_order_feed_tab(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_TAB)


    @allure.step('Проверка отображения раздела "Лента заказов"')
    def check_order_feed_section_displayed(self):
        return self.check_element_displayed(MainPageLocators.ORDER_FEED_TITLE)


    @allure.step('Клик по ингредиенту')
    def click_ingredient_item(self):
        self.click_on_element(MainPageLocators.BUN_ITEM)


    @allure.step('Проверка отображения попапа с деталями ингредиента')
    def check_ingredient_details_displayed(self):
        element = self.wait_for_element_visible(MainPageLocators.INGREDIENT_POPUP_TITLE)
        return element.is_displayed()


    @allure.step('Проверка закрытия попапа с деталями ингредиента')
    def check_ingredient_details_closed(self):
        try:
            self.wait_for_element_hidden(MainPageLocators.CLOSE_POPUP_BTN)
            return True
        except TimeoutException:
            return False


    @allure.step('Клик по кнопке закрытия попапа')
    def click_close_popup_button(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_BTN)


    @allure.step('Скролл к соусу')
    def scroll_to_sauce_ingredient(self):
        self.click_ingredient_item(MainPageLocators.SAUCE_ITEM)


    @allure.step('Клик по кнопке оформить заказ')
    def click_create_order_button(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BTN)


    @allure.step('Получение счетчика ингредиента')
    def get_ingredient_counter_value(self):
        return self.get_text_from_element(MainPageLocators.SAUCE_COUNT)


    @allure.step('Добавление булки в конструктор')
    def add_bun_to_constructor(self):
        self.check_construction_section_displayed()
        ingredient = self.wait_for_element_visible(locator=MainPageLocators.BUN_ITEM)
        drop_area = self.wait_for_element_visible(locator=MainPageLocators.DROP_AREA)
        self.perform_drag_and_drop(source_element=ingredient, target_element=drop_area)


    @allure.step('Добавление соуса в конструктор')
    def add_sauce_to_constructor(self):
        self.check_construction_section_displayed()
        ingredient = self.wait_for_element_visible(locator=MainPageLocators.SAUCE_ITEM)
        drop_area = self.wait_for_element_visible(locator=MainPageLocators.DROP_AREA)
        self.perform_drag_and_drop(source_element=ingredient, target_element=drop_area)
