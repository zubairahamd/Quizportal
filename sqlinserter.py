import customtkinter as ctk
import pymysql
from CTkMessagebox import CTkMessagebox

app = ctk.CTk()
app.title("Quiz Portal - Reappear Insert")
app.geometry("1530x790+0+0")
app.config(bg="#2A3335")

def pythonsave():
    try:
        db = pymysql.connect(host='localhost', user='root', password='root', database='quizportal')
        cur = db.cursor()
        
        xa = qno_entry.get()
        xb = question_entry.get()
        xc = op1_entry.get()
        xd = op2_entry.get()
        xe = op3_entry.get()
        xf = op4_entry.get()
        xg = correct_entry.get()
        
        # Validate inputs
        if not all([xa, xb, xc, xd, xe, xf, xg]):
            CTkMessagebox(title="Error", message="All fields are required!", icon="cancel")
            return
            
        # Convert question number to integer
        try:
            xa = int(xa)
        except ValueError:
            CTkMessagebox(title="Error", message="Question number must be an integer!", icon="cancel")
            return

        sql = "INSERT INTO sql_mcq VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (xa, xb, xc, xd, xe, xf, xg))
        
        db.commit()
        CTkMessagebox(title="Success", message="DATA SAVED SUCCESSFULLY", 
                     icon="check", option_1="Ok")
        
    except pymysql.Error as e:
        CTkMessagebox(title="Database Error", message=f"Error: {str(e)}", icon="cancel")
    finally:
        db.close()

# Create main frame
main_frame = ctk.CTkFrame(app, corner_radius=15, fg_color="#2A3335")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create content frame
content_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color="#222222")
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Title
title_label = ctk.CTkLabel(
    content_frame,
    text="SQL QUIZ INSERTER",
    font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
    text_color="#ffffff"
)
title_label.pack(pady=10)

# Form container
form_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
form_frame.pack(padx=20, pady=20)

# Question Number
qno_label = ctk.CTkLabel(
    form_frame,
    text="Question No.",
    font=ctk.CTkFont(size=14),
    text_color="#ffffff"
)
qno_label.pack(anchor="w", pady=(10, 0))
qno_entry = ctk.CTkEntry(
    form_frame,
    width=400,
    height=20,
    font=ctk.CTkFont(size=14)
)
qno_entry.pack(pady=(5, 10))

# Question
question_label = ctk.CTkLabel(
    form_frame,
    text="Write Question...",
    font=ctk.CTkFont(size=14),
    text_color="#ffffff"
)
question_label.pack(anchor="w", pady=(10, 0))
question_entry = ctk.CTkEntry(
    form_frame,
    width=400,
    height=20,
    font=ctk.CTkFont(size=14)
)
question_entry.pack(pady=(5, 10))

# Option 1
op1_label = ctk.CTkLabel(
    form_frame,
    text="Option 1",
    font=ctk.CTkFont(size=14),
    text_color="#ffffff"
)
op1_label.pack(anchor="w", pady=(10, 0))
op1_entry = ctk.CTkEntry(
    form_frame,
    width=400,
    height=20,
    font=ctk.CTkFont(size=14)
)
op1_entry.pack(pady=(5, 10))

# Option 2
op2_label = ctk.CTkLabel(
    form_frame,
    text="Option 2",
    font=ctk.CTkFont(size=14),
    text_color="#ffffff"
)
op2_label.pack(anchor="w", pady=(10, 0))
op2_entry = ctk.CTkEntry(
    form_frame,
    width=400,
    height=20,
    font=ctk.CTkFont(size=14)
)
op2_entry.pack(pady=(5, 10))

# Option 3
op3_label = ctk.CTkLabel(
    form_frame,
    text="Option 3",
    font=ctk.CTkFont(size=14),
    text_color="#ffffff"
)
op3_label.pack(anchor="w", pady=(10, 0))
op3_entry = ctk.CTkEntry(
    form_frame,
    width=400,
    height=20,
    font=ctk.CTkFont(size=14)
)
op3_entry.pack(pady=(5, 10))

# Option 4
op4_label = ctk.CTkLabel(
    form_frame,
    text="Option 4",
    font=ctk.CTkFont(size=14),
    text_color="#ffffff"
)
op4_label.pack(anchor="w", pady=(10, 0))
op4_entry = ctk.CTkEntry(
    form_frame,
    width=400,
    height=20,
    font=ctk.CTkFont(size=14)
)
op4_entry.pack(pady=(5, 10))

# Correct Answer
correct_label = ctk.CTkLabel(
    form_frame,
    text="Correct Answer",
    font=ctk.CTkFont(size=14),
    text_color="#ffffff"
)
correct_label.pack(anchor="w", pady=(10, 0))
correct_entry = ctk.CTkEntry(
    form_frame,
    width=400,
    height=20,
    font=ctk.CTkFont(size=14)
)
correct_entry.pack(pady=(5, 10))

# Insert button
insert_button = ctk.CTkButton(
    form_frame,
    text="Insert",
    font=ctk.CTkFont(size=15, weight="bold"),
    corner_radius=10,
    border_width=0,
    height=50,
    fg_color="#3a7ebf",
    hover_color="#2d5f8f",
    command=pythonsave
)
insert_button.pack(pady=20)

app.mainloop()