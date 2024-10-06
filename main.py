from anyio.abc import value
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium
import time

#setup the webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

url = "https://www.linkedin.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

time.sleep(5)
email_input = driver.find_element(By.ID, value="username")
email_input.send_keys('EMAIL ADDRSSS')

password_input = driver.find_element(By.ID,value="password")
password_input.send_keys("Phone Number")

sign_in_button = driver.find_element(By.CSS_SELECTOR,value="form .login__form_action_container  button")
sign_in_button.click()

time.sleep(15)
input_job_search = driver.find_element(By.CSS_SELECTOR,value="#global-nav-typeahead input")
input_job_search.send_keys("Python Developer")
input_job_search.send_keys(Keys.ENTER)

time.sleep(5)
jobs_filter_button = driver.find_element(By.CSS_SELECTOR,value=".search-reusables__filter-list .search-reusables__primary-filter button")
jobs_filter_button.click()

#shortlisting easy apply
time.sleep(5)
easy_apply_filter = driver.find_element(By.CSS_SELECTOR, value="ul .search-reusables__primary-filter .search-reusables__filter-binary-toggle button")
easy_apply_filter.click()


time.sleep(5)
list_of_jobs = driver.find_elements(By.CSS_SELECTOR, value="ul li .job-card-container--clickable")

def abort_application():
    cross_button = driver.find_element(By.CSS_SELECTOR, value=".artdeco-modal__dismiss svg")
    cross_button.click()
    time.sleep(3)
    discard_button = driver.find_element(By.LINK_TEXT, value="Discard")
    discard_button.click()

for i in range(len(list_of_jobs)):

    list_of_jobs[i].click()

    try:
            # click easy apply filter
            time.sleep(10)
            apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
            apply_button.click()

            # entering phone number
            # time.sleep(5)
            # input_phone = driver.find_element(By.ID, value='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4041825708-7628135682-phoneNumber-nationalNumber')
            # input_phone.send_keys("1234567839")

            # jobs
            time.sleep(2)
            next_button = driver.find_element(By.CSS_SELECTOR, value='footer div button')
            next_button.click()

            # next button
            time.sleep(2)
            next_button2 = driver.find_element(By.CSS_SELECTOR, value='.justify-flex-end .artdeco-button--primary')
            next_button2.click()

            # years of experience
            time.sleep(4)
            work_experience = driver.find_elements(By.CSS_SELECTOR, value='.artdeco-text-input--container input')
            for element in work_experience:
                element.send_keys("3")

            # review button
            time.sleep(6)
            review_button = driver.find_element(By.CSS_SELECTOR, value='.justify-flex-end .artdeco-button--primary')
            review_button.click()

            # submit button
            time.sleep(5)
            submit_button = driver.find_element(By.CSS_SELECTOR, value='.justify-flex-end .artdeco-button--primary')
            submit_button.click()

    except selenium.common.exceptions.ElementClickInterceptedException:
            abort_application()

    except NoSuchElementException:
        continue

