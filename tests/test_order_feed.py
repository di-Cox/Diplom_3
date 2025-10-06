import allure
import data
from pages.home_page import HomePage
from pages.personal_account_page import PersonalAccountPage
from pages.order_feed_page import OrderFeedPage


@allure.feature('Основной функционал')
@allure.story('Тесты раздела Ленты заказов')
class TestOrderFeedPage:
    @allure.title('Тест увеличения счетчика "Выполнено за всё время"')
    def test_total_orders_counter_increase(self, driver):
        account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page = HomePage(driver)

        with allure.step('Авторизация в системе'):
            account_page.login_to_system()

        with allure.step('Переход в ленту заказов'):
            order_feed_page.click_order_feed_tab()

        with allure.step('Запись количества заказов за всё время'):
            orders_count_before = order_feed_page.get_total_orders_count()

        with allure.step('Создание заказа'):
            order_feed_page.click_constructor_tab()
            home_page.add_bun_to_constructor()
            home_page.add_sauce_to_constructor()
            order_feed_page.click_place_order_button()

        with allure.step('Закрытие окна с деталями заказа'):
            order_feed_page.wait_and_get_order_number()
            order_feed_page.click_close_order_modal()

        with allure.step('Переход в ленту заказов'):
            order_feed_page.click_order_feed_tab()

        with allure.step('Проверка количества заказов за всё время'):
            orders_count_after = order_feed_page.get_total_orders_count()

        with allure.step('Проверка увеличения счетчика'):
            assert orders_count_after > orders_count_before, \
                f"Ожидалось увеличение счетчика. Было: {orders_count_before}, стало: {orders_count_after}"

    @allure.title('Тест увеличения счетчика "Выполнено за сегодня"')
    def test_today_orders_counter_increase(self, driver):
        account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page = HomePage(driver)

        with allure.step('Авторизация в системе'):
            account_page.login_to_system()

        with allure.step('Переход в ленту заказов'):
            order_feed_page.click_order_feed_tab()

        with allure.step('Запись количества заказов за сегодня'):
            orders_count_before = order_feed_page.get_today_orders_count()

        with allure.step('Создание заказа'):
            order_feed_page.click_constructor_tab()
            home_page.add_bun_to_constructor()
            home_page.add_sauce_to_constructor()
            order_feed_page.click_place_order_button()

        with allure.step('Закрытие окна с деталями заказа'):
            order_feed_page.wait_and_get_order_number()
            order_feed_page.click_close_order_modal()

        with allure.step('Переход в ленту заказов'):
            order_feed_page.click_order_feed_tab()

        with allure.step('Проверка количества заказов за сегодня'):
            orders_count_after = order_feed_page.get_today_orders_count()

        with allure.step('Проверка увеличения счетчика'):
            assert orders_count_after > orders_count_before, \
                f"Ожидалось увеличение счетчика. Было: {orders_count_before}, стало: {orders_count_after}"

    @allure.title('Тест отображения заказа в разделе "В работе"')
    def test_order_in_progress_section(self, driver):
        account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page = HomePage(driver)

        with allure.step('Авторизация в системе'):
            account_page.login_to_system()

        with allure.step('Создание заказа'):
            order_feed_page.click_constructor_tab()
            home_page.add_bun_to_constructor()
            home_page.add_sauce_to_constructor()
            order_feed_page.click_place_order_button()

        with allure.step('Получение номера созданного заказа'):
            order_number = order_feed_page.wait_and_get_order_number()
            order_feed_page.click_close_order_modal()

        with allure.step('Переход в ленту заказов'):
            order_feed_page.click_order_feed_tab()

        with allure.step('Проверка номера заказа в разделе "В работе"'):
            is_order_in_progress = order_feed_page.check_order_in_progress_section(order_number)

        with allure.step('Проверка совпадения номеров заказов'):
            assert is_order_in_progress, \
                f"Ожидалось, что номер заказа {order_number} будет в разделе 'В работе'"



