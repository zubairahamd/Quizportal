import customtkinter as ctk
from python_questions import python_questions
from java_questions import java_questions
from htmlcss_questions import htmlcss_questions
from sql_questions import sql_questions

# Create main window
root = ctk.CTk()
root.title("Question Inserter")
root.geometry("1530x790+0+0")

# Create header
header_frame = ctk.CTkFrame(root, fg_color=("#1f538d", "#2b5b9e"))
header_frame.pack(pady=0, padx=0, fill="x")

title_label = ctk.CTkLabel(
    header_frame,
    text="Question Inserter",
    font=("Arial", 32, "bold"),
    text_color="white"
)
title_label.pack(pady=20)

# Create main content frame
main_frame = ctk.CTkFrame(root, fg_color="transparent")
main_frame.pack(fill="both", expand=True)

# Create subject buttons frame
subject_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"))
subject_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a frame for buttons
buttons_frame = ctk.CTkFrame(subject_frame, fg_color="transparent")
buttons_frame.pack(pady=30, padx=30)

# Subject buttons with bigger size
python_btn = ctk.CTkButton(
    buttons_frame,
    text="Python",
    width=300,
    height=60,
    font=("Arial", 20, "bold"),
    fg_color="#1f538d",
    hover_color="#2b5b9e",
    command=python_questions
)
python_btn.pack(pady=15)

java_btn = ctk.CTkButton(
    buttons_frame,
    text="Java",
    width=300,
    height=60,
    font=("Arial", 20, "bold"),
    fg_color="#1f538d",
    hover_color="#2b5b9e",
    command=java_questions
)
java_btn.pack(pady=15)

htmlcss_btn = ctk.CTkButton(
    buttons_frame,
    text="HTML/CSS",
    width=300,
    height=60,
    font=("Arial", 20, "bold"),
    fg_color="#1f538d",
    hover_color="#2b5b9e",
    command=htmlcss_questions
)
htmlcss_btn.pack(pady=15)

sql_btn = ctk.CTkButton(
    buttons_frame,
    text="SQL",
    width=300,
    height=60,
    font=("Arial", 20, "bold"),
    fg_color="#1f538d",
    hover_color="#2b5b9e",
    command=sql_questions
)
sql_btn.pack(pady=15)

# Start the application
root.mainloop() 