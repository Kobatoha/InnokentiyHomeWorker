import time
import pretty_errors
from datetime import datetime
from selenium.webdriver.common.by import By
import random


def personally_ufo_list():
    pufos = {
        'Keanu Reeves': ['Набор Никты', 'https://www.lowadi.com/joueur/fiche/?id=13066244'],
        'Delirium': ['Длани Морфея', 'https://www.lowadi.com/joueur/fiche/?id=14617033'],
        'rossi': ['Винтажное яблоко', 'https://www.lowadi.com/joueur/fiche/?id=11822262'],
        'Мad Hatter': ['Винтажное яблоко', 'https://www.lowadi.com/joueur/fiche/?id=13149545'],
        'Mignonette': ['Винтажное яблоко', 'https://www.lowadi.com/joueur/fiche/?id=16250375'],
        'Lonn': ['Слезы Афродиты', 'https://www.lowadi.com/joueur/fiche/?id=14079930'],
        'Mr.Robot': ['Слезы Афродиты', 'https://www.lowadi.com/joueur/fiche/?id=15290760'],
        'микаэла.': ['Слезы Афродиты', 'https://www.lowadi.com/joueur/fiche/?id=13901654'],
        'IrinaRoys': ['Слезы Афродиты', 'https://www.lowadi.com/joueur/fiche/?id=11684880'],
        'Petunya': ['Посох плодовитости', 'https://www.lowadi.com/joueur/fiche/?id=11631646'],
        'AlexNic': ['Посох плодовитости', 'https://www.lowadi.com/joueur/fiche/?id=15736714'],
        'Фишка2': ['Посох плодовитости', 'https://www.lowadi.com/joueur/fiche/?id=11772648'],
        'Илион': ['Кровь Медузы', 'https://www.lowadi.com/joueur/fiche/?id=12025847'],
        'Landlord': ['Кровь Медузы', 'https://www.lowadi.com/joueur/fiche/?id=14295425'],
        'xiao': ['Бонус-набор', 'https://www.lowadi.com/joueur/fiche/?id=13001842'],
        'sdssd': ['Черная орхидея', 'https://www.lowadi.com/joueur/fiche/?id=16303641'],
        'Nansy': ['Черная орхидея', 'https://www.lowadi.com/joueur/fiche/?id=11501551'],

        'Layfhozich': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=15709011'],
        'Nadyas93': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=12133906'],
        'швар': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=13545002'],
        'Сат': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=13244894'],
        'Римуру': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=16072890'],
        'Наяда': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=14673969'],
        'Osinka': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=12118685'],
        'аrcher': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=16043043'],
        '※Şwěèţ Đřęåm※': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=15904190'],
        'ДиЗа': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=15688756'],
        'НиаКриС': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=12438693'],
        'Novokem': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=12134091'],
        'Бревно': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=15737187'],
        'Ferrum': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=13075102'],
        'Karamba.t': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=16274712'],
        'АлинаХ': ['Папирус Плутоса', 'https://www.lowadi.com/joueur/fiche/?id=12654035'],

        'Anato': ['Черно-белый налобник 2**', 'https://www.lowadi.com/joueur/fiche/?id=13300548'],
        'Талъинка': ['Черно-розовый налобник 2**', 'https://www.lowadi.com/joueur/fiche/?id=16234313'],
        'шатенка': ['Зеленый классический вальтрап 2**', 'https://www.lowadi.com/joueur/fiche/?id=13252451'],
        'Lorani': ['Розовые бинты 2**', 'https://www.lowadi.com/joueur/fiche/?id=12771917'],
        'Night': ['Черные бинты 2**', 'https://www.lowadi.com/joueur/fiche/?id=11514153'],
        'Северчанка': ['Зеленые бинты 2**', 'https://www.lowadi.com/joueur/fiche/?id=11874839'],
        'sweta310': ['Розовые бинты 2**', 'https://www.lowadi.com/joueur/fiche/?id=13137754'],

        'BlackDog': ['Одеяло Гипноса', 'https://www.lowadi.com/joueur/fiche/?id=12764045'],
        'Nene4ka': ['Одеяло Гипноса', 'https://www.lowadi.com/joueur/fiche/?id=11722306'],
        '.bluenevada': ['Одеяло Гипноса', 'https://www.lowadi.com/joueur/fiche/?id=15883910'],
        'annechka': ['Одеяло Гипноса', 'https://www.lowadi.com/joueur/fiche/?id=11679256'],
        'Авантюра new': ['Одеяло Гипноса', 'https://www.lowadi.com/joueur/fiche/?id=15272090'],
        'Магесса': ['Одеяло Гипноса', 'https://www.lowadi.com/joueur/fiche/?id=12039911'],
        'Boxerka 53': ['Одеяло Гипноса', 'https://www.lowadi.com/joueur/fiche/?id=15811176'],
        'marishka2006': ['Лира Аполлона', 'https://www.lowadi.com/joueur/fiche/?id=13627601'],
        'ENIGMA666': ['Лира Аполлона', 'https://www.lowadi.com/joueur/fiche/?id=11797567'],
        'Zero05': ['Лира Аполлона', 'https://www.lowadi.com/joueur/fiche/?id=15828861'],
        'сандравит': ['Лира Аполлона', 'https://www.lowadi.com/joueur/fiche/?id=12473582'],
        'Koshko': ['Богатство Креза', 'https://www.lowadi.com/joueur/fiche/?id=11593636'],
        'галакси': ['Богатство Креза', 'https://www.lowadi.com/joueur/fiche/?id=11932942'],
        'Aziza1992': ['Стрела Артемиды', 'https://www.lowadi.com/joueur/fiche/?id=12395746'],
        'Olesya': ['Стрела Артемиды', 'https://www.lowadi.com/joueur/fiche/?id=15770180'],

        'brosse': ['Корда', 'https://www.lowadi.com/joueur/fiche/?id=16113089'],
        'Mckee': ['Корда', 'https://www.lowadi.com/joueur/fiche/?id=16140685'],
        'Джули16': ['Шипы', 'https://www.lowadi.com/joueur/fiche/?id=11713598'],
        'блумм111': ['Шипы', 'https://www.lowadi.com/joueur/fiche/?id=11872158'],
        'дажд': ['Шпоры', 'https://www.lowadi.com/joueur/fiche/?id=11878569'],
        'вилуна': ['Шпоры', 'https://www.lowadi.com/joueur/fiche/?id=11844856'],
        'Ландыш': ['Ногавки', 'https://www.lowadi.com/joueur/fiche/?id=16191151'],
        'Темный Властелин': ['3*** Классическая уздечка', 'https://www.lowadi.com/joueur/fiche/?id=14937887'],
        'Eagles': ['3*** Классическое седло', 'https://www.lowadi.com/joueur/fiche/?id=12316969'],

        'Джул': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=11616811'],
        'rainastik': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16296658'],
        'Leareth': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=11753215'],
        'Полина Окель': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16188853'],
        'Seong Hwa': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16244706'],
        'THE METRO': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16302609'],
        'Markiz de Pomm': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=12619435'],
        'Деким': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16168931'],
        'Лэйлика': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13317932'],
        'Newly': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13362034'],
        'Догма': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13641807'],
        'Лилеанна': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=12044566'],
        'Му-му': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=12053829'],
        'Хурма1234': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16220563'],
        'Юрашик': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13212747'],
        'Texxi': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16239148'],
        'Tschassa': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13415996'],
        'Ангелина1402': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13460763'],
        'panky.': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13059769'],
        'Lapsiinja_LV': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=13398767'],
        'Солнышко я': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=12786727'],
        'Mister Rebel': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16209035'],
        'ASPERa': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=11995496'],
        'GЕRDА': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16308583'],
        'додик': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=15355092'],
        'Vashaki': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16018857'],
        'Katja': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=12874091'],
        'Lula': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=12882945'],
        '~Багирка~': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=11597486'],
        'wIK': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=15558355'],
        'ОльКо': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=11555235'],
        'Dragonija': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16275746'],
        'Meteliz': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16303327'],
        'Тигра': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16316021'],
        'Sumi': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16294726'],
        'Dz. Ell.': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=12756991'],
        'dwaekki': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16282135'],
        'Vaylis.': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16150528'],
        'Noch': ['Очки роста', 'https://www.lowadi.com/joueur/fiche/?id=16168849'],

        'Roswell 47': ['Семена пропуска', 'https://www.lowadi.com/joueur/fiche/?id=11662957'],
        'Baykuş': ['Семена пропуска', 'https://www.lowadi.com/joueur/fiche/?id=11565254'],
        'Ольга1703': ['Семена пропуска', 'https://www.lowadi.com/joueur/fiche/?id=11718336']
    }

    return pufos


