import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.web_driver.current_url

    @allure.step('Переход по URL')
    def navigate_to_page(self, url):
        self.web_driver.get(url)

    @allure.step("Клик по элементу")
    def click_on_element(self, locator, wait_time=10):
        element = WebDriverWait(self.web_driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator, wait_time=10):
        element = self.wait_for_element_visible(locator, wait_time)
        self.web_driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator, wait_time=10):
        WebDriverWait(self.web_driver, wait_time).until(EC.visibility_of_element_located(locator))
        return self.web_driver.find_element(*locator)

    @allure.step("Ожидание скрытия элемента")
    def wait_for_element_hidden(self, locator, wait_time=10):
        return WebDriverWait(self.web_driver, wait_time).until_not(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание присутствия элемента")
    def wait_for_element_present(self, locator, wait_time=10):
        WebDriverWait(self.web_driver, wait_time).until(EC.presence_of_element_located(locator))
        return self.web_driver.find_element(*locator)

    @allure.step("Ввод текста в поле")
    def fill_field(self, locator, text_value, wait_time=10):
        element = self.wait_for_element_visible(locator, wait_time)
        element.clear()
        element.send_keys(text_value)

    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locator, wait_time=10):
        element = self.wait_for_element_visible(locator, wait_time)
        return element.text

    @allure.step("Получение CSS свойства")
    def get_css_value(self, locator, property_name, wait_time=10):
        element = self.wait_for_element_present(locator, wait_time)
        return element.value_of_css_property(property_name)

    @allure.step("Получение атрибута элемента")
    def get_attribute_value(self, locator, attribute_name, wait_time=10):
        element = self.wait_for_element_present(locator, wait_time)
        return element.get_attribute(attribute_name)

    @allure.step("Ожидание значения в атрибуте")
    def wait_for_attribute_contains(self, locator, attribute, expected_value, wait_time=10):
        return WebDriverWait(self.web_driver, wait_time).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, expected_value)
        )

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        self.web_driver.switch_to.window(self.web_driver.window_handles[1])

    @allure.step('Перетаскивание элемента')
    def perform_drag_and_drop(self, source_element, target_element):
        drag_and_drop(self.web_driver, source_element, target_element)

    @allure.step('Проверка отображения элемента')
    def check_element_displayed(self, locator):
        try:
            element = self.wait_for_element_visible(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step('Ожидание изменения текста элемента')
    def wait_for_text_change(self, locator, initial_text, timeout=30):
        WebDriverWait(self.web_driver, timeout).until(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.wait_for_element_visible(locator)

    @allure.step("Клик по элементу через JavaScript")
    def click_via_javascript(self, locator, wait_time=10):
        element = WebDriverWait(self.web_driver, wait_time).until(
            EC.presence_of_element_located(locator)
        )
        self.web_driver.execute_script("arguments[0].click();", element)