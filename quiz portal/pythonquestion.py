import tkinter
import pymysql
from tkinter import * 
from tkinter import messagebox
from datetime import datetime


ht=0
def pythonquestion():
    
    # Global variables
    score = 1
    ht = 0
    i = 0
    q = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    ans = ''
    student_name = ''
    student_roll = ''
    
    # Initialize window
    t = tkinter.Tk()
    t.title('PYTHON QUIZ')
    t.geometry('700x700')
    t.config(bg='white')

    def create_widgets():
        global title_label, question_label, x, r1, r2, r3, r4, check_button, correct_answer, name_label, name_entry, roll_label, roll_entry
        
        # Student info frame
        info_frame = Frame(t, bg='white')
        info_frame.pack(pady=10)
        
        name_label = Label(info_frame, text='Name:', font=('arial', 12))
        name_label.grid(row=0, column=0, padx=5)
        name_entry = Entry(info_frame, font=('arial', 12))
        name_entry.grid(row=0, column=1, padx=5)
        
        roll_label = Label(info_frame, text='Roll No:', font=('arial', 12))
        roll_label.grid(row=0, column=2, padx=5)
        roll_entry = Entry(info_frame, font=('arial', 12))
        roll_entry.grid(row=0, column=3, padx=5)
            
        title_label = Label(t, text='PYTHON QUIZ', font=('arial', 20))
        title_label.place(x=240, y=50)
        
        question_label = Label(t, text='Question Name', font=('arial', 15))
        question_label.place(x=50, y=180)
        
        x = IntVar()
        
        r1 = Radiobutton(t, text='Option1', variable=x, value=0, 
                        font=('arial', 15), command=lambda: [check1(), save_result()])
        r1.place(x=50, y=220)
        
        r2 = Radiobutton(t, text='Option2', variable=x, value=1, 
                        font=('arial', 15), command=lambda: [check2(), save_result()])
        r2.place(x=50, y=260)
        
        r3 = Radiobutton(t, text='Option3', variable=x, value=2, 
                        font=('arial', 15), command=lambda: [check3(), save_result()])
        r3.place(x=50, y=300)
        
        r4 = Radiobutton(t, text='Option4', variable=x, value=3, 
                        font=('arial', 15), command=lambda: [check4(), save_result()])
        r4.place(x=50, y=340)
        
        check_button = Button(t, text='Check', command=lambda: [check(), save_result()])
        check_button.place(x=140, y=480)
        
        correct_answer = Label(t, text='.', fg='white', bg='white')
        correct_answer.place(x=40, y=520)

    def questionfill():
        global ht
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='quizportal')
            cur = db.cursor()
            sql = "select qname,opt1,opt2,opt3,opt4,correct from python"
            cur.execute(sql)
            data = cur.fetchall()
            
            for res in data:
                q.append(res[0])
                a1.append(res[1])
                a2.append(res[2])
                a3.append(res[3])
                a4.append(res[4])
                a5.append(res[5])
                ht += 1
                
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")
        finally:
            if 'db' in locals():
                db.close()

    def first():
        global i
        i = 0
        update_question()

    def nextd():
        global i
        i += 1
        update_question()

    def update_question():
        question_label.config(text=q[i])
        r1.config(text=a1[i])
        r2.config(text=a2[i])
        r3.config(text=a3[i])
        r4.config(text=a4[i])
        correct_answer.config(text=a5[i])

    def check1():
        global ans
        ans = r1.cget("text")

    def check2():
        global ans
        ans = r2.cget("text")

    def check3():
        global ans
        ans = r3.cget("text")

    def check4():
        global ans
        ans = r4.cget("text")

    def save_result():
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='quizportal')
            cur = db.cursor()
            
            # Get student info
            student_name = name_entry.get()
            student_roll = roll_entry.get()
            
            if not student_name or not student_roll:
                messagebox.showerror("Error", "Please enter name and roll number!")
                return
                
            # Save result to database with updated structure
            sql = "INSERT INTO resulttable (rollno, coursename, name, totalscore) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (student_roll, 'Java', student_name, score))
            db.commit()
            
            messagebox.showinfo("Success", "Result saved successfully!")
            
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Failed to save result: {str(e)}")
        finally:
            if 'db' in locals():
                db.close()

    def check():
        global score, i
        if i == ht - 1:
            messagebox.showinfo("Score", f"Your score: {score}")
            save_result()  # Save result when quiz is complete
            return
            
        correct_answer_text = correct_answer.cget("text")
        if correct_answer_text == ans:
            score += 1
            messagebox.showinfo('Result', "Correct!")
        else:
            messagebox.showinfo('Result', 'Incorrect!')
            
        nextd()

    # Initialize the application
    create_widgets()
    questionfill()
    first()
    t.mainloop()