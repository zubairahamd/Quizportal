import customtkinter as ctk
#from CTkMessagebox import CTkMessagebox
from pythonquestion import*
from javaquestion import*
from htmlcssquestion import*
from sqlquestion import*
import pymysql
import os
import signup
import admin_login
import tkinter
from tkinter import *
from tkinter import messagebox


def save():
    db = pymysql.connect(host='localhost',user='root',passwd='root',database='quizportal')
    cur = db.cursor()
    xa = name_entry.get()
    xb = roll_entry.get()
    
    sql = "insert into test values('%s','%s)"%(xa,xb)

    data = cur.execute(sql)
    db.commit()
    
    CTkMessagebox(title="message", message="DATA SAVED SUCCESSFULLY")

def open_login():
    app.withdraw()  # Hide the main window
    os.system('python login.py')  # Open the login window
    app.destroy()  # Close the dashboard



# Set the appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main window
app = ctk.CTk()
app.title("quizportal")
app.geometry("1530x790+0+0")

# Configure grid
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)  # Make main content expandable

# Create header frame
header_frame = ctk.CTkFrame(app, fg_color=("#1f538d", "#2b5b9e"))
header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

# Add title
title_label = ctk.CTkLabel(
    header_frame,
    text="Lets Play Quiz",
    font=("Brush Script MT", 55, "bold"),
    text_color="white"
)
title_label.grid(row=0, column=0, pady=20,padx = 650)

# Create main content frame
main_frame = ctk.CTkFrame(app, fg_color="transparent")
main_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)

# Configure grid for main frame
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

# Create frames for each quiz
python_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"), corner_radius=10)
python_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

java_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"), corner_radius=10)
java_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

html_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"), corner_radius=10)
html_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

sql_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"), corner_radius=10)
sql_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

# Configure grid for each quiz frame
for frame in [python_frame, java_frame, html_frame, sql_frame]:
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)

# Python Quiz
python_title = ctk.CTkLabel(
    python_frame,
    text="Python Quiz",
    font=("Brush Script MT", 30, "bold"),
    text_color="white"
)
python_title.grid(row=0, column=0, pady=(20, 10))

python_btn = ctk.CTkButton(
    python_frame,
    text="Start Quiz",
    width=200,
    height=50,
    command=pythonquestion,
    font=("Brush Script MT", 20),
    fg_color="#4CAF50",
    hover_color="#45a049"
)
python_btn.grid(row=1, column=0, pady=(0, 20))

# Java Quiz
java_title = ctk.CTkLabel(
    java_frame,
    text="Java Quiz",
    font=("Brush Script MT", 30, "bold"),
    text_color="white"
)
java_title.grid(row=0, column=0, pady=(20, 10))

java_btn = ctk.CTkButton(
    java_frame,
    text="Start Quiz",
    width=200,
    height=50,
    command=javaquestion,
    font=("Brush Script MT", 20),
    fg_color="#4CAF50",
    hover_color="#45a049"
)
java_btn.grid(row=1, column=0, pady=(0, 20))

# HTML & CSS Quiz
html_title = ctk.CTkLabel(
    html_frame,
    text="HTML & CSS Quiz",
    font=("Brush Script MT", 30, "bold"),
    text_color="white"
)
html_title.grid(row=0, column=0, pady=(20, 10))

html_btn = ctk.CTkButton(
    html_frame,
    text="Start Quiz",
    width=200,
    height=50,
    command=htmlcssquestion,
    font=("Brush Script MT", 20),
    fg_color="#4CAF50",
    hover_color="#45a049"
)
html_btn.grid(row=1, column=0, pady=(0, 20))

# SQL Quiz
sql_title = ctk.CTkLabel(
    sql_frame,
    text="SQL Quiz",
    font=("Brush Script MT", 30, "bold"),
    text_color="white"
)
sql_title.grid(row=0, column=0, pady=(20, 10))

sql_btn = ctk.CTkButton(
    sql_frame,
    text="Start Quiz",
    width=200,
    height=50,
    command=sqlquestion,
    font=("Brush Script MT", 20),
    fg_color="#4CAF50",
    hover_color="#45a049"
)
sql_btn.grid(row=1, column=0, pady=(0, 20))

app.mainloop() 

def quizdashboard():
    t = tkinter.Tk()
    t.title('QUIZ DASHBOARD')
    t.geometry('800x600')
    t.config(bg='white')

    def create_widgets():
        global title_label, python_button, java_button, exit_button
        
        # Title
        title_label = Label(t, text='QUIZ DASHBOARD', font=('arial', 24, 'bold'))
        title_label.pack(pady=20)
        
        # Buttons Frame
        button_frame = Frame(t, bg='white')
        button_frame.pack(pady=30)
        
        # Python Quiz Button
        python_button = Button(button_frame, text='PYTHON QUIZ', 
                             font=('arial', 14), width=20, height=2,
                             command=pythonquestion)
        python_button.grid(row=0, column=0, padx=20, pady=10)
        
        # Java Quiz Button
        java_button = Button(button_frame, text='JAVA QUIZ', 
                           font=('arial', 14), width=20, height=2,
                           command=javaquestion)
        java_button.grid(row=1, column=0, padx=20, pady=10)
        
        # Exit Button
        exit_button = Button(button_frame, text='EXIT', 
                           font=('arial', 14), width=20, height=2,
                           command=t.destroy)
        exit_button.grid(row=2, column=0, padx=20, pady=10)

    # Initialize the application
    create_widgets()
    t.mainloop() 