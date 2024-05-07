import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains

extension = 'omghfjlpggmjjaagoclmmobgdodcjboh'


def newDRB(): 
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    chromeOptions.add_argument(
        "--load-extension=" +
        rf"C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default\Extensions\{extension}\3.84.1_0")
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)

    return driver
