import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegPage(unittest.TestCase):
    def test_page1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        first = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]").send_keys("AAA")
        last = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]").send_keys("AAA")
        email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys("AAA")
        sub = browser.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    def test_page2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        first = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]").send_keys("AAA")
        last = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]").send_keys("AAA")
        email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys("AAA")
        sub = browser.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
if __name__ == "__main__":
    unittest.main()