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
        self.sign_up_menu = (By.ID, 'createAccountSubmit')
        self.sign_up_name = (By.ID, 'ap_customer_name')
        self.sign_up_email = (By.ID, 'ap_email')
        self.sign_up_password = (By.ID, 'ap_password')
        self.sign_up_password_check = (By.ID, 'ap_password_check')
        self.sign_up_submit = (By.ID, 'continue')

    def test_a_success_signup(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_up_menu).click()
        browser.find_element(*self.sign_up_name).send_keys("Nanda")
        browser.find_element(*self.sign_up_email).send_keys("nantest@mailsac.com")
        browser.find_element(*self.sign_up_password).send_keys("Nanda123")
        browser.find_element(*self.sign_up_password_check).send_keys("Nanda123")
        browser.find_element(*self.sign_up_submit).click()

    def test_b_failed_signup_with_registered_email(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_up_menu).click()
        browser.find_element(*self.sign_up_name).send_keys("Nanda")
        browser.find_element(*self.sign_up_email).send_keys("Nanda@gmail.com")
        browser.find_element(*self.sign_up_password).send_keys("Nanda123")
        browser.find_element(*self.sign_up_password_check).send_keys("Nanda123")
        browser.find_element(*self.sign_up_submit).click()

        error_message = browser.find_element(By.XPATH, "//div[@id='register-mase-inlineerror']//div[@class='a-alert-content']").text
        self.assertIn("There's already an account with this email.", error_message)
    
    def test_c_failed_signup_with_invalid_email_format(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_up_menu).click()
        browser.find_element(*self.sign_up_name).send_keys("Nanda")
        browser.find_element(*self.sign_up_email).send_keys("Nanda")
        browser.find_element(*self.sign_up_password).send_keys("Nanda123")
        browser.find_element(*self.sign_up_password_check).send_keys("Nanda123")
        browser.find_element(*self.sign_up_submit).click()

        error_message = browser.find_element(By.XPATH, "//div[@id='auth-email-invalid-claim-alert']//div[@class='a-alert-content']").text
        self.assertEqual(error_message, "Wrong or Invalid email address or mobile phone number. Please correct and try again.")

    def test_d_failed_signup_with_invalid_password_format(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_up_menu).click()
        browser.find_element(*self.sign_up_name).send_keys("Nanda")
        browser.find_element(*self.sign_up_email).send_keys("Nantest@mailsac.com")
        browser.find_element(*self.sign_up_password).send_keys("Nanda")
        browser.find_element(*self.sign_up_password_check).send_keys("Nanda")
        browser.find_element(*self.sign_up_submit).click()

        error_message = browser.find_element(By.XPATH, "//div[@id='auth-password-invalid-password-alert']//div[@class='a-alert-content']").text
        self.assertEqual(error_message, "Minimum 6 characters required")

    def test_e_failed_signup_with_unmatch_password(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        time.sleep(15)
        browser.find_element(*self.sign_in_menu).click()
        browser.find_element(*self.sign_up_menu).click()
        browser.find_element(*self.sign_up_name).send_keys("Nanda")
        browser.find_element(*self.sign_up_email).send_keys("Nantest@mailsac.com")
        browser.find_element(*self.sign_up_password).send_keys("Nanda123")
        browser.find_element(*self.sign_up_password_check).send_keys("Nanda12")
        browser.find_element(*self.sign_up_submit).click()

        error_message = browser.find_element(By.XPATH, "//div[@id='auth-password-mismatch-alert']//div[@class='a-alert-content']").text
        self.assertEqual(error_message, "Passwords must match")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()