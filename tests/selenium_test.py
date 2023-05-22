import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pathlib import Path
import unittest, os, time, datetime, tracemalloc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from app import create_app, db
from app.models import *
from app.main.main_controller import init_db,init_settings
from config import TestingConfig

from selenium.webdriver.chrome.service import Service


basedir = os.path.dirname(os.path.abspath(__file__))

chrome_driver_path = os.path.join(basedir, "chromedriver")
ser = Service(chrome_driver_path)

chrome_options = ChromeOptions()
chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
class SystemTest(unittest.TestCase):
    driver = None
    service = None

    def setUp(self):
        self.driver = webdriver.Chrome(service=ser, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:5000/index")

    def tearDown(self) -> None:
        if self.driver:
            self.driver.close()

    def test_signup(self):
        self.driver.get("http://localhost:5000/signup")

        username = self.driver.find_element(By.ID, "username")
        username.send_keys("testuser")
        pass1 = self.driver.find_element(By.ID, "password")
        pass1.send_keys("testpass")
        pass2 = self.driver.find_element(By.ID, "password2")
        pass2.send_keys("testpass")
        submit = self.driver.find_element(By.ID, "submit")
        submit.click()
        u = User.query.filter_by(username="testuser").first()
        self.assertEqual(u.username, "testuser")

if __name__ == "__main__":
    unittest.main(verbosity=2)