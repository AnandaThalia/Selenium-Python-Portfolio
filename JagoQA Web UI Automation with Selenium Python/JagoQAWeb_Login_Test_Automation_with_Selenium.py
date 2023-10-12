import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(options=options)
        
    def test_a_success_login(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "email").send_keys("jagoqaindonesia@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "Welcome Jago QA")
        self.assertEqual(respon_berhasil, "Anda Berhasil Login")

    def test_b_failed_login_email_not_registered(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "email").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "User's not found")
        self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")

    def test_c_failed_login_empty_email_and_password(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "Cek Formulir Anda")
        self.assertEqual(respon_berhasil, "Email & Password tidak boleh kosong")


    def test_d_failed_login_empty_email(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "Cek Formulir Anda")
        self.assertEqual(respon_berhasil, "Email tidak boleh kosong")

    def test_e_failed_login_empty_password(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "email").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "Cek Formulir Anda")
        self.assertEqual(respon_berhasil, "Password tidak boleh kosong")

    def test_f_failed_login_email_too_long(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "email").send_keys("wxsmgswoylgxmgeqzkongnlpghkxlulahcvdamudbypfwlbkizmfwvezbmebxtexnqhxanpcibddolrxgswtnhaavwseabkxjvmdmlaenjria@jagoqa.com")
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "User's not found")
        self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")

    def test_g_failed_login_password_too_long(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "email").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "wxsmgswoylgxmgeqzkongnlpghkxlulahcvdamudbypfwlbkizmfwvezbmebxtexnqhxanpcibddolrxgswtnhaavwseabkxjvmdmlaenjria")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "User's not found")
        self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")

    def test_h_failed_login_invalid_email_format(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "email").send_keys("nanda@@jagoqa.com")
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("wxsmgswoylgxmgeqzk")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        email_error = browser.find_element(By.ID, "email").get_attribute("validationMessage")
        print(email_error)
        self.assertIn("A part following '@' should not contain the symbol '@'.", email_error)

    def test_i_failed_login_password_contain_symbol(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        browser.find_element(
            By.ID, "email").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("wxsmgsw&@jria")
        time.sleep(1)
        browser.find_element(
            By.ID, "signin_login").click()
        time.sleep(2)
        respon_welcome = browser.find_element(
            By.ID, "swal2-title").text
        respon_berhasil = browser.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(respon_welcome, "User's not found")
        self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
