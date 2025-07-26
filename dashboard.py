import customtkinter as ctk
from tkinter import messagebox, ttk
import pymysql
from CTkMessagebox import CTkMessagebox

# Set appearance mode and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create main window
root = ctk.CTk()
root.title("Admin Dashboard")
root.geometry("1530x790+0+0")
root.configure(fg_color="#2A3335")

# Create main frame
main_frame = ctk.CTkFrame(root, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create header
header_frame = ctk.CTkFrame(main_frame, fg_color="#3a7ebf", height=60)
header_frame.pack(fill="x", pady=(0, 20))

# Title
title_label = ctk.CTkLabel(
    header_frame,
    text="User Management Dashboard",
    font=ctk.CTkFont(size=24, weight="bold"),
    text_color="white"
)
title_label.pack(pady=10)

# Create content frame
content_frame = ctk.CTkFrame(main_frame, fg_color="#222222")
content_frame.pack(fill="both", expand=True)

# Create left panel for operations
left_panel = ctk.CTkFrame(content_frame, fg_color="transparent", width=300)
left_panel.pack(side="left", fill="y", padx=10, pady=10)

# Create right panel for table
right_panel = ctk.CTkFrame(content_frame, fg_color="transparent")
right_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Create Treeview with scrollbar
tree_frame = ctk.CTkFrame(right_panel)
tree_frame.pack(fill="both", expand=True)

tree = ttk.Treeview(
    tree_frame,
    columns=("Name", "Address", "Email", "City", "Phone", "UserID", "Password"),
    show="headings"
)

# Configure columns
tree.heading("Name", text="Name")
tree.heading("Address", text="Address")
tree.heading("Email", text="Email")
tree.heading("City", text="City")
tree.heading("Phone", text="Phone")
tree.heading("UserID", text="User ID")
tree.heading("Password", text="Password")

# Set column widths
tree.column("Name", width=150)
tree.column("Address", width=200)
tree.column("Email", width=200)
tree.column("City", width=100)
tree.column("Phone", width=120)
tree.column("UserID", width=120)
tree.column("Password", width=120)

# Add scrollbar
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Pack tree and scrollbar
tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Function to load data
def load_data():
    try:
        # Clear existing items
        for item in tree.get_children():
            tree.delete(item)
            
        # Connect to database
        db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='quizportal'
        )
        cur = db.cursor()
        
        # Fetch all users
        cur.execute("SELECT * FROM userinfo")
        rows = cur.fetchall()
        
        # Insert data into treeview
        for row in rows:
            tree.insert("", "end", values=row)
            
        db.close()
        
    except Exception as e:
        CTkMessagebox(
            title="Error",
            message=f"Error loading data: {str(e)}",
            icon="cancel"
        )

# Function to show add user window
def show_add_user_window():
    add_window = ctk.CTkToplevel(root)
    add_window.title("Add New User")
    add_window.geometry("500x600")
    
    # Create form frame
    form_frame = ctk.CTkFrame(add_window)
    form_frame.pack(padx=20, pady=20, fill="both", expand=True)
    
    # Title
    title = ctk.CTkLabel(
        form_frame,
        text="Add New User",
        font=ctk.CTkFont(size=20, weight="bold")
    )
    title.pack(pady=20)
    
    # Create entry fields with better layout
    fields = ["Name", "Address", "Email", "City", "Phone", "User ID", "Password"]
    entries = {}
    
    for field in fields:
        frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=5)
        
        label = ctk.CTkLabel(
            frame,
            text=field,
            font=ctk.CTkFont(size=14),
            width=100
        )
        label.pack(side="left", padx=(0, 10))
        
        entry = ctk.CTkEntry(
            frame,
            width=300,
            height=35,
            font=ctk.CTkFont(size=14)
        )
        entry.pack(side="left", fill="x", expand=True)
        entries[field] = entry
    
    # Add button with better styling
    add_btn = ctk.CTkButton(
        form_frame,
        text="Add User",
        font=ctk.CTkFont(size=14, weight="bold"),
        height=40,
        width=200,
        command=lambda: add_user(entries, add_window)
    )
    add_btn.pack(pady=20)

# Function to add user
def add_user(entries, window):
    try:
        eboxvalues = [entries[field].get() for field in ["Name", "Address", "Email", "City", "Phone", "User ID", "Password"]]
        
        if not all(values):
            CTkMessag(
                title="Error",
                message="Please fill all fields",
                icon="warning"
            )
            return
            
        db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='quizportal'
        )
        cur = db.cursor()
        
        sql = "INSERT INTO userinfo VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, values)
        db.commit()
        
        CTkMessagebox(
            title="Success",
            message="User added successfully!",
            icon="check"
        )
        
        window.destroy()
        load_data()
        
        db.close()
        
    except Exception as e:
        CTkMessagebox(
            title="Error",
            message=f"Error adding user: {str(e)}",
            icon="cancel"
        )

