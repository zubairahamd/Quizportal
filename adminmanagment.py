import customtkinter as ctk
from adminquizupdate import*
from userresult import*

def adminenter():
    
    
    app = ctk.CTk()
    app.title("Quiz Portal")
    app.geometry("1530x790+0+0")
    app.config(bg="#2A3335")
    
    
    
    
    
    
    
    
    # Create the main app
    
    
    # Create main frame
    main_frame = ctk.CTkFrame(app, corner_radius=15, fg_color="#2A3335")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Create side frames
    left_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color="#B70101")
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
    
    right_frame = ctk.CTkFrame(main_frame, corner_radius=15,fg_color="#222222")
    right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
    
    # Left side content
    left_center_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
    left_center_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    title_label = ctk.CTkLabel(left_center_frame, 
        text="ADMIN MANAGMENT \n DASHBORD",
        font=ctk.CTkFont(family="times new roman", size=50, weight="bold"),
        text_color="#fff"
    )
    title_label.pack(pady=(0, 30))
    
    features_text = "ADMIN CAN MANAGE\n FULL FUNCTIONALITY\n OVER ALL PORTAL"
    
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
        text="Welcome Back Admin",
        font=ctk.CTkFont(family="Brush Script MT", size=32, weight="bold"),
        text_color="#ffffff"
    )
    welcome_label.pack(pady=(0, 5))
    
    description_label = ctk.CTkLabel(
        login_container,
        text="What do you want to change?",
        font=ctk.CTkFont(family="Brush Script MT", size=20),
        text_color="gray"
    )
    description_label.pack(pady=(0, 40))
    
    login_button = ctk.CTkButton(
        login_container,
        text="QUIZ MANAGMENT DASHBORD",
        font=ctk.CTkFont(size=15, weight="bold"),
        corner_radius=10,
        fg_color="#B70101",
        border_width=0,
        height=50,
        command=adminquizupdate
    )
    login_button.pack(pady=10, fill="x")
    
    signin_button = ctk.CTkButton(
        login_container,
        text="VIEW SCORES",
        font=ctk.CTkFont(size=15, weight="bold"),
        corner_radius=10,
        border_width=0,
        height=50,
        command=userresult,
        fg_color="#B70101"
    )
    signin_button.pack(pady=10, fill="x")
    
    
    
    
    
    
    app.mainloop() 