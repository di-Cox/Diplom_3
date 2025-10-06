from selenium.webdriver.common.by import By



class AccountPageLocators:
    SIGNIN_BUTTON_MAIN = (By.XPATH, "//main//button[contains(text(), 'Войти в аккаунт')]")
    INPUT_EMAIL = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")
    INPUT_PASSWORD = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")
    SIGNIN_BUTTON_FORM = (By.XPATH, "//form[contains(@class, 'Auth_form')]//button[contains(text(), 'Войти')]")

    SIGNOUT_BUTTON = (By.XPATH, "//nav//button[contains(text(), 'Выход')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    COMPLETED_ORDER_STATUS = (By.XPATH, "//p[contains(text(),'Выполнен')]")
    SIGNIN_FROM_TITLE = (By.XPATH, "//h2[contains(text(),'Вход')]")
    MAIN_PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")