# Function to show update user window
def show_update_user_window():
    selected = tree.selection()
    if not selected:
        CTkMessagebox(
            title="Error",
            message="Please select a user to update",
            icon="warning"
        )
        return
        
    values = tree.item(selected[0])['values']
    
    update_window = ctk.CTkToplevel(root)
    update_window.title("Update User")
    update_window.geometry("500x600")
    
    form_frame = ctk.CTkFrame(update_window)
    form_frame.pack(padx=20, pady=20, fill="both", expand=True)
    
    # Title
    title = ctk.CTkLabel(
        form_frame,
        text="Update User",
        font=ctk.CTkFont(size=20, weight="bold")
    )
    title.pack(pady=20)
    
    fields = ["Name", "Address", "Email", "City", "Phone", "User ID", "Password"]
    entries = {}
    
    for i, field in enumerate(fields):
        frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=5)
        
        label = ctk.CTkLabel(
            frame,
            text=field,
            font=ctk.CTkFont(size=14),
            width=100
        )
        label.pack(side="left", padx=(0, 10))
        
        entry = ctk.CTkEntry(
            frame,
            width=300,
            height=35,
            font=ctk.CTkFont(size=14)
        )
        entry.insert(0, values[i])
        entry.pack(side="left", fill="x", expand=True)
        entries[field] = entry
    
    update_btn = ctk.CTkButton(
        form_frame,
        text="Update User",
        font=ctk.CTkFont(size=14, weight="bold"),
        height=40,
        width=200,
        command=lambda: update_user(entries, values[5], update_window)
    )
    update_btn.pack(pady=20)

# Function to update user
def update_user(entries, old_userid, window):
    try:
        values = [entries[field].get() for field in ["Name", "Address", "Email", "City", "Phone", "User ID", "Password"]]
        
        if not all(values):
            CTkMessagebox(
                title="Error",
                message="Please fill all fields",
                icon="warning"
            )
            return
            
        db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='quizportal'
        )
        cur = db.cursor()
        
        sql = """UPDATE userinfo 
                SET name=%s, address=%s, email=%s, city=%s, phone=%s, userid=%s, password=%s 
                WHERE userid=%s"""
        cur.execute(sql, values + [old_userid])
        db.commit()
        
        CTkMessagebox(
            title="Success",
            message="User updated successfully!",
            icon="check"
        )
        
        window.destroy()
        load_data()
        
        db.close()
        
    except Exception as e:
        CTkMessagebox(
            title="Error",
            message=f"Error updating user: {str(e)}",
            icon="cancel"
        )

# Function to delete user
def delete_user():
    selected = tree.selection()
    if not selected:
        CTkMessagebox(
            title="Error",
            message="Please select a user to delete",
            icon="warning"
        )
        return
        
    msg = CTkMessagebox(
        title="Confirm Delete",
        message="Are you sure you want to delete this user?",
        icon="warning",
        option_1="Yes",
        option_2="No"
    )
    
    if msg.get() == "Yes":
        try:
            userid = tree.item(selected[0])['values'][5]
            
            db = pymysql.connect(
                host='localhost',
                user='root',
                passwd='root',
                database='quizportal'
            )
            cur = db.cursor()
            
            sql = "DELETE FROM userinfo WHERE userid=%s"
            cur.execute(sql, (userid,))
            db.commit()
            
            CTkMessagebox(
                title="Success",
                message="User deleted successfully!",
                icon="check"
            )
            
            load_data()
            
            db.close()
            
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"Error deleting user: {str(e)}",
                icon="cancel"
            )

# Function to search user
def search_user():
    try:
        search_term = search_entry.get()
        if not search_term:
            load_data()
            return
            
        for item in tree.get_children():
            tree.delete(item)
            
        db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='quizportal'
        )
        cur = db.cursor()
        
        sql = "SELECT * FROM userinfo WHERE userid LIKE %s OR name LIKE %s"
        search_pattern = f"%{search_term}%"
        cur.execute(sql, (search_pattern, search_pattern))
        rows = cur.fetchall()
        
        for row in rows:
            tree.insert("", "end", values=row)
            
        db.close()
        
    except Exception as e:
        CTkMessagebox(
            title="Error",
            message=f"Error searching users: {str(e)}",
            icon="cancel"
        )

# Add operation buttons to left panel
add_btn = ctk.CTkButton(
    left_panel,
    text="Add New User",
    font=ctk.CTkFont(size=14, weight="bold"),
    height=40,
    command=show_add_user_window
)
add_btn.pack(pady=10, padx=20, fill="x")

update_btn = ctk.CTkButton(
    left_panel,
    text="Update User",
    font=ctk.CTkFont(size=14, weight="bold"),
    height=40,
    command=show_update_user_window
)
update_btn.pack(pady=10, padx=20, fill="x")

delete_btn = ctk.CTkButton(
    left_panel,
    text="Delete User",
    font=ctk.CTkFont(size=14, weight="bold"),
    height=40,
    command=delete_user
)
delete_btn.pack(pady=10, padx=20, fill="x")

# Search Frame
search_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
search_frame.pack(pady=20, padx=20, fill="x")

search_label = ctk.CTkLabel(
    search_frame,
    text="Search User:",
    font=ctk.CTkFont(size=14)
)
search_label.pack(anchor="w")

search_entry = ctk.CTkEntry(
    search_frame,
    placeholder_text="Enter User ID or Name",
    height=35
)
search_entry.pack(pady=5, fill="x")

search_btn = ctk.CTkButton(
    search_frame,
    text="Search",
    font=ctk.CTkFont(size=12),
    height=35,
    command=search_user
)
search_btn.pack(pady=5, fill="x")

# Refresh Button
refresh_btn = ctk.CTkButton(
    left_panel,
    text="Refresh Data",
    font=ctk.CTkFont(size=14, weight="bold"),
    height=40,
    command=load_data
)
refresh_btn.pack(pady=10, padx=20, fill="x")

# Load initial data
load_data()

# Start the application
root.mainloop() 