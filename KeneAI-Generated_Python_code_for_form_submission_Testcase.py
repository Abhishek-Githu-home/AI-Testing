
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None
    driver.implicitly_wait(6)

    # Step - 1 : Open URL https://rahulshettyacademy.com/loginpagePractise/
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(6)

    # Step - 2 : Type rahulshettyacademy in Username input field
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'rahulshettyacademy':
            element.send_keys(char)
    else:
        element.send_keys('rahulshettyacademy')
    driver.implicitly_wait(6)

    # Step - 3 : type ***************** in Password input field
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'Learning@830$3mK2':
            element.send_keys(char)
    else:
        element.send_keys('Learning@830$3mK2')
    driver.implicitly_wait(6)

    # Step - 4 : Click Admin radio button
    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Click I Agree to the terms and conditions checkbox
    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 6 : Click Sign In button
    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 7 : Wait 2 seconds for login to complete
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 8 : Check ProtoCommerce Home heading visibility → {{dashboard_visible}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 9 : Assert {{dashboard_visible}} equals true
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 10 : Open URL http://rahulshettyacademy.com/angularpractice/
    driver.get("http://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(6)

    # Step - 11 : Type John Doe in Name input field
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'John Doe':
            element.send_keys(char)
    else:
        element.send_keys('John Doe')
    driver.implicitly_wait(6)

    # Step - 12 : Type john@example.com in Email input field
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'john@example.com':
            element.send_keys(char)
    else:
        element.send_keys('john@example.com')
    driver.implicitly_wait(6)

    # Step - 13 : type *********** in Password input field
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'password123':
            element.send_keys(char)
    else:
        element.send_keys('password123')
    driver.implicitly_wait(6)

    # Step - 14 : Click Love IceCreams checkbox
    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 15 : Click Student employment status radio button
    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 16 : Scroll window down slightly to reveal rest of form
    driver.execute_script(f"scroll_height = 1*window.innerHeight; window.scrollBy(0, scroll_height)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 17 : Click Submit button
    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 18 : Check success banner text → {{form_success_text}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 19 : Assert {{form_success_text}} contains The Form has been submitted successfully
    'This Instruction Is Carried Out By The Vision Model'

    driver.quit()
except Exception as e:
    driver.quit()