def ufo_list():
    noir_ufo = {
        'pomme-vintage': 'Винтажное яблоко',
        'lyre-apollon': 'Лира Аполлона',
        'orchidee-noire': 'Черная орхидея',
        'fleche-artemis': 'Стрела Артемиды',
        'bras-morphee': 'Длани Морфея',
        'couverture-hypnos': 'Одеяло Гипноса',
        'larmes-aphrodite': 'Слезы Афродиты',
        'pactole-cresus': 'Богатство Креза',
        'pack-nyx': 'Набор Никты',
        'parchemin-ploutos': 'Папирус Плутоса',
        'sang-meduse': 'Кровь Медузы',
        'baton-fertilite': 'Посох плодовитости',
        'bonnet-2x-noir-blanc': 'Черно-белый налобник 2**',
        'bonnet-2x-noir-rose': 'Черно-розовый налобник 2**',
        'tapis-classique-2x-vert': 'Зеленый классический вальтрап 2**',
        'bande-2x-rose': 'Розовые бинты 2**',
        'bande-2x-noir': 'Черные бинты 2**',
        'bande-2x-vert': 'Зеленые бинты 2**',
        'graines-pass': 'Семена пропуска'
    }

    good_ufo = {
        'vieillissement': 'Очки роста'
    }

    bad_ufo = {
        'pomme': 'яблоко',
        'carotte': 'морковь',
        'classique': 'седло',
        'mash': 'комбикорм',
        'equus': 'экю'
    }

    return good_ufo, bad_ufo


