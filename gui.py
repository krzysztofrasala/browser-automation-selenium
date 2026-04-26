import tkinter as tk
from tkinter import messagebox
from main import WebAutomation

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")
        self.root.geometry("400x350")

        # Login Frame
        self.login_frame = tk.LabelFrame(self.root, text="Login Credentials", padx=10, pady=10)
        self.login_frame.pack(padx=10, pady=5, fill="x")

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, sticky="w")
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky="ew")

        # Form submission frame
        self.form_frame = tk.LabelFrame(self.root, text="Form Data", padx=10, pady=10)
        self.form_frame.pack(padx=10, pady=5, fill="x")

        tk.Label(self.form_frame, text="Full Name").grid(row=0, column=0, sticky="w")
        self.entry_fullname = tk.Entry(self.form_frame)
        self.entry_fullname.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email").grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Current Address").grid(row=2, column=0, sticky="w")
        self.entry_current_address = tk.Entry(self.form_frame)
        self.entry_current_address.grid(row=2, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Permanent Address").grid(row=3, column=0, sticky="w")
        self.entry_permanent_address = tk.Entry(self.form_frame)
        self.entry_permanent_address.grid(row=3, column=1, sticky="ew")

        # Buttons
        self.btn_submit = tk.Button(self.root, text="Submit", command=self.submit_data)
        self.btn_submit.pack(side="left", padx=20, pady=10)

        self.btn_close = tk.Button(self.root, text="Close Browser", command=self.root.quit)
        self.btn_close.pack(side="right", padx=20, pady=10)

    def submit_data(self):
        """Fetch data from GUI and trigger WebAutomation."""
        # Get data from entries
        username = self.entry_username.get()
        password = self.entry_password.get()
        fullname = self.entry_fullname.get()
        email = self.entry_email.get()
        curr_addr = self.entry_current_address.get()
        perm_addr = self.entry_permanent_address.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please provide at least login and password!")
            return

        try:
            # Initialize automation logic
            bot = WebAutomation()
            
            # Override .env credentials with GUI input if provided
            if username: bot.user = username
            if password: bot.password = password

            # Execute steps
            bot.login()
            bot.fill_text_box_form(fullname, email, curr_addr, perm_addr)
            bot.download_file()
            
            messagebox.showinfo("Success", "Automation finished successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()