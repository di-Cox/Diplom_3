import allure

from locators.main_page_locators import MainPageLocators
from pages.home_page import HomePage







@allure.feature("Основной функционал")
@allure.story("Тест функционала главной страницы 'Stellar Burgers'")
class TestMainPage:
    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_constructor_navigation(self, driver):
        home_page = HomePage(driver)

        with allure.step('Открытие страницы входа'):
            home_page.navigate_to_account_page()

        with allure.step('Нажатие на "Конструктор"'):
            home_page.click_constructor_tab()

        with allure.step('Проверка отображения раздела "Собери бургер"'):
            assert home_page.check_construction_section_displayed(), 'Раздел "Собери бургер" не отображается!'


    @allure.title("Проверка перехода по клику на раздел «Лента заказов»")
    def test_order_feed_navigation(self, driver):
        home_page = HomePage(driver)

        with allure.step('Открытие страницы входа'):
            home_page.navigate_to_account_page()

        with allure.step('Нажатие на "Ленту заказов"'):
            home_page.click_order_feed_tab()

        with allure.step('Проверка отображения раздела "Лента заказов"'):
            assert home_page.check_order_feed_section_displayed(), 'Раздел "Лента заказов" не отображается'


    @allure.title("Тест открытия попапа с деталями ингредиента")
    def test_ingredient_details_popup(self, driver):
        home_page = HomePage(driver)

        with allure.step('Открытие главной страницы'):
            home_page.navigate_to_main_page()

        with allure.step('Нажатие на ингредиент "Краторная булка N-200i"'):
            home_page.click_ingredient_item()

        with allure.step('Проверка отображения попапа с деталями'):
            assert home_page.check_ingredient_details_displayed(), 'Попап с деталями ингредиента не отображается'


    @allure.title("Тест закрытия попапа с деталями ингредиента")
    def test_ingredient_details_popup_close(self, driver):
        home_page = HomePage(driver)

        with allure.step('Открытие главной страницы'):
            home_page.navigate_to_main_page()

        with allure.step('Нажатие на ингредиент "Краторная булка N-200i"'):
            home_page.click_ingredient_item()

        with allure.step('Нажатие на крестик в попапе'):
            home_page.click_close_popup_button()

        with allure.step('Проверка закрытия попапа'):
            assert home_page.check_ingredient_details_closed(), 'Попап с деталями ингредиента не закрылся'


    @allure.title("Тест увеличения счетчика ингредиента при добавлении")
    def test_ingredient_counter_increase(self, driver):
        home_page = HomePage(driver)

        with allure.step('Открытие главной страницы'):
            home_page.navigate_to_main_page()

        with allure.step('Получение счетчика соусов до добавления'):
            count_before = home_page.get_ingredient_counter_value()

        with allure.step('Добавление соуса в конструктор'):
            home_page.add_sauce_to_constructor()

        with allure.step('Получение счетчика соусов после добавления'):
            count_after = home_page.get_ingredient_counter_value()

        with allure.step('Проверка увеличения счетчика'):
            assert count_after > count_before, 'Счетчик ингредиента не увеличился после добавления'
