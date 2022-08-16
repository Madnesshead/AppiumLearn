import time

from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723/wd/hub'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '14.5',
    'deviceName': 'iPhone 12 Pro Max',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS,
)
try:
    time.sleep(5)
    print(driver.page_source)
finally:
    driver.quit()
