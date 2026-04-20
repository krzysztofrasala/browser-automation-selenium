# Browser Automation with Selenium - DemoQA

A training project focused on web browser automation using Python and Selenium. The script automates the process of logging in, filling out forms, and downloading files on the DemoQA platform.

## 🚀 Features

* **Automated Login:** Secure login process using environment variables.
* **Form Handling:** Automatic completion of text fields (Full Name, Email, Addresses).
* **UI Interactions:** Page scrolling and handling dynamic elements using WebDriverWait.
* **File Download:** Navigating to the Upload/Download section and triggering a file download to the local directory.

## 🛠️ Technologies

* **Python 3.x**
* **Selenium WebDriver** - Automation engine.
* **python-dotenv** - Secure credential management.
* **ChromeDriver** - Driver for Chrome browser.

## 📋 Installation

1. **Clone the repository:**

       git clone [https://github.com/krzysztofrasala/browser-automation-selenium.git](https://github.com/krzysztofrasala/browser-automation-selenium.git)
       cd browser-automation-selenium

2. **Create and activate a virtual environment:**

       python3 -m venv .venv
       source .venv/bin/activate

3. **Install dependencies:**

       pip install -r requirements.txt

## 🔐 Security Configuration

This project uses a .env file to store login credentials. This file is excluded from version control (defined in .gitignore) to prevent passwords from being exposed online.

1. Create a .env file in the root directory.
2. Add your credentials as follows:

       user=your_username
       password=your_secret_password

## 🏁 How to Run

1. Ensure you have Google Chrome installed.
2. Ensure the chromedriver path in main.py matches your local setup.
3. Run the script:

       python main.py
