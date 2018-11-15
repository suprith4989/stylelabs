# Author: Suprith Gangawar <sgangawa@redhat.com>

try:
    import os
    from behave import when, then
    from selenium import webdriver
    import paramiko
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait, Select
    from selenium.webdriver.support import expected_conditions as EC
except ImportError as e:
    print("{0} failed to import one or more dependencies, as indicated below:\n{1}: {2}".format(__name__, e.__class__, e))
    sys.exit(1)

@given('I open google in browser')
def step_impl(context):
# This will pick the required URL from the settings.yml file
    context.browser.get("http://" + context.data['development']['common']['google']['uri'])
#    alert = context.browser.switch_to_alert()
#    alert.accept()

@when('I search for Bahamas')
def step_impl(context):

    #webdriver wait function is used here to avoid failures due to network latency.
#It will wait till the element expected is visible in the web page and use it once observed.

    search1 = webdriver.support.ui.WebDriverWait(context.browser, 8200).until(
            webdriver.support.expected_conditions.visibility_of_element_located((
                webdriver.common.by.By.XPATH,"//input[@id='lst-ib']")))

#clear() function below is used to clear any text already present in the text box to avoid redundancy.
    search1.clear()
    search1.send_keys('Bahamas')
    context.browser.find_element_by_xpath("//input[@value='Google Search']").click()

@when('I ensure I have arrived on the Bahamas result page')
def step_impl(context):
    search2 = webdriver.support.ui.WebDriverWait(context.browser, 8200).until(
            webdriver.support.expected_conditions.visibility_of_element_located((
                webdriver.common.by.By.XPATH,"//div[@class='FxvUNb kno-ecr-pt kno-fb-ctx']//span[contains(text(),'Bahamas')]")))
    assert search2.text == 'Bahamas'

@when('I take a screenshot of result page')
def step_impl(context):
    context.browser.get_screenshot_as_file('/tmp/google.png')

@when('I search for Amsterdam')
def step_impl(context):
    search3 = webdriver.support.ui.WebDriverWait(context.browser, 8200).until(
            webdriver.support.expected_conditions.visibility_of_element_located((
                webdriver.common.by.By.XPATH,"//input[@id='lst-ib']")))
    search3.clear()
    search3.send_keys('Amsterdam')
    context.browser.find_element_by_xpath("//button[@id='mKlEF']").click()

@then('I ensure I have arrived on Amsterdam the result page')
def step_impl(context):
    searchx = webdriver.support.ui.WebDriverWait(context.browser, 8200).until(
            webdriver.support.expected_conditions.visibility_of_element_located((
                webdriver.common.by.By.XPATH,"//div[@class='FxvUNb kno-ecr-pt kno-fb-ctx']//span[contains(text(),'Amsterdam')]")))
    assert searchx.text == 'Amsterdam'

@given('I navigate to expedia website')
def step_impl(context):
    context.browser.get("https://" + context.data['development']['common']['expedia']['uri'])

@when('I look for a flight+accommodation from Brussels to New York')
def step_impl(context):
    search4 = webdriver.support.ui.WebDriverWait(context.browser, 8200).until(
            webdriver.support.expected_conditions.visibility_of_element_located((
                webdriver.common.by.By.XPATH,"//input[@id='package-origin-hp-package']")))
    search4.send_keys('Brussels')

    search5 = context.browser.find_element_by_xpath("//input[@id='package-destination-hp-package']")
    search5.send_keys('Newyork')
    
    search6 = context.browser.find_element_by_xpath("//input[@id='package-departing-hp-package']")
    search6.send_keys('12/15/2018')

    search7 = context.browser.find_element_by_xpath("//input[@id='package-returning-hp-package']")
    search7.send_keys('12/18/2018')
    
    search8 = context.browser.find_element_by_xpath("//button[@id='search-button-hp-package']")
    search8.click()

@then('Result page contains travel option for the chosen destination')
def step_impl(context):
    webdriver.support.ui.WebDriverWait(context.browser, 8200).until(
            webdriver.support.expected_conditions.visibility_of_element_located((
                webdriver.common.by.By.XPATH,"//h3[contains(text(),'Filter properties by')]")))
