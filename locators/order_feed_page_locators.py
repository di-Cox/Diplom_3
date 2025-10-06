from selenium.webdriver.common.by import By



class OrderFeedPageLocators:
    PLACE_ORDER_BTN = (By.XPATH, "//main//button[contains(text(), 'Оформить заказ')]")
    FEED_TAB = (By.XPATH, "//header//a//p[contains(text(),'Лента Заказов')]")
    FEED_PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

    CONSTRUCTOR_TAB = (By.XPATH, "//header//a//p[contains(text(),'Конструктор')]")
    CONSTRUCTOR_PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    ACCOUNT_LINK = (By.XPATH, "//header//a//p[contains(text(), 'Личный Кабинет')]")

    RECENT_ORDER = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]/a/div")

    ALL_TIME_ORDERS_COUNT = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")

    ORDER_ID_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")
    CLOSE_ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")

    CURRENT_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]")
    ORDER_ID_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[contains(@class,'text_type_digits')]")

    PAGE_HEADER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")

    LOADING_OVERLAY = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")
    MODAL_OVERLAY_SECTION = (By.XPATH, "//section[contains(@class,'Modal_modal__P3_V5')]")
    MODAL_OVERLAY_DIV = (By.XPATH, "//div[contains(@class,'Modal_modal__P3_V5')]")
    