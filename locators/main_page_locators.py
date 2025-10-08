from selenium.webdriver.common.by import By



class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//header/nav//a//p[contains(text(), 'Конструктор')]")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    CREATE_ORDER_BTN = (By.XPATH, "//main//button[contains(text(), 'Оформить заказ')]")
    PROFILE_LINK = (By.XPATH, "//header//a//p[contains(text(), 'Личный Кабинет')]")

    ORDER_FEED_TAB = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

    BUN_ITEM = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    SAUCE_ITEM = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")

    INGREDIENT_POPUP_TITLE = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    CLOSE_POPUP_BTN = (By.XPATH, "//div[contains(@class,'modal__container')]//button[contains(@class,'modal__close')]")

    DROP_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
    SAUCE_COUNT = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']/preceding-sibling::div/p")
    BUN_COUNT = (By.XPATH, "//img[@alt='Краторная булка N-200i']/preceding-sibling::div/p")
