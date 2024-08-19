import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    # Simple validation
    if not name or not email or not age:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    # For demonstration, we'll just show the data in a message box
    messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}\nAge: {age}")
    
    # Clear the form fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place labels and entry widgets for name, email, and age
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()