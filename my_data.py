user_name = 'Sergey'
password = '123456'
email = 'Sergey_Martinovsky_15_007@yandex.ru'
invalid_password = '6789'

import random
def gen_email():
    login_email = ''
    domain_email = 'yandex.ru'
    for _ in range (6):
        login_email += random.choice('abcdefghjiklmnopqrstuvwxyz1234567890')
    random_email= f"{login_email}@{domain_email}"
    return random_email
