import customtkinter as ctk
from tkinter import messagebox
from captcha.image import ImageCaptcha
import string
import random
from PIL import Image, ImageTk
import os
import pymysql

def login():
    # Set the appearance mode and default color theme
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Initialize variables
    captext = ''
    captcha_image = None

    def generate_captcha():
        nonlocal captext, captcha_image
        img = ImageCaptcha(width=200, height=200)
        m = random.choice(string.ascii_letters)
        r2 = random.random() * 1500
        m2 = str(round(r2))
        captext = str(m) + str(m2)
        data = img.generate(captext)
        img.write(captext, 'capone.png')
        
        # Display the captcha image
        captcha_img = Image.open('capone.png')
        captcha_img = captcha_img.resize((200, 200), Image.Resampling.LANCZOS)
        captcha_image = ImageTk.PhotoImage(captcha_img)
        captcha_label.configure(image=captcha_image)
        captcha_label.image = captcha_image

    def verify_login():
        try:
            # Get entered values
            entered_username = username_entry.get()
            entered_password = password_entry.get()
            entered_captcha = captcha_entry.get()

            # Connect to database
            db = pymysql.connect(
                host='localhost',
                user='root',
                passwd='root',
                database='quizportal'
            )
            cur = db.cursor()

            # Check user credentials
            sql = "SELECT * FROM userinfo WHERE userid=%s AND password=%s"
            cur.execute(sql, (entered_username, entered_password))
            result = cur.fetchone()

            # Verify all conditions
            if result and entered_captcha.strip() == captext.strip():
                messagebox.showinfo("Success", "Welcome to Quiz Portal!")
                root.destroy()  # Close the login window
                os.system('python quizdashboard.py')  # Open the quiz dashboard
            else:
                if not result:
                    messagebox.showerror("Error", "Invalid Username or Password!")
                if entered_captcha.strip() != captext.strip():
                    messagebox.showerror("Error", "Invalid Captcha!")
                generate_captcha()
                captcha_entry.delete(0, 'end')

            db.close()

        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    # Create Toplevel window
    root = ctk.CTkToplevel()
    root.title("Login Page")
    root.geometry("1530x790+0+0")  # Centered position
    root.grab_set()  # Make window modal

    # Create header frame
    header_frame = ctk.CTkFrame(root, fg_color=("#1f538d", "#2b5b9e"))
    header_frame.pack(pady=0, padx=0, fill="x")

    # Add title
    title_label = ctk.CTkLabel(
        header_frame,
        text="Student Login Portal",
        font=("Arial", 32, "bold"),
        text_color="white"
    )
    title_label.pack(pady=20)

    # Create main content frame
    main_frame = ctk.CTkFrame(root, fg_color="transparent")
    main_frame.pack(fill="both", expand=True, pady=20)

    # Create login frame with fixed width and centered
    login_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"), width=500, height=700)
    login_frame.pack(pady=20, padx=20, anchor="center")

    # Center the login frame
    login_frame.pack_propagate(False)  # Prevent frame from shrinking

    # Username
    username_label = ctk.CTkLabel(login_frame, text="User ID:", font=("Arial", 16, "bold"))
    username_label.pack(pady=(40, 5))
    username_entry = ctk.CTkEntry(login_frame, width=400, height=40, font=("Arial", 14))
    username_entry.pack(pady=5)

    # Password
    password_label = ctk.CTkLabel(login_frame, text="Password:", font=("Arial", 16, "bold"))
    password_label.pack(pady=(20, 5))
    password_entry = ctk.CTkEntry(login_frame, width=400, height=40, font=("Arial", 14), show="*")
    password_entry.pack(pady=5)

    # Captcha
    captcha_label = ctk.CTkLabel(login_frame)
    captcha_label.pack(pady=(20, 10))

    captcha_entry_label = ctk.CTkLabel(login_frame, text="Enter Captcha:", font=("Arial", 16, "bold"))
    captcha_entry_label.pack(pady=5)
    captcha_entry = ctk.CTkEntry(login_frame, width=400, height=40, font=("Arial", 14))
    captcha_entry.pack(pady=5)

    # Generate initial captcha
    generate_captcha()

    # Button frame for better alignment
    button_frame = ctk.CTkFrame(login_frame, fg_color="transparent")
    button_frame.pack(pady=30, fill="x")

    # Refresh captcha button
    refresh_button = ctk.CTkButton(
        button_frame,
        text="Refresh Captcha",
        width=200,
        height=40,
        command=generate_captcha,
        font=("Arial", 14)
    )
    refresh_button.pack(side="left", padx=10, expand=True)

    # Login button
    login_button = ctk.CTkButton(
        button_frame,
        text="Login",
        width=200,
        height=40,
        command=verify_login,
        font=("Arial", 14)
    )
    login_button.pack(side="right", padx=10, expand=True)

    root.mainloop() 
    