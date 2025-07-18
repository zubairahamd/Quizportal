import customtkinter as ctk
from tkinter import messagebox
import os
import pymysql
from adminmanagment import *

def admin_login():
    def verify_admin():
        try:
            # Get entered values
            entered_adminid = adminid_entry.get()
            entered_password = password_entry.get()

            # Connect to database
            db = pymysql.connect(
                host='localhost',
                user='root',
                passwd='root',
                database='quizportal'
            )
            cur = db.cursor()

            # Check admin credentials
            sql = "SELECT * FROM admininfo WHERE adminid=%s AND password=%s"
            cur.execute(sql, (entered_adminid, entered_password))
            result = cur.fetchone()

            if result:
                messagebox.showinfo("Success", "Welcome Admin!")
                root.destroy()
                adminenter()  # Call adminenter function
                os.system('python admindashboard.py')  # VerboseObjectInputStream('admindashboard.py')  # Open the admin dashboard
            else:
                messagebox.showerror("Error", "Invalid Admin ID or Password!")
                adminid_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

            db.close()

        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    # Create CustomTkinter root window (not Toplevel)
    root = ctk.CTk()  # Changed from CTkToplevel to CTk
    root.title("Admin Login")
    root.geometry("800x900+365+0")  # Centered position

    # Create header frame
    header_frame = ctk.CTkFrame(root, fg_color=("#1f538d", "#2b5b9e"))
    header_frame.pack(pady=0, padx=0, fill="x")

    # Add title
    title_label = ctk.CTkLabel(
        header_frame,
        text="Admin Login Portal",
        font=("Arial", 32, "bold"),
        text_color="white"
    )
    title_label.pack(pady=20)

    # Create main content frame
    main_frame = ctk.CTkFrame(root, fg_color="transparent")
    main_frame.pack(fill="both", expand=True, pady=20)

    # Create login frame with fixed width and centered
    login_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"), width=500, height=400)
    login_frame.pack(pady=20, padx=20, anchor="center")

    # Center the login frame
    login_frame.pack_propagate(False)  # Prevent frame from shrinking

    # Admin ID
    adminid_label = ctk.CTkLabel(login_frame, text="Admin ID:", font=("Arial", 16, "bold"))
    adminid_label.pack(pady=(40, 5))
    adminid_entry = ctk.CTkEntry(login_frame, width=400, height=40, font=("Arial", 14))
    adminid_entry.pack(pady=5)

    # Password
    password_label = ctk.CTkLabel(login_frame, text="Password:", font=("Arial", 16, "bold"))
    password_label.pack(pady=(20, 5))
    password_entry = ctk.CTkEntry(login_frame, width=400, height=40, font=("Arial", 14), show="*")
    password_entry.pack(pady=5)

    # Login button
    login_button = ctk.CTkButton(
        login_frame,
        text="Login",
        width=200,
        height=40,
        command=verify_admin,
        font=("Arial", 14)
    )
    login_button.pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    admin_login()