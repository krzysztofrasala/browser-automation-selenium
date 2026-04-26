import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAutomation:
    def __init__(self):
        load_dotenv()
        self.user = os.getenv('user')
        self.password = os.getenv('password')
        
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-search-engine-choice-screen")
        # Added to ignore minor SSL/certificate issues
        self.chrome_options.add_argument("--ignore-certificate-errors")
        
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        self.chrome_options.add_experimental_option('prefs', prefs)
        
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # Increased wait time to 15 seconds for slower connections/ads
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        print("Logging in...")
        self.driver.get('https://demoqa.com/login')
        
        user_field = self.wait.until(EC.element_to_be_clickable((By.ID, 'userName')))
        pass_field = self.driver.find_element(By.ID, 'password')
        login_btn = self.driver.find_element(By.ID, 'login')

        user_field.send_keys(self.user)
        pass_field.send_keys(self.password)
        self.driver.execute_script("arguments[0].click();", login_btn)

    def fill_text_box_form(self, name, email, current_addr, perm_addr):
        print("Filling out the Text Box form...")
        
        # Click Elements using JS to bypass overlays
        elements_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Elements']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", elements_menu)
        self.driver.execute_script("arguments[0].click();", elements_menu)
        
        # Click Text Box
        text_box_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']")))
        self.driver.execute_script("arguments[0].click();", text_box_btn)

        # Fill fields
        self.wait.until(EC.visibility_of_element_located((By.ID, 'userName'))).send_keys(name)
        self.driver.find_element(By.ID, 'userEmail').send_keys(email)
        self.driver.find_element(By.ID, 'currentAddress').send_keys(current_addr)
        self.driver.find_element(By.ID, 'permanentAddress').send_keys(perm_addr)

        submit_btn = self.driver.find_element(By.ID, 'submit')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def download_file(self):
        print("Downloading file...")
        # Finding the 'Upload and Download' item in the sidebar
        # Using a more specific selector to avoid mistakes
        upload_item = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Upload and Download']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", upload_item)
        self.driver.execute_script("arguments[0].click();", upload_item)
        
        # Wait for download button and click it
        download_btn = self.wait.until(EC.element_to_be_clickable((By.ID, 'downloadButton')))
        self.driver.execute_script("arguments[0].click();", download_btn)
        
        # Small sleep to let the browser start the download before closing
        time.sleep(2) 

    def run(self, name='John Doe', email='john@example.com', c_addr='Addr 1', p_addr='Addr 2'):
        try:
            self.login()
            self.fill_text_box_form(name, email, c_addr, p_addr)
            self.download_file()
            print("Finished!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Removed the input() to prevent terminal hanging
            self.driver.quit()