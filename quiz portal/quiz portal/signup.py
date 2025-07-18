import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import pymysql

def usersave():
    db = pymysql.connect(host='localhost',user='root',passwd='root',database='quizportal')
    cur = db.cursor()
    xa = name_entry.get()
    xb = address_entry.get()
    xc = email_entry.get()
    xd = city_entry.get()
    xe = phone_entry.get()
    xf = user_id_entry.get()
    xg = password_entry.get()
    sql = "insert into userinfo values('%s','%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg)
    data = cur.execute(sql)
    db.commit()
    CTkMessagebox(title="message", message="DATA SAVED SUCCESSFULLY", 
                        icon="warning", option_1="Yes")
   
    db.close()
    name_entry(0,100)
    address_entry(0,100)
    phone_entry(0,100)
    email_entry(0,100)
    user_id_entry(0,100)
    password_entry(0,100)
    city_entry(0,100)






# Create the main window

root = ctk.CTk()
root.title("Quiz Portal - User Registration")
root.geometry("1530x790+0+0")

# Custom colors
primary_color = "#2A3335"
secondary_color = "#222222"
accent_color = "#4CAF50"

# Create main frame
main_frame = ctk.CTkFrame(root, corner_radius=15, fg_color=secondary_color)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Configure grid layout for main_frame
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=0)  # Title row
main_frame.rowconfigure(1, weight=1)  # Content row

# Title
title_label = ctk.CTkLabel(
    main_frame,
    text="USER REGISTRATION",
    font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
    text_color="#3a7ebf"
)
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 30), sticky="n")

# Left column for form
left_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
left_frame.grid(row=1, column=0, padx=(50, 20), pady=20, sticky="nsew")

# Right column for form
right_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
right_frame.grid(row=1, column=1, padx=(20, 50), pady=20, sticky="nsew")

# Configure grid for left and right frames
for frame in [left_frame, right_frame]:
    frame.columnconfigure(0, weight=1)
    for i in range(8):  # Rows for each frame
        frame.rowconfigure(i, weight=1)

# Name (left side)
name_label = ctk.CTkLabel(
    left_frame,
    text="Name",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
name_label.grid(row=0, column=0, sticky="w", pady=(10, 0))

name_entry = ctk.CTkEntry(
    left_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0
)
name_entry.grid(row=1, column=0, sticky="ew", pady=(5, 20))

# Email (left side)
email_label = ctk.CTkLabel(
    left_frame,
    text="Email",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
email_label.grid(row=2, column=0, sticky="w", pady=(10, 0))

email_entry = ctk.CTkEntry(
    left_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0
)
email_entry.grid(row=3, column=0, sticky="ew", pady=(5, 20))

# Phone (left side)
phone_label = ctk.CTkLabel(
    left_frame,
    text="Phone No.",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
phone_label.grid(row=4, column=0, sticky="w", pady=(10, 0))

phone_entry = ctk.CTkEntry(
    left_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0
)
phone_entry.grid(row=5, column=0, sticky="ew", pady=(5, 20))

# Address (right side)
address_label = ctk.CTkLabel(
    right_frame,
    text="Address",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
address_label.grid(row=0, column=0, sticky="w", pady=(10, 0))


address_entry = ctk.CTkEntry(
    right_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0
)
address_entry.grid(row=1, column=0, sticky="ew", pady=(5, 20))

# City (right side)
city_label = ctk.CTkLabel(
    right_frame,
    text="City",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
city_label.grid(row=2, column=0, sticky="w", pady=(10, 0))

city_entry = ctk.CTkEntry(
    right_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0
)
city_entry.grid(row=3, column=0, sticky="ew", pady=(5, 20))

# User ID (right side)
user_id_label = ctk.CTkLabel(
    right_frame,
    text="Create User ID",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
user_id_label.grid(row=4, column=0, sticky="w", pady=(10, 0))

user_id_entry = ctk.CTkEntry(
    right_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0
)
user_id_entry.grid(row=5, column=0, sticky="ew", pady=(5, 20))

course_label = ctk.CTkLabel(
    right_frame,
    text="Confirm Password",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
course_label.grid(row=6, column=0, sticky="w", pady=(10, 0))

course_entry = ctk.CTkEntry(
    right_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0
)
course_entry.grid(row=7, column=0, sticky="ew", pady=(5, 20))

# Password (left side)
password_label = ctk.CTkLabel(
    left_frame,
    text="Create Password",
    font=ctk.CTkFont(size=16),
    text_color="#ffffff"
)
password_label.grid(row=6, column=0, sticky="w", pady=(10, 0))

password_entry = ctk.CTkEntry(
    left_frame,
    width=500,
    height=40,
    font=ctk.CTkFont(size=16),
    corner_radius=8,
    border_width=0,
    show="•"
)
password_entry.grid(row=7, column=0, sticky="ew", pady=(5, 20))

# Button frame at the bottom center
button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 30))

# Register button
register_button = ctk.CTkButton(
    button_frame,
    text="Register",
    font=ctk.CTkFont(size=18, weight="bold"),
    corner_radius=8,
    border_width=0,
    height=50,
    width=200,
    fg_color=accent_color,
    hover_color="#3d8b40",
    command = usersave
)
register_button.grid(row=0, column=0, padx=20)

# Back button
def go_back():
    root.destroy()  
back_button = ctk.CTkButton(
    button_frame,
    text="Back",
    font=ctk.CTkFont(size=18, weight="bold"),
    corner_radius=8,
    border_width=0,
    height=50,
    width=200,
    fg_color="#F44336",
    hover_color="#d32f2f"
)
back_button.configure(command=go_back)
back_button.grid(row=0, column=1, padx=20)

# Start the main loop
root.mainloop()