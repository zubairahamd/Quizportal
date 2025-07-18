import customtkinter as ctk
from tkinter import messagebox
import os
import sys

class QuizPortal(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Quiz Portal - Main Menu")
        self.geometry("1200x720+100+50")
        self.config(bg="#2A3335")
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#2A3335")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Create content frame
        self.content_frame = ctk.CTkFrame(self.main_frame, corner_radius=15, fg_color="#222222")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.content_frame,
            text="QUIZ PORTAL",
            font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(pady=20)
        
        # Create buttons frame
        self.buttons_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.buttons_frame.pack(padx=40, pady=20)
        
        # Create buttons with consistent styling
        button_style = {
            "font": ctk.CTkFont(size=15, weight="bold"),
            "corner_radius": 10,
            "border_width": 0,
            "height": 50,
            "fg_color": "#3a7ebf",
            "hover_color": "#2d5f8f",
            "width": 300
        }
        
        # Student Management Section
        self.create_section_label("Student Management", self.buttons_frame)
        self.create_button("Student Registration", self.open_signup, self.buttons_frame, **button_style)
        self.create_button("Student Management", self.open_students, self.buttons_frame, **button_style)
        
        # Quiz Management Section
        self.create_section_label("Quiz Management", self.buttons_frame)
        self.create_button("Quiz Appear", self.open_quiz_appear, self.buttons_frame, **button_style)
        self.create_button("HTML/CSS Quiz", self.open_html_quiz, self.buttons_frame, **button_style)
        self.create_button("Java Quiz", self.open_java_quiz, self.buttons_frame, **button_style)
        self.create_button("Python Quiz", self.open_python_quiz, self.buttons_frame, **button_style)
        self.create_button("SQL Quiz", self.open_sql_quiz, self.buttons_frame, **button_style)
        
        # Exam Management Section
        self.create_section_label("Exam Management", self.buttons_frame)
        self.create_button("Exam Schedule", self.open_exam_schedule, self.buttons_frame, **button_style)
        self.create_button("Result Table", self.open_result_table, self.buttons_frame, **button_style)
        
        # Reappear Management Section
        self.create_section_label("Reappear Management", self.buttons_frame)
        self.create_button("Reappear Insert", self.open_reappear_insert, self.buttons_frame, **button_style)
        self.create_button("Reappear Delete", self.open_reappear_delete, self.buttons_frame, **button_style)
        self.create_button("Reappear Find", self.open_reappear_find, self.buttons_frame, **button_style)
        
        # Certificate Management Section
        self.create_section_label("Certificate Management", self.buttons_frame)
        self.create_button("Certificate Issue Insert", self.open_certificate_insert, self.buttons_frame, **button_style)
        self.create_button("Certificate Issue Delete", self.open_certificate_delete, self.buttons_frame, **button_style)
        self.create_button("Certificate Issue Find", self.open_certificate_find, self.buttons_frame, **button_style)
        self.create_button("Certificate Issue Show", self.open_certificate_show, self.buttons_frame, **button_style)
        self.create_button("Certificate Issue Save", self.open_certificate_save, self.buttons_frame, **button_style)
        
        # Exit button
        self.create_button("Exit", self.exit_application, self.buttons_frame, **button_style)
    
    def create_section_label(self, text, parent):
        label = ctk.CTkLabel(
            parent,
            text=text,
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#ffffff"
        )
        label.pack(pady=(20, 10))
    
    def create_button(self, text, command, parent, **kwargs):
        button = ctk.CTkButton(
            parent,
            text=text,
            command=command,
            **kwargs
        )
        button.pack(pady=10)
        return button
    
    def open_signup(self):
        os.system('python signup.py')
    
    def open_students(self):
        os.system('python projectstudents.py')
    
    def open_quiz_appear(self):
        os.system('python projectquizappear.py')
    
    def open_html_quiz(self):
        os.system('python htmlcssquestion.py')
    
    def open_java_quiz(self):
        os.system('python javaquestion.py')
    
    def open_python_quiz(self):
        os.system('python pythonquestion.py')
    
    def open_sql_quiz(self):
        os.system('python sqlquestion.py')
    
    def open_exam_schedule(self):
        os.system('python projectexamschedule.py')
    
    def open_result_table(self):
        os.system('python projectresulttable.py')
    
    def open_reappear_insert(self):
        os.system('python reappearinsert.py')
    
    def open_reappear_delete(self):
        os.system('python reappeardelete.py')
    
    def open_reappear_find(self):
        os.system('python reappearfind.py')
    
    def open_certificate_insert(self):
        os.system('python certificateissueinsert.py')
    
    def open_certificate_delete(self):
        os.system('python certificateissuedelete.py')
    
    def open_certificate_find(self):
        os.system('python certificateissuefind.py')
    
    def open_certificate_show(self):
        os.system('python certificateissueshow.py')
    
    def open_certificate_save(self):
        os.system('python certificateissuesave.py')
    
    def exit_application(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.quit()

if __name__ == "__main__":
    app = QuizPortal()
    app.mainloop() 