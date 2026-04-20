import os 
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Load credentials from .env
load_dotenv()

user = os.getenv('user')
password = os.getenv('password')

# Define options
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Set default download directory to current working directory
download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

# Initialize the driver - Selenium automatically manages the ChromeDriver now!
driver = webdriver.Chrome(options=chrome_options)

try:
    # Load the webpage
    driver.get('https://demoqa.com/login')

    # Locate username, password and login button
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
    login_button = driver.find_element(By.ID, 'login')

    # Fill in username and password
    username_field.send_keys(user)
    password_field.send_keys(password) 
    driver.execute_script("arguments[0].click();", login_button)

    # Locate the Elements dropdown and Text Box
    elements = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Elements']")))
    driver.execute_script("arguments[0].click();", elements)

    text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Text Box']")))
    driver.execute_script("arguments[0].click();", text_box)

    # Locate the form fields and sumbit button 
    fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
    current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
    permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
    submit_button = driver.find_element(By.ID, 'submit')

    # Fill in the form fields
    fullname_field.send_keys('John Smith')
    email_field.send_keys('john@gmail.com')
    current_address_field.send_keys('Rondo Daszynskiego 1, Warsaw, Poland')
    permanent_address_field.send_keys('John Street 1, Warsaw, Poland')

    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    # Locate the Upload and Download section and the Download button
    upload_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
    upload_download.click()
    download_button = driver.find_element(By.ID, 'downloadButton')
    driver.execute_script("arguments[0].click();", download_button)

    print("The script executed successfully!")

finally:
    input("Press Enter to close the browser...")
    driver.quit()