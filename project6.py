import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

# Function to check reminders
def check_reminders():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        for reminder_time, message in reminders.items():
            if reminder_time == current_time:
                messagebox.showinfo("Reminder", f"Time: {reminder_time}\nMessage: {message}")
                del reminders[reminder_time]  # Remove the reminder after showing it
                break
        time.sleep(1)  # Check every second

# Function to set a reminder
def set_reminder():
    time_str = time_entry.get()
    message = message_entry.get()
    if not time_str or not message:
        messagebox.showerror("Error", "Please fill in both fields!")
        return

    try:
        datetime.strptime(time_str, "%H:%M:%S")  # Validate time format
        reminders[time_str] = message
        messagebox.showinfo("Success", f"Reminder set for {time_str}")
        time_entry.delete(0, tk.END)
        message_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid time format! Use HH:MM:SS")

# Initialize the main application window
root = tk.Tk()
root.title("Simple Reminder Application")
root.geometry("400x250")
root.resizable(False, False)

# Label and entry for time
tk.Label(root, text="Enter Time (HH:MM:SS):", font=("Arial", 12)).pack(pady=10)
time_entry = tk.Entry(root, font=("Arial", 12), width=20)
time_entry.pack(pady=5)

# Label and entry for message
tk.Label(root, text="Enter Reminder Message:", font=("Arial", 12)).pack(pady=10)
message_entry = tk.Entry(root, font=("Arial", 12), width=40)
message_entry.pack(pady=5)

# Button to set a reminder
set_button = tk.Button(root, text="Set Reminder", font=("Arial", 12), command=set_reminder)
set_button.pack(pady=20)

# Dictionary to store reminders
reminders = {}

# Run the reminder checking in a separate thread
threading.Thread(target=check_reminders, daemon=True).start()

# Run the GUI application
root.mainloop()
