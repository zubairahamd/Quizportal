import customtkinter as ctk
import pymysql
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def userresult():
    # Create the main window
    app = ctk.CTk()
    app.title("User Results")
    app.geometry("1530x790+0+0")

    # Create header frame
    header_frame = ctk.CTkFrame(app, fg_color=("#1f538d", "#2b5b9e"))
    header_frame.pack(pady=0, padx=0, fill="x")

    # Add title
    title_label = ctk.CTkLabel(
        header_frame,
        text="User Results",
        font=("Brush Script MT", 40, "bold"),
        text_color="white"
    )
    title_label.pack(pady=20)

    # Create main frame
    main_frame = ctk.CTkFrame(app, fg_color="transparent")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Create email input frame
    email_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    email_frame.pack(fill="x", padx=20, pady=10)

    email_label = ctk.CTkLabel(
        email_frame,
        text="Enter Email:",
        font=("Brush Script MT", 20),
        text_color="white"
    )
    email_label.pack(side="left", padx=10)

    email_entry = ctk.CTkEntry(
        email_frame,
        width=300,
        height=35,
        font=("Arial", 14)
    )
    email_entry.pack(side="left", padx=10)

    # Create Treeview
    style = ttk.Style()
    style.configure("Treeview", 
                    background="#2b2b2b",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#2b2b2b")
    style.configure("Treeview.Heading", 
                    background="#1f538d",
                    foreground="white",
                    relief="flat")
    style.map("Treeview.Heading",
                background=[('active', '#2b5b9e')])

    # Create Treeview with scrollbar
    tree_frame = ctk.CTkFrame(main_frame)
    tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side="right", fill="y")

    tree = ttk.Treeview(tree_frame, 
                        columns=("rollno", "name", "coursename", "totalscore"),
                        show="headings",
                        yscrollcommand=tree_scroll.set)

    tree_scroll.config(command=tree.yview)

    # Configure columns
    tree.heading("rollno", text="Roll No")
    tree.heading("name", text="Name")
    tree.heading("coursename", text="Course")
    tree.heading("totalscore", text="Score")

    tree.column("rollno", width=100, anchor="center")
    tree.column("name", width=200, anchor="center")
    tree.column("coursename", width=150, anchor="center")
    tree.column("totalscore", width=100, anchor="center")

    tree.pack(fill="both", expand=True)

    def load_results():
        try:
            # Clear existing items
            for item in tree.get_children():
                tree.delete(item)
                
            # Connect to database
            db = pymysql.connect(host='localhost', user='root', password='root', database='quizportal')
            cur = db.cursor()
            
            # Fetch results
            sql = "SELECT rollno, name, coursename, totalscore FROM resulttable"
            cur.execute(sql)
            results = cur.fetchall()
            
            # Insert results into treeview
            for result in results:
                tree.insert("", "end", values=result)
                
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Failed to load results: {str(e)}")
        finally:
            if 'db' in locals():
                db.close()

    def send_result():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a result to send")
            return
            
        email = email_entry.get().strip()
        if not email:
            messagebox.showwarning("Warning", "Please enter an email address")
            return
            
        try:
            # Get selected result
            values = tree.item(selected_item[0])['values']
            rollno, name, course, score = values
            
            # Create email content
            from_address = "abbasaman77@gmail.com"
            to_address = email
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"Quiz Result - {course}"
            msg['From'] = from_address
            msg['To'] = to_address
            
            # Create HTML content
            html = f"""
            <html>
                <body style="font-family: Arial, sans-serif; padding: 20px;">
                    <h2 style="color: #1f538d;">Quiz Result</h2>
                    <p>Dear {name},</p>
                    <p>Here is your quiz result:</p>
                    <table style="border-collapse: collapse; width: 100%; margin: 20px 0;">
                        <tr style="background-color: #1f538d; color: white;">
                            <th style="padding: 10px; border: 1px solid #ddd;">Roll No</th>
                            <th style="padding: 10px; border: 1px solid #ddd;">Course</th>
                            <th style="padding: 10px; border: 1px solid #ddd;">Score</th>
                        </tr>
                        <tr>
                            <td style="padding: 10px; border: 1px solid #ddd;">{rollno}</td>
                            <td style="padding: 10px; border: 1px solid #ddd;">{course}</td>
                            <td style="padding: 10px; border: 1px solid #ddd;">{score}</td>
                        </tr>
                    </table>
                    <p>Thank you for taking the quiz!</p>
                </body>
            </html>
            """
            
            part = MIMEText(html, 'html')
            msg.attach(part)
            
            # Email credentials
            username = 'abbasaman77@gmail.com'
            password = 'yhgttirbjkmhjrtm'  # Replace with the App Password you generated
            
            # Send email with better error handling
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(username, password)
                server.sendmail(from_address, to_address, msg.as_string())
                server.quit()
                messagebox.showinfo("Success", f"Result sent to {email}")
            except smtplib.SMTPAuthenticationError:
                messagebox.showerror("Error", "Authentication failed. Please make sure you're using an App Password.")
            except smtplib.SMTPException as e:
                messagebox.showerror("Error", f"Failed to send email: {str(e)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send result: {str(e)}")

    # Create button frame
    button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    button_frame.pack(pady=20)

    # Send Result button
    send_btn = ctk.CTkButton(
        button_frame,
        text="Send Result",
        width=200,
        height=40,
        command=send_result,
        font=("Brush Script MT", 20),
        fg_color="#4CAF50",
        hover_color="#45a049"
    )
    send_btn.pack(side="left", padx=10)

    # Refresh button
    refresh_btn = ctk.CTkButton(
        button_frame,
        text="Refresh",
        width=200,
        height=40,
        command=load_results,
        font=("Brush Script MT", 20),
        fg_color="#2196F3",
        hover_color="#1976D2"
    )
    refresh_btn.pack(side="left", padx=10)

    # Load initial results
    load_results()

    app.mainloop() 