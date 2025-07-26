import tkinter
import pymysql
from tkinter import * 
from tkinter import messagebox

def htmlcssquestion():
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

    # Initialize window
    t = tkinter.Tk()
    t.title('HTML & CSS')
    t.geometry('700x700')
    t.config(bg='white')

    def create_widgets():
        global title_label, question_label, x, r1, r2, r3, r4, check_button, correct_answer
        
        title_label = Label(t, text='HTML & CSS', font=('arial', 20))
        title_label.place(x=240, y=10)
        
        question_label = Label(t, text='Question Name', font=('arial', 15))
        question_label.place(x=50, y=180)
        
        x = IntVar()
        
        r1 = Radiobutton(t, text='Option1', variable=x, value=0, 
                        font=('arial', 15), command=check1)
        r1.place(x=50, y=220)
        
        r2 = Radiobutton(t, text='Option2', variable=x, value=1, 
                        font=('arial', 15), command=check2)
        r2.place(x=50, y=260)
        
        r3 = Radiobutton(t, text='Option3', variable=x, value=2, 
                        font=('arial', 15), command=check3)
        r3.place(x=50, y=300)
        
        r4 = Radiobutton(t, text='Option4', variable=x, value=3, 
                        font=('arial', 15), command=check4)
        r4.place(x=50, y=340)
        
        check_button = Button(t, text='Check', command=check)
        check_button.place(x=140, y=480)
        
        correct_answer = Label(t, text='.', fg='white', bg='white')
        correct_answer.place(x=40, y=520)

    def questionfill():
        global ht
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='quizportal')
            cur = db.cursor()
            sql = "select qname,opt1,opt2,opt3,opt4,correct from html_css"
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

    def check():
        global score, i
        if i == ht - 1:
            messagebox.showinfo("Score", str(score))
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