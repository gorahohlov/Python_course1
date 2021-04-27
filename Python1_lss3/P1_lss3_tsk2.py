# 2. -------------------------------

def brief_info(name, surname, birth_year, city, email, mobile):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город проживания: {city}, Электронная почта: {email}, Мобильный телефон: {mobile}')
    print('----')
    print(f' \
        Имя: {name}\n \
        Фамилия: {surname}\n \
        Год рождения: {birth_year}\n \
        Город проживания: {city}\n \
        Электронная почта: {email}\n \
        Мобильный телефон: {mobile}\
        ')
    return

brief_info(mobile = '01234567890', email = 'gorahohlov@gmail.com', city = 'Saint-Petersburg', birth_year = 1977, surname = 'Hohlov', name = 'Vladislav')
