import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestSignUp(unittest.TestCase):
    def setUp(self):
        options = Options()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu') 
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-infobars')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--start-maximized')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        ## Locator
        self.sign_in_menu = (By.ID, 'nav-link-accountList')
        self.sign_in_email = (By.ID, 'ap_email')
        self.sign_in_password = (By.ID, 'ap_password')
        self.sign_in_submit_email = (By.ID, 'continue')
        self.sign_in_submit_password = (By.ID, 'signInSubmit')
        self.sign_in_skip = (By.ID, 'ap-account-fixup-phone-skip-link')

    def test_a_success_signin(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_in_email).send_keys("nantest17@gmail.com")
        browser.find_element(*self.sign_in_submit_email).click()
        browser.find_element(*self.sign_in_password).send_keys("Nanda123")
        browser.find_element(*self.sign_in_submit_password).click()
        welcome_message = browser.find_element(By.ID, "nav-link-accountList-nav-line-1").text
        self.assertEqual(welcome_message, "Hello, Nanda")

    def test_b_failed_signin_with_unregistered_email(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_in_email).send_keys("nantest@gmail.com")
        browser.find_element(*self.sign_in_submit_email).click()
        error_message = browser.find_element(By.XPATH, "//div[@id='auth-error-message-box']//span[@class='a-list-item']").text
        self.assertEqual(error_message, "We cannot find an account with that email address")

    def test_c_failed_signin_with_empty_email(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_in_submit_email).click()
        error_message = browser.find_element(By.XPATH, "//div[@id='auth-email-missing-alert']//div[@class='a-alert-content']").text
        self.assertEqual(error_message, "Enter your email or mobile phone number")

    def test_d_failed_signin_with_invalid_email_format(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_in_email).send_keys("nanda")
        browser.find_element(*self.sign_in_submit_email).click()
        error_message = browser.find_element(By.XPATH, "//div[@id='auth-email-invalid-claim-alert']//div[@class='a-alert-content']").text
        self.assertEqual(error_message, "Wrong or Invalid email address or mobile phone number. Please correct and try again.")

    def test_e_failed_signin_with_invalid_phone_number(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(2)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_in_email).send_keys("081122334455")
        browser.find_element(*self.sign_in_submit_email).click()
        error_message = browser.find_element(By.XPATH, "//div[@id='auth-error-message-box']//span[@class='a-list-item']").text
        self.assertEqual(error_message, "We cannot find an account with that mobile number")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()