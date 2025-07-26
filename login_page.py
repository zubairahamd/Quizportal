import customtkinter as ctk
from PIL import Image, ImageTk
import os
from captcha.image import ImageCaptcha
import string
import random
from tkinter import messagebox

def create_login_window():
    # Create login window
    login_window = ctk.CTk()
    login_window.title("Login")
    login_window.geometry("1530x790+0+0")
    login_window.configure(fg_color="#2A3335")
    
    # Create main frame
    main_frame = ctk.CTkFrame(login_window, fg_color="transparent")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Create center frame for login form
    center_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    center_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    # Title
    title_label = ctk.CTkLabel(
        center_frame,
        text="Login",
        font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
        text_color="#ffffff"
    )
    title_label.pack(pady=(20, 30))
    
    # Username
    username_label = ctk.CTkLabel(
        center_frame,
        text="Username",
        font=ctk.CTkFont(size=14),
        text_color="#ffffff"
    )
    username_label.pack(anchor="w", padx=20)
    
    username_entry = ctk.CTkEntry(
        center_frame,
        placeholder_text="Enter your username",
        width=300,
        height=40,
        font=ctk.CTkFont(size=14)
    )
    username_entry.pack(pady=(0, 20))
    
    # Password
    password_label = ctk.CTkLabel(
        center_frame,
        text="Password",
        font=ctk.CTkFont(size=14),
        text_color="#ffffff"
    )
    password_label.pack(anchor="w", padx=20)
    
    password_entry = ctk.CTkEntry(
        center_frame,
        placeholder_text="Enter your password",
        width=300,
        height=40,
        font=ctk.CTkFont(size=14),
        show="*"
    )
    password_entry.pack(pady=(0, 20))
    
    # Captcha section
    captcha_frame = ctk.CTkFrame(center_frame, fg_color="transparent")
    captcha_frame.pack(pady=10)
    
    captcha_label = ctk.CTkLabel(
        captcha_frame,
        text="Enter Captcha",
        font=ctk.CTkFont(size=14),
        text_color="#ffffff"
    )
    captcha_label.pack(anchor="w", padx=20)
    
    captcha_image_label = ctk.CTkLabel(captcha_frame, text="")
    captcha_image_label.pack(pady=5)
    
    captcha_entry = ctk.CTkEntry(
        captcha_frame,
        placeholder_text="Enter captcha code",
        width=300,
        height=40,
        font=ctk.CTkFont(size=14)
    )
    captcha_entry.pack(pady=5)
    
    # Captcha variables
    captext = ''
    
    def generate_captcha():
        nonlocal captext
        img = ImageCaptcha(width=200, height=200)
        m = random.choice(string.ascii_letters)
        r2 = random.random() * 1500
        m2 = str(round(r2))
        captext = str(m) + str(m2)
        data = img.generate(captext)
        img.write(captext, 'capone.png')
        show_captcha()
    
    def show_captcha():
        try:
            captcha_image = Image.open('capone.png')
            captcha_photo = ImageTk.PhotoImage(captcha_image)
            captcha_image_label.configure(image=captcha_photo)
            captcha_image_label.image = captcha_photo
        except Exception as e:
            print(f"Error showing captcha: {e}")
    
    # Generate initial captcha
    generate_captcha()
    
    refresh_button = ctk.CTkButton(
        captcha_frame,
        text="Refresh Captcha",
        width=150,
        height=30,
        font=ctk.CTkFont(size=12),
        command=generate_captcha
    )
    refresh_button.pack(pady=5)
    
    def login():
        username = username_entry.get()
        password = password_entry.get()
        entered_captcha = captcha_entry.get()
        
        if not username or not password or not entered_captcha:
            messagebox.showerror("Error", "Please fill in all fields")
            return
            
        if entered_captcha != captext:
            messagebox.showerror("Error", "Invalid captcha code")
            generate_captcha()
            captcha_entry.delete(0, 'end')
            return
            
        # Add your login logic here
        print(f"Login attempt - Username: {username}, Password: {password}")
        messagebox.showinfo("Success", "Login successful!")
    
    def go_back():
        login_window.destroy()  # Close the login window
    
    # Login button
    login_button = ctk.CTkButton(
        center_frame,
        text="Login",
        width=300,
        height=40,
        font=ctk.CTkFont(size=14, weight="bold"),
        command=login
    )
    login_button.pack(pady=20)
    
    # Back button
    back_button = ctk.CTkButton(
        center_frame,
        text="Back to Main",
        width=300,
        height=40,
        font=ctk.CTkFont(size=14),
        fg_color="transparent",
        border_width=1,
        command=go_back
    )
    back_button.pack(pady=10)
    
    return login_window 