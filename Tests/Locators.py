from selenium.webdriver.common.by import By

class Locator:
    #Регистрация
    #Поле Имя
    name_field = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    #Поле Email
    email_field = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    #Поле Пароль
    password_field = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    #Кнопка Зарегистрироваться
    button_registration = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')

    #Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
    #Кнопка "Войти в аккаунт"
    button_enter_to_account = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    #Кнопка Войти
    button_enter = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    #Кнопка Восстановить пароль
    button_recovery_password = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')
    #Кнопка перехода Конструктор
    button_constructor = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')
    #Кнопка Логотип Stellar Burgers
    logo_stella_burgers = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a/svg/path[6]')
    #Кнопка перехода - Булки
    button_bread = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')
    #Кнопка перехода - Соусы
    button_sauce = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
    #Кнопка перехода - Начинки
    button_filling = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')
    #Кнопка Выхода из аккаунта
    button_exit_from_account = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
    #Ошика при вводе неверного пароля
    invalid_password = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/p')