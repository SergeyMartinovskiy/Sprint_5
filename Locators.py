from selenium.webdriver.common.by import By

class Locator:
    #Регистрация
    #Поле Имя
    name_field = (By.XPATH, ".//input[@name='name']")
    #Поле Email
    email_field = (By.XPATH, ".//label[text()='Email']/input[@class ='text input__textfield text_type_main-default']")
    #Поле Пароль
    password_field = (By.XPATH, ".//input[@name='Пароль']")
    #Кнопка Зарегистрироваться (после ввода данных в поля Имя, почта, пароль)
    button_registration = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    # Активная надпись Зарегистрироваться (Новый пользователь)
    sign_registration = (By.XPATH,'//*[@id="root"]/div/main/div/div/p[1]/a')

    #Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
    #Кнопка "Войти в аккаунт"
    button_enter_to_account = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    #Кнопка Войти
    button_enter = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    #Активная надпись Восстановить пароль
    sign_recovery_password = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')
    #Кнопка Восставноить пароль после ввода пароля
    button_recovery_password = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    #Кнопка перехода Конструктор
    button_constructor = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')
    #Кнопка Логотип Stellar Burgers
    logo_stella_burgers = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a/svg/path[6]')
    #Кнопка перехода - Булки
    button_bread = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')
    #Кнопка перехода - Соусы
    button_sauce = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
    #Кнопка перехода - Начинки
    button_topping = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')
    #Кнопка Выхода из аккаунта
    button_exit_from_account = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
    #Ошибка при вводе неверного пароля
    invalid_password = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/p')
    #Проверка текста Вход (Проверка выхода из аккаунта)
    text_enter_in_account = (By.XPATH, '//*[@id="root"]/div/main/div/h2')
    #Проверка перехода в личный кабинет через текст "Профиль" на странице Личного кабинета
    text_profile_in_personal_account = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a')
    #Проверка перехода по кнопке Конструктор текстом "Соберите бургер"
    text_in_page_constructor= (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
    #Проверка перехода по кнопке Логотипа - текстом "Оформить заказ"
    text_in_main_page = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    #Выбранная секция в конструкторе
    choose_section_of_item = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")
    #Текст Соус на странице выбора вариантов Соуса (Конструктор)
    text_sauce_in_scroll = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
    #Текст Начинки на странице выбора вариантов начинок (Конструктор)
    text_topping_in_scroll = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')
    #Текст Хлеб на странице выбора вариантов Хлеба (Конструктор)
    text_bread_in_scroll = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')
    #Кнопка пересохранения пароля
    button_resave_password = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    #Некорректный пароль
