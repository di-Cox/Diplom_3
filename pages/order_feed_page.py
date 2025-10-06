import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators






class OrderFeedPage(BasePage):
    @allure.step('Клик по вкладке "Конструктор"')
    def click_constructor_tab(self):
        self.wait_for_element_hidden(OrderFeedPageLocators.MODAL_OVERLAY_SECTION)
        self.wait_for_element_hidden(OrderFeedPageLocators.MODAL_OVERLAY_DIV)
        self.wait_for_element_visible(OrderFeedPageLocators.CONSTRUCTOR_TAB)
        self.click_on_element(OrderFeedPageLocators.CONSTRUCTOR_TAB)
        self.wait_for_element_visible(OrderFeedPageLocators.CONSTRUCTOR_PAGE_TITLE)


    @allure.step('Клик по вкладке "Лента заказов"')
    def click_order_feed_tab(self):
        self.wait_for_element_hidden(OrderFeedPageLocators.MODAL_OVERLAY_SECTION)
        self.wait_for_element_hidden(OrderFeedPageLocators.MODAL_OVERLAY_DIV)
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_TAB)
        self.click_on_element(OrderFeedPageLocators.FEED_TAB)
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_PAGE_TITLE)


    @allure.step('Получение общего количества заказов')
    def get_total_orders_count(self):
        count = self.get_text_from_element(OrderFeedPageLocators.ALL_TIME_ORDERS_COUNT)
        return int(count)


    @allure.step('Получение количества заказов за сегодня')
    def get_today_orders_count(self):
        count = self.get_text_from_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT)
        return int(count)


    @allure.step('Проверка номера заказа в разделе "В работе"')
    def check_order_in_progress_section(self, order_number):
        self.wait_for_element_visible(OrderFeedPageLocators.CURRENT_ORDERS_LIST)
        order_text = self.get_text_from_element(OrderFeedPageLocators.CURRENT_ORDERS_LIST)
        return order_number in order_text


    @allure.step('Получение номера заказа в разделе "В работе"')
    def get_order_number_in_progress(self):
        order_text = self.get_text_from_element(OrderFeedPageLocators.CURRENT_ORDERS_LIST)
        return order_text


    @allure.step('Клик по кнопке оформления заказа')
    def click_place_order_button(self):
        self.click_on_element(OrderFeedPageLocators.PLACE_ORDER_BTN)


    @allure.step('Клик по кнопке закрытия модального окна заказа')
    def click_close_order_modal(self):
        self.click_on_element(OrderFeedPageLocators.CLOSE_ORDER_MODAL)


    @allure.step('Ожидание и получение номера заказа')
    def wait_and_get_order_number(self):
        order_element = self.wait_for_text_change(OrderFeedPageLocators.ORDER_ID_MODAL, '9999')
        order_number = f'{int(order_element.text):07d}'
        return order_number
