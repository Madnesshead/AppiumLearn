from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    wait = WebDriverWait(driver, timeout=10)
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys('Hello')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
    saved_text = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
    assert saved_text == 'Hello'
    driver.back()
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    saved_text = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'savedMessage'))).text
    assert saved_text == 'Hello'
finally:
    driver.quit()
