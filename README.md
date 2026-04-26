# Web Automation Bot 🚀

Professional Selenium automation with a Tkinter GUI for DemoQA. Refactored into clean OOP structure.

## 🛠 Features
- **OOP Design**: Logic encapsulated in `WebAutomation` class.
- **Tkinter GUI**: Simple interface for data entry.
- **Reliable Locators**: Uses JS clicks and Explicit Waits to bypass ads.
- **Process**: Auto-login -> Form Fill -> File Download.

## ⚙️ Setup
1. **Install Dependencies**:
   ```bash
   pip install selenium python-dotenv
   ```
2. **Environment Variables**: Create a `.env` file:
   ```env
   user=your_username
   password=your_password
   ```

## 🚀 How to Run
```bash
python gui.py
```

## 📂 Project Structure
- `main.py` - Core automation logic (Class-based).
- `gui.py` - Tkinter interface.
- `.env` - Private credentials (ignored by git).

---
*Created for browser automation testing.*
