import get_driver


def handle_driver_brave(main_app):
    print('Кнопка driver_brave нажата!')
    main_app.driver = get_driver.new_brave_dr()
    print('Драйвер создан:', main_app.driver)


def handle_driver_chrome(main_app):
    print('Кнопка driver_chrome нажата!')
    main_app.driver = get_driver.new_drb()
    print('Драйвер создан:', main_app.driver)


def handle_female_andalus():
    print('Кнопка female_andalus нажата!')


def handle_male_andalus():
    print('Кнопка male_andalus нажата!')


def handle_unicorn_andalus():
    print('Кнопка unicorn_andalus нажата!')


def handle_competitions_andalus():
    print('Кнопка competitions_andalus нажата!')


def handle_blup_baium():
    print('Кнопка blup_baium нажата!')


def handle_female_marshadore():
    print('Кнопка female_marshadore нажата!')


def handle_male_marshadore():
    print('Кнопка male_marshadore нажата!')


def handle_heavy():
    print('Кнопка heavy нажата!')


def count_horses():
    return 1