def find_rating_urls(driver):
    rating_lists = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section'
    )
    urls = []
    users = rating_lists.find_elements(By.CLASS_NAME, 'usergroup_2')
    for user in users:
        url = user.get_attribute('href')
        urls.append(url)

    return set(urls)


def find_personally_pufo_hands(driver):
    url = driver.current_url
    table = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/table/tbody/tr[2]'
    ).text.split('\n')
    nickname = table[0]
    pufo = ''
    for tr in table:
        if 'Сейчас: ' in tr:
            pufo = tr[8:]
    if pufo:
        return {nickname: [pufo, url]}
    return 'Индивидуальные НЛО отсутствуют'


def find_personally_pufo_in_rating(driver):
    urls = find_rating_urls(driver)
    for url in urls:
        driver.get(url)
        table = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/table/tbody/tr[2]'
        ).text.split('\n')
        nickname = table[0]
        pufo = ''
        for tr in table:
            if 'Сейчас: ' in tr:
                pufo = tr[8:]
        if pufo:
            result = {nickname: [pufo, url]}
            print(result)


def check_personally_ufo(driver):
    pufos = personally_ufo_list()
    for url in pufos:
        driver.get(pufos[url][1])
        time.sleep(2)
        try:
            if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]'):
                alarm = input('Я что-то нашел на персональной странице игрока с Индивидуальными НЛО, нужна помощь!')

                finded_ufo = driver.find_element(
                    By.XPATH,
                    '/html/body/div[12]'
                ).text.split('\n')[1]
                print(finded_ufo)
        except:
            pass


