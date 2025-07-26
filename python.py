import customtkinter as ctk
import pymysql
from tkinter import messagebox

# Create main window
root = ctk.CTk()
root.title("Python Question Entry")
root.geometry("1530x790+0+0")

# Create header
header_frame = ctk.CTkFrame(root, fg_color=("#1f538d", "#2b5b9e"))
header_frame.pack(pady=0, padx=0, fill="x")

title_label = ctk.CTkLabel(
    header_frame,
    text="Python Question Entry",
    font=("Arial", 32, "bold"),
    text_color="white"
)
title_label.pack(pady=5)

# Create main content frame
main_frame = ctk.CTkFrame(root, fg_color="transparent")
main_frame.pack(fill="both", expand=True, pady=5)

# Create form frame
form_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"))
form_frame.pack(pady=20, padx=20, fill="both", expand=True)

def save_question():
    question = question_entry.get("1.0", "end-1c").strip()
    options = [entry.get().strip() for entry in options_entries]
    correct_answer = correct_answer_entry.get().strip()
    
    if not question or not all(options) or not correct_answer:
        messagebox.showerror("Error", "Please fill all fields!")
        return
        
    try:
        db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='quizportal'
        )
        cur = db.cursor()
        
        sql = "INSERT INTO python (question, option1, option2, option3, option4, correct_answer) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (question, *options, correct_answer))
        db.commit()
        
        messagebox.showinfo("Success", "Question saved successfully!")
        
        # Clear form
        question_entry.delete("1.0", "end")
        for entry in options_entries:
            entry.delete(0, "end")
        correct_answer_entry.delete(0, "end")
        
        db.close()
        
    except Exception as e:
        messagebox.showerror("Error", f"Database Error: {str(e)}")

# Question entry
question_label = ctk.CTkLabel(form_frame, text="Question:", font=("Arial", 16, "bold"))
question_label.pack(pady=(20, 5))
question_entry = ctk.CTkTextbox(form_frame, width=800, height=30, font=("Arial", 14))
question_entry.pack(pady=5)

# Options entries
options_entries = []
for i in range(4):
    option_label = ctk.CTkLabel(form_frame, text=f"Option {i+1}:", font=("Arial", 16, "bold"))
    option_label.pack(pady=(20, 5))
    option_entry = ctk.CTkEntry(form_frame, width=800, height=40, font=("Arial", 14))
    option_entry.pack(pady=5)
    options_entries.append(option_entry)

# Correct answer entry
correct_answer_label = ctk.CTkLabel(form_frame, text="Correct Answer:", font=("Arial", 16, "bold"))
correct_answer_label.pack(pady=(20, 5))
correct_answer_entry = ctk.CTkEntry(form_frame, width=800, height=40, font=("Arial", 14))
correct_answer_entry.pack(pady=5)

# Save button
save_button = ctk.CTkButton(
    form_frame,
    text="Save Question",
    width=200,
    height=40,
    command=save_question,
    font=("Arial", 14)
)
save_button.pack(pady=10)

# Start the application
root.mainloop() 