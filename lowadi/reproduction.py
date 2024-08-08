import time
import os
import pretty_errors
from selenium.webdriver.common.by import By
from lowadi.other import check_ufo, check_equus


def ready_matt(driver):
    try:
        not_ready = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'
        ).text
        print(not_ready)
        time.sleep(1)

        return False

    except:

        if driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Случить кобылу':

            return [True, 0]

        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Открытые случки':

            print('Кобыле продложена случка')

            return [True, 1]

        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Эхография':

            print('Кобыла уже жеребая')
            time.sleep(1)

            return False


def female_reproduction(driver):
    matting = ready_matt(driver)



def female_andalusian(driver, current_url):

    matting = ready_matt(driver)

    if matting and matting[1] == 0:

        print('Нужна случка, идем на брачный рынок..')
        check_ufo(driver)
        driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
        time.sleep(1)
        master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
        time.sleep(1)
        get_offers = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/button[1]/span/span'
        ).click()
        time.sleep(1)
        gp_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[4]/div/a').click()
        time.sleep(1)
        get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
        time.sleep(1)

        if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:
            mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
            time.sleep(1)

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    else:

        return 0


def male_andalusian(driver):
    time.sleep(1)
    mating = 25
    num = 0
    name = get_name_horse(driver)
    gp = int(name.split()[1][:-3])

    try:

        for i in range(5):
            energie = int(driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[2]'
                '/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
            ).text)
            if energie - mating >= 20:
                create_mating = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
                )
                try:
                    create_mating.click()
                    time.sleep(1)
                    open_mating = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[1]/input'
                    ).click()
                    choice_equus = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select'
                    ).click()
                    time.sleep(2)
                    if gp >= 11555:
                        lower_price = driver.find_element(
                            By.XPATH,
                            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                            '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[13]'
                        ).click()
                        time.sleep(1)
                    else:
                        lower_price = driver.find_element(
                            By.XPATH,
                            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                            '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[9]'
                        ).click()
                        time.sleep(1)
                    complete = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span'
                    ).click()
                    time.sleep(5)

                    num += 1

                except:
                    return num

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_horse')

        return 0


def female_andalusian_elite_mating(driver):
    matting = ready_matt(driver)

    if matting and matting[1] == 1:

        male_name = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
        ).text
        print(f'Принимаем случку от {male_name}')

        ok = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
            '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
        ).click()

        check_ufo(driver)

        mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
        time.sleep(1)

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    elif matting and matting[1] == 0:

        name = get_name_horse(driver)

        with open('lowadi/Lists of horses/andalusian.txt', 'r') as file:
            names = file.readlines()

        if name + '\n' not in names:
            with open('lowadi/Lists of horses/andalusian.txt', 'a') as file:
                file.write(name + '\n')

            print('Добавлена в очередь на ожидание случки')
        else:
            print('Уже в очереди на ожидание случки')

        return 0

    else:

        return 0


def male_andalusian_elite_mating(driver):

    mating = 25
    num = 0
    name = get_name_horse(driver)
    energy = get_energy(driver)

    count = energy // mating

    try:
        while count != 0:
            with open('lowadi/Lists of horses/andalusian.txt', 'r') as file:
                females = file.readlines()

            if not females:
                return num

            use_mating = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
            ).click()
            time.sleep(2)

            choice_reservation = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[3]/input'
            ).click()
            time.sleep(2)

            send_name = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/input'
            ).send_keys(f'{females[0][:-1]}')
            time.sleep(1)

            watch = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/button/span/span/span'
            ).click()
            time.sleep(1)

            complete = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span/span/span'
            ).click()
            time.sleep(3)

            with open('lowadi/Lists of horses/andalusian.txt', 'w') as file:
                for female in females[1:]:
                    file.write(female)

            num += 1
            count -= 1

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_andalusian_elite_mating')

        return num


def female_marshadore(driver, current_url):
    matting = ready_matt(driver)

    if matting and matting[1] == 1:

        male_name = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
        ).text
        print(f'Принимаем случку от {male_name}')

        ok = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
            '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
        ).click()

        check_ufo(driver)

        mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
        time.sleep(1)

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    elif matting and matting[1] == 0:

        name = get_name_horse(driver)

        with open('lowadi/Lists of horses/marshadore.txt', 'r') as file:
            names = file.readlines()

        if name + '\n' not in names:
            with open('lowadi/Lists of horses/marshadore.txt', 'a') as file:
                file.write(name + '\n')

            print('Добавлена в очередь на ожидание случки')
        else:
            print('Уже в очереди на ожидание случки')

        return 0

    else:

        return 0


def male_marshadore(driver):

    mating = 25
    num = 0
    name = get_name_horse(driver)
    energy = get_energy(driver)

    count = energy // mating

    try:
        while count != 0:
            with open('lowadi/marshadore.txt', 'r') as file:
                females = file.readlines()

            if not females:
                return num

            use_mating = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
            ).click()
            time.sleep(2)

            choice_reservation = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[3]/input'
            ).click()
            time.sleep(2)

            send_name = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/input'
            ).send_keys(f'{females[0][:-1]}')
            time.sleep(1)

            watch = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/button/span/span/span'
            ).click()
            time.sleep(1)

            complete = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span/span/span'
            ).click()
            time.sleep(3)

            with open('lowadi/marshadore.txt', 'w') as file:
                for female in females[1:]:
                    file.write(female)

            num += 1
            count -= 1

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_marshadore')

        return num


def female_andalusian_unicorn_mating(driver, current_url):
    matting = ready_matt(driver)

    if matting and matting[1] == 1:

        male_name = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
        ).text
        print(f'Принимаем случку от {male_name}')

        ok = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
            '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
        ).click()

        check_ufo(driver)

        mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
        time.sleep(1)

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    elif matting and matting[1] == 0:

        name = get_name_horse(driver)

        with open('lowadi/andalusian_unicorn.txt', 'r') as file:
            names = file.readlines()

        if name + '\n' not in names:
            with open('lowadi/andalusian_unicorn.txt', 'a') as file:
                file.write(name + '\n')

            print('Добавлена в очередь на ожидание случки')
        else:
            print('Уже в очереди на ожидание случки')

        return 0

    else:

        return 0


def male_andalusian_unicorn_mating(driver):

    mating = 25
    num = 0
    name = get_name_horse(driver)
    energy = get_energy(driver)

    count = energy // mating

    try:
        while count != 0:
            with open('lowadi/andalusian_unicorn.txt', 'r') as file:
                females = file.readlines()

            if not females:
                return num

            use_mating = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
            ).click()
            time.sleep(2)

            choice_reservation = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[3]/input'
            ).click()
            time.sleep(2)

            send_name = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/input'
            ).send_keys(f'{females[0][:-1]}')
            time.sleep(1)

            watch = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/button/span/span/span'
            ).click()
            time.sleep(1)

            complete = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span/span/span'
            ).click()
            time.sleep(3)

            with open('lowadi/andalusian_unicorn.txt', 'w') as file:
                for female in females[1:]:
                    file.write(female)

            num += 1
            count -= 1

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_andalusian_unicorn_mating')

        return num