def check_ufo(driver):

    good_ufo = {'vieillissement': 'очки роста'}
    bad_ufo = {'pomme': 'яблоко', 'carotte': 'морковь', 'classique': 'седло', 'mash': 'комбикорм',
               'equus': 'экю'}
    try:

        if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]'):
            icon = driver.find_element(By.XPATH, '/html/body/div[1]/img').get_attribute('src')

            for bad_key in bad_ufo:
                if bad_key in icon:
                    print(f"НЛО: {bad_ufo[bad_key]}, надо скипнуть")
                    driver.refresh()

            for good_key in good_ufo:
                if good_key in icon:
                    print(f"НЛО: {good_ufo[good_key]}, надо брать")
                    driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="agi-10972849001709751854"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '/html/body/div[12]/aside/div[2]/button/span/span').click()
                    driver.refresh()
                    time.sleep(1)

            driver.get(driver.current_url)
            time.sleep(2)

    except:

        return


def check_equus(driver):
    try:
        equus = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/header/nav[1]/ul/li[8]/a/span/span[2]/strong'
        ).text.replace(' ', ''))

        if equus >= 10000:
            return 'Good'
        else:
            return 'Bad'
    except:
        driver.refresh()
        time.sleep(2)
        check_equus(driver)


def get_resurses(driver, name):
    resurses = {
        'wood': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[2]/td[5]/button/span/span/span/img'
        ),
        'iron': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[3]/td[5]/button/span/span/span/img'
        ),
        'sand': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[4]/td[5]/button/span/span/span/img'
        ),
        'skin': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[5]/td[5]/button/span/span/span/img'
        ),
        'straw': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[7]/td[5]/button/span/span/span/img'
        ),
        'flax': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[8]/td[5]/button/span/span/span/img'
        ),
        'wheat': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[10]/td[5]/button/span/span/span/img'
        ),
    }
    return resurses[name]


def spend_equus(driver, res='skin'):
    try:
        equus = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/header/nav[1]/ul/li[8]/a/span/span[2]/strong'
        ).text.replace(' ', ''))
        driver.get('https://www.lowadi.com/marche/boutique')
        time.sleep(1)
        resurses = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/ul/li[3]/div/a/img'
        ).click()
        time.sleep(3)
        iron = 10
        if equus >= 66000:
            driver.get('https://www.lowadi.com/centre/pres/')
            time.sleep(2)
            fields = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[3]'
                '/div/div[1]/div/ul/li[1]/span[4]/button/span/span/span/img'
            ).click()
            time.sleep(2)
            big_field = driver.find_element(
                By.XPATH,
                '/html/body/div[11]/div/div/div[2]/form/ul/li[3]/span[1]/input'
            ).click()
            time.sleep(1)
            buy_field = driver.find_element(
                By.XPATH,
                '/html/body/div[11]/div/div/div[2]/form/div/div/div/button/span/span/span'
            ).click()
        else:
            while equus > 10000:
                get_resurses(driver, res).click()
                time.sleep(1)
                quality = driver.find_element(
                    By.XPATH,
                    '/html/body/div[11]/div/div/table/tbody/tr[1]/td[1]/select/option[21]'
                ).click()
                time.sleep(1)
                confirm = driver.find_element(
                    By.XPATH,
                    '/html/body/div[11]/div/div/table/tbody/tr[1]/td[1]/button/span[2]'
                ).click()
                time.sleep(1)
                equus = int(driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/header/nav[1]/ul/li[8]/a/span/span[2]/strong'
                ).text.replace(' ', ''))
                time.sleep(1)

        driver.back()
    except:
        time.sleep(3)
        spend_equus(driver)


def login_lowadi(driver):
    now = datetime.now().strftime('%H:%M:%S')
    print(f'{now}: Логинимся на lowadi.com')
    url = 'https://www.lowadi.com'

    driver.get(url)

    try:
        print('Принимаем cookie')
        driver.find_element(By.XPATH, '/html/body/aside/div/article/div/div[2]/div/div/div[3]/form/button').click()

    except:
        print('Принять cookie не просили')

    try:

        print(f'Начинаем!')
        driver.find_element(By.XPATH, '/html/body/div[7]/header/nav/div/strong').click()
        time.sleep(2)
        if driver.find_element(By.XPATH, '//*[@id="login"]').text == '':
            print(f'Вводим логин..')
            login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
            time.sleep(1)
            print(f'Вводим пароль..')
            password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
            time.sleep(1)
        print(f'Входим')
        connect = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/header/nav/div/div/form/button/span/span/span'
        ).click()
        time.sleep(2)

    except:

        url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=20378769'
        driver.get(url)

        print(f'Пробуем зайти заново')
        time.sleep(10)
        if driver.find_element(By.XPATH, '//*[@id="login"]').text == '':
            print(f'Вводим логин..')
            login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
            time.sleep(1)
            print(f'Вводим пароль..')
            password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
            time.sleep(1)
            print(f'Входим')
        connect = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/aside/form/button'
        ).click()
        time.sleep(10)


