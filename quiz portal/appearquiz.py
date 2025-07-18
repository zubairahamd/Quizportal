import customtkinter as ctk

# Set the appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main window
app = ctk.CTk()
app.title("Programming Dashboard")
app.geometry("1530x790+0+0")

# Configure grid weights for better responsiveness
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

# Create a frame for the header with gradient effect
header_frame = ctk.CTkFrame(app, fg_color=("#1f538d", "#2b5b9e"))
header_frame.pack(pady=0, padx=0, fill="x")

# Add title label with shadow effect
title_label = ctk.CTkLabel(
    header_frame,
    text="Student Programming Dashboard",
    font=("Arial", 32, "bold"),
    text_color="white"
)
title_label.pack(pady=20)

# Create main content frame
main_frame = ctk.CTkFrame(app, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=40, pady=20)

# Create a frame for student information at the top
info_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"))
info_frame.pack(pady=20, padx=20, fill="x")

# Add a subtitle
subtitle_label = ctk.CTkLabel(
    info_frame,
    text="Student Information",
    font=("Arial", 20, "bold"),
    text_color=("#ffffff", "#ffffff")
)
subtitle_label.pack(pady=(20, 10))

# Create a frame for name and roll number in a row
input_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
input_frame.pack(pady=20, padx=40, fill="x")

# Add name field (left side)
name_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
name_frame.pack(side="left", padx=20, expand=True)
name_label = ctk.CTkLabel(
    name_frame,
    text="Name:",
    font=("Arial", 16, "bold"),
    text_color=("#ffffff", "#ffffff")
)
name_label.pack(pady=5)
name_entry = ctk.CTkEntry(
    name_frame,
    width=400,
    height=40,
    font=("Arial", 14),
    placeholder_text="Enter your name"
)
name_entry.pack(pady=5)

# Add roll number field (right side)
roll_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
roll_frame.pack(side="right", padx=20, expand=True)
roll_label = ctk.CTkLabel(
    roll_frame,
    text="Roll Number:",
    font=("Arial", 16, "bold"),
    text_color=("#ffffff", "#ffffff")
)
roll_label.pack(pady=5)
roll_entry = ctk.CTkEntry(
    roll_frame,
    width=400,
    height=40,
    font=("Arial", 14),
    placeholder_text="Enter your roll number"
)
roll_entry.pack(pady=5)

# Create a frame for programming language buttons
button_frame = ctk.CTkFrame(main_frame, fg_color=("#2b2b2b", "#3b3b3b"))
button_frame.pack(pady=20, padx=20, fill="x", expand=True)

# Add a subtitle for programming languages
lang_subtitle = ctk.CTkLabel(
    button_frame,
    text="Select Programming Language",
    font=("Arial", 20, "bold"),
    text_color=("#ffffff", "#ffffff")
)
lang_subtitle.pack(pady=(20, 10))

# Create a frame for buttons with grid layout
buttons_container = ctk.CTkFrame(button_frame, fg_color="transparent")
buttons_container.pack(pady=20, padx=40, fill="both", expand=True)

# Configure grid for buttons
buttons_container.grid_columnconfigure((0, 1, 2), weight=1)
buttons_container.grid_rowconfigure((0, 1, 2), weight=1)

# Add programming language buttons with improved styling
languages = ["Python", "Java", "SQL", "HTML", "CSS"]
buttons = []

for idx, lang in enumerate(languages):
    row = idx // 3
    col = idx % 3
    btn = ctk.CTkButton(
        buttons_container,
        text=lang,
        width=300,
        height=50,
        font=("Arial", 16, "bold"),
        corner_radius=10,
        fg_color=("#1f538d", "#2b5b9e"),
        hover_color=("#2b5b9e", "#3b6bb0"),
        command=lambda l=lang: print(f"Selected: {l}")
    )
    btn.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")
    buttons.append(btn)

# Start the application
if __name__ == "__main__":
    app.mainloop() 