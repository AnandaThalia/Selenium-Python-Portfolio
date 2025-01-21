from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from guara.transaction import AbstractTransaction, Application
from guara import setup, it


class OpenAmazonHomePage(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, url):
        self._driver.get(url)
        self._driver.implicitly_wait(15)


class SignIn(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, email, password):
        sign_in_menu = (By.ID, "nav-link-accountList")
        sign_in_email = (By.ID, "ap_email")
        sign_in_submit_email = (By.ID, "continue")
        sign_in_password = (By.ID, "ap_password")
        sign_in_submit_password = (By.ID, "signInSubmit")

        # Perform sign-in steps
        self._driver.find_element(*sign_in_menu).click()
        self._driver.find_element(*sign_in_email).send_keys(email)
        self._driver.find_element(*sign_in_submit_email).click()
        self._driver.find_element(*sign_in_password).send_keys(password)
        self._driver.find_element(*sign_in_submit_password).click()

        # Return the welcome message text for assertion
        welcome_message_locator = (By.ID, "nav-link-accountList-nav-line-1")
        return self._driver.find_element(*welcome_message_locator).text


def test_successful_signin():
    # Configure WebDriver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    # Instantiate the application
    app = Application(driver)

    try:
        # Open Amazon home page
        app.at(OpenAmazonHomePage, url="https://www.amazon.com/")

        # Perform sign-in and assert the welcome message
        app.at(SignIn, email="nantest17@gmail.com", password="Nanda123").asserts(
            it.IsEqualTo, "Hello, Nanda"
        )
    finally:
        # Close the browser
        app.at(setup.CloseApp)