def xanthos(driver):
    """
    Ежедневная глажка 5 Ксанфов.
    Есть вероятность получить рог изобилия.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=1045736',
        'https://www.lowadi.com/elevage/fiche/?id=1047131',
        'https://www.lowadi.com/elevage/fiche/?id=1044747',
        'https://www.lowadi.com/elevage/fiche/?id=1044960',
        'https://www.lowadi.com/elevage/fiche/?id=1046269'
    ]
    print('Гладим Ксанфов')
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_xanthos = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]'
            '/div/div/div/div/div/div[1]/table/tbody/tr/td[3]/form/a'
        ).click()
        time.sleep(2)


def topaz(driver):
    """
    Ежедневная глажка 5 Топазов.
    Есть вероятность получить 10 пропусков.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=4763736',
        'https://www.lowadi.com/elevage/fiche/?id=4775333',
        'https://www.lowadi.com/elevage/fiche/?id=4771120',
        'https://www.lowadi.com/elevage/fiche/?id=4792032',
        'https://www.lowadi.com/elevage/fiche/?id=4789329'
    ]
    print('Гладим Топазов')
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_topaz = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]'
            '/div/div/div/div/div/div[1]/table/tbody/tr/td[3]/form/a'
        ).click()
        time.sleep(2)


def givre(driver):
    """
    Ежедневная разморозка Морозницы.
    Есть вероятность получить Одеяло Гипноса.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=12086505'
    ]
    print('Размораживаем Морозницу')
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_givre = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]/'
            'div/div/div/div/div/div[1]/table/tbody/tr/td[3]/a'
        ).click()
        time.sleep(2)


def atelier(driver, workshop=3):
    print(datetime.now().strftime('%H:%M:%S'), 'Проверяем мастерские..')
    url = 'https://www.lowadi.com/centre/atelier/'
    driver.get(url)
    try:
        for _ in range(workshop):
            try:
                get_stable_1 = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/form/table/tbody/tr[6]/td[6]/a/span'
                )
            except:
                get_stable_1 = driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/form/table/tbody/tr[6]/td[6]/a/span'
                )

            match get_stable_1.text:
                case 'Получить':
                    print('Стойла готовы, собираем')
                    get_stable_1.click()
                    time.sleep(2)
                    try:
                        driver.find_element(
                            By.XPATH,
                            '/html/body/div[11]/div/div/form/button/span/span/span'
                        ).click()
                    except:
                        driver.find_element(
                            By.XPATH,
                            '/html/body/div[12]/div/div/form/button/span/span/span'
                        ).click()
                    time.sleep(2)
                case 'Стоп':
                    print('Стойла не готовы, сваливаем')
                    return 0

        for _ in range(workshop):
            begin_stable = driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/form/table/tbody/tr[1]/td[6]/button/span/span/span'
            )
            match begin_stable.text:
                case 'Производство':
                    print('Мастерская свободна, пора запускать постройку стойла')
                    begin_stable.click()
                    time.sleep(2)
                    driver.find_element(
                        By.XPATH,
                        '/html/body/div[12]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div/span'
                    ).click()
                    time.sleep(2)
                    driver.find_element(
                        By.XPATH,
                        '/html/body/div[12]/div/div/div/div/div/div/div[2]/form[8]/div[2]/button/span/span/span'
                    ).click()
                    time.sleep(2)

    except:
        print('Проверка мастерской провалилась')


def refresh(driver):
    driver.refresh()
    time.sleep(2)


def quit_lowadi(driver):
    print(f'{datetime.now().strftime("%H:%M:%S")}: закрываем chrome')
    driver.quit()
