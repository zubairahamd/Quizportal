import customtkinter as ctk
from login_page import*
from adminmanagment import*


app = ctk.CTk()
app.title("Quiz Portal")
app.geometry("1530x790+0+0")
app.config(bg="#2A3335")






# Function definitions
def login():
    app.withdraw()  # Hide the main window
    login_window = create_login_window()
    login_window.protocol("WM_DELETE_WINDOW", lambda: on_login_close(login_window))
    login_window.mainloop()

def on_login_close(login_window):
    login_window.destroy()
    app.deiconify()  # Show the main window again

def sign_up():
    print("Sign up button clicked")
    
def forgot_password():
    print("Forgot password clicked")

# Create the main app


# Create main frame
main_frame = ctk.CTkFrame(app, corner_radius=15, fg_color="#2A3335")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create side frames
left_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color="#3a7ebf")
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

right_frame = ctk.CTkFrame(main_frame, corner_radius=15,fg_color="#222222")
right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

# Left side content
left_center_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
left_center_frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = ctk.CTkLabel(left_center_frame, 
    text="QUIZ PORTAL",
    font=ctk.CTkFont(family="times new roman", size=90, weight="bold"),
    text_color="#fff"
)
title_label.pack(pady=(0, 30))

features_text = "Interactive Questions\nProgress Tracking\nInstant Results\nMultiple Categories"

features_label = ctk.CTkLabel(
    left_center_frame,
    text=features_text,
    font=ctk.CTkFont(family="times new roman", size=16),
    text_color="#ffffff",
    justify="left"
)
features_label.pack(pady=20)

# Right side content
login_container = ctk.CTkFrame(right_frame, fg_color="transparent")
login_container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8)

welcome_label = ctk.CTkLabel(
    login_container,
    text="Welcome Back",
    font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
    text_color="#ffffff"
)
welcome_label.pack(pady=(0, 5))

description_label = ctk.CTkLabel(
    login_container,
    text="Sign in to continue or create a new account",
    font=ctk.CTkFont(size=14),
    text_color="gray"
)
description_label.pack(pady=(0, 40))

login_button = ctk.CTkButton(
    login_container,
    text="Login",
    font=ctk.CTkFont(size=15, weight="bold"),
    corner_radius=10,
    border_width=0,
    height=50,
    command=login
)
login_button.pack(pady=10, fill="x")

signin_button = ctk.CTkButton(
    login_container,
    text="Sign Up",
    font=ctk.CTkFont(size=15, weight="bold"),
    corner_radius=10,
    border_width=0,
    height=50,
    command=sign_up
)
signin_button.pack(pady=10, fill="x")


adminlogin_button = ctk.CTkButton(
    right_frame,
    text="ADMIN LOGIN",
    font=ctk.CTkFont(size=15, weight="bold"),
    corner_radius=10,
    border_width=0,
    height=50,
    command=adminenter
  
)
adminlogin_button.place(x=550,y=10)

options_frame = ctk.CTkFrame(login_container, fg_color="transparent")
options_frame.pack(pady=(30, 0), fill="x")

forgot_button = ctk.CTkButton(
    options_frame,
    text="Forgot Password?",
    font=ctk.CTkFont(size=12),
    fg_color="transparent",
    hover_color=right_frame._fg_color,
    text_color="gray",
    width=20,
    height=20,
    command=forgot_password
)
forgot_button.pack()



app.mainloop() 