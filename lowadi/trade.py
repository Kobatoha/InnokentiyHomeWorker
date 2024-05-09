from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains
import os
import random
from datetime import datetime
import time
from other import check_equus


def buy_marshadore():
    check_ufo()
    equus = check_equus()

    while equus == 'Good':
        check_ufo()
        time.sleep(0.1)
        equus = check_equus()

        url = ['https://www.lowadi.com/marche/vente/?chevalType=&chevalEspece=any-all&unicorn=2&pegasus=2&'
               'amountComparaison=g&amount=0&currency=soft&competencesComparaison=g&competences=0&race-cheval=&'
               'race-poney=&race-ane=&race-cheval-trait=&race-all=78&race-cheval-pegase=&race-poney-pegase=&'
               'race-cheval-licorne=&race-poney-licorne=&race-cheval-licorne-ailee=&race-poney-licorne-ailee=&'
               'race-cheval-trait-pegase=&race-cheval-trait-licorne=&race-cheval-trait-licorne-ailee=&race-ane-pegase=&'
               'race-ane-licorne=&race-ane-licorne-ailee=&chevalTypeRace=78&aneRaceId=49&ageComparaison=g&age=0&'
               'uniteAge=ans&sexe=femelle&genetiqueComparaison=g&genetique=0&pierre-philosophale=2&sablier-chronos=2&'
               'bras-morphee=2&pommeOr=2&pommeOrDisparue=2&rayonHelios=2&lyre-apollon=2&5th-element=2&fragment=2&'
               'jouvence=2&pack-poseidon=2&eleveur=&excellenceComparaison=g&excellence=0&blupComparaison=g&blup=-100&'
               'purete=1&rall=&r58=&r38=&r43=&r31=&r60=&r30=&r41=&r75=&r32=&r61=&r45=&r33=&r71=&r53=&r63=&r74=&r72=&'
               'r57=&r40=&r46=&r50=&r78=&r47=&r55=&r56=&r76=&r39=&r49=&r36=&r66=&r64=&r59=&r51=&r42=&r77=&r73=&r65=&'
               'r34=&r70=&r35=&r48=&r52=&r44=&r37=&r54=&r67=&r62=&moisNaissance=0&anneeNaissance=0&gestation=2&'
               'nbSaillie=2&hasCompanion=2&affixe=2&mesEncheres=2&bookmarks=2&classique=2&western=2&enduranceComparaison=g&'
               'endurance=0&vitesseComparaison=g&vitesse=0&dressageComparaison=g&dressage=0&galopComparaison=g&galop=0&'
               'trotComparaison=g&trot=0&sautComparaison=g&saut=0&cVictoiresComparaison=g&cVictoires=0&cFlotsComparaison=g&'
               'cFlots=0&distinctionGP=2&pack-nyx=2&caresse-philotes=2&don-hestia=2&citrouille-ensorcelee=2&'
               'sceau-apocalypse=2&chapeau-magique=2&double-face=2&livre-monstres=2&trail-riding-diary=2&catrina-brooch=2&'
               'esprit-nomade=2&diamond-apple=2&pomme-vintage=2&iris-coat=2&button-braided-mane=2&tail-braid-1=2&'
               'parade-apple=2&alexandre-dumas-inkwell=2&arthur-conan-doyle-inkwell=2&heracles-horseshoes=2&cloches=2&'
               'cravache=2&eperons=2&longe=2&crampons=2&bride=&selle=&tapis=&bonnet=&bande=&search=0&noFilter=1&advanced=0&'
               'tri=amount&sens=ASC&submit=']
        driver.get(url[0])
        first_price = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[3]/table/tbody/tr[1]/td[9]'
        ).text.replace(' ', ''))

        if first_price <= 3000 and equus == 'Good':
            driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[3]/table/tbody/tr[1]/td[9]/div/div[1]'
             ).click()
            alert.accept()
        time.sleep(0.5)
