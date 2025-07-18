import customtkinter as ctk
import pymysql
from tkinter import messagebox

def java_questions():
    def save_question():
        question = question_entry.get("1.0", "end-1c").strip()
        options = [entry.get().strip() for entry in options_entries]
        correct_answer = int(correct_answer_var.get())
        
        if not question or not all(options):
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
            
            sql = "INSERT INTO javaquestions (question, option1, option2, option3, option4, correct_answer) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(sql, (question, *options, correct_answer))
            db.commit()
            
            messagebox.showinfo("Success", "Question saved successfully!")
            
            # Clear form
            question_entry.delete("1.0", "end")
            for entry in options_entries:
                entry.delete(0, "end")
            correct_answer_var.set("1")
            
            db.close()
            
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    # Create window
    root = ctk.CTkToplevel()
    root.title("Java Questions")
    root.geometry("1530x790+0+0")
    
    # Create header
    header_frame = ctk.CTkFrame(root, fg_color=("#1f538d", "#2b5b9e"))
    header_frame.pack(pady=0, padx=0, fill="x")
    
    title_label = ctk.CTkLabel(
        header_frame,
        text="Java Questions",
        font=("Arial", 32, "bold"),
        text_color="white"
    )
    title_label.pack(pady=20)
    
    # Create main content frame
    main_frame = ctk.CTkFrame(root, fg_color="transparent")
    main_frame.pack(fill="both", expand=True, pady=20)
    
    # Create form frame
    form_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"))
    form_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Question entry
    question_label = ctk.CTkLabel(form_frame, text="Question:", font=("Arial", 16, "bold"))
    question_label.pack(pady=(20, 5))
    question_entry = ctk.CTkTextbox(form_frame, width=800, height=100, font=("Arial", 14))
    question_entry.pack(pady=5)
    
    # Options entries
    options_entries = []
    for i in range(4):
        option_label = ctk.CTkLabel(form_frame, text=f"Option {i+1}:", font=("Arial", 16, "bold"))
        option_label.pack(pady=(20, 5))
        option_entry = ctk.CTkEntry(form_frame, width=800, height=40, font=("Arial", 14))
        option_entry.pack(pady=5)
        options_entries.append(option_entry)
    
    # Correct answer selection
    correct_answer_label = ctk.CTkLabel(form_frame, text="Correct Answer:", font=("Arial", 16, "bold"))
    correct_answer_label.pack(pady=(20, 5))
    correct_answer_var = ctk.StringVar(value="1")
    for i in range(4):
        radio = ctk.CTkRadioButton(
            form_frame,
            text=f"Option {i+1}",
            variable=correct_answer_var,
            value=str(i+1),
            font=("Arial", 14)
        )
        radio.pack(pady=5)
    
    # Save button
    save_button = ctk.CTkButton(
        form_frame,
        text="Save Question",
        width=200,
        height=40,
        command=save_question,
        font=("Arial", 14)
    )
    save_button.pack(pady=30)

if __name__ == "__main__":
    java_questions() 