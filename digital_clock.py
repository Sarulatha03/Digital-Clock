import tkinter as tk
from time import strftime

# Create a tkinter window
window = tk.Tk()
window.title("Digital Clock")

# Function to update the time
def time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, time)  # Update every 1 second

# Create a label to display the time
label = tk.Label(window, font=("calibri", 40, "bold"), background="purple", foreground="white")
label.pack(anchor="center")

# Start the clock
time()

# Run the tkinter event loop
window.mainloop()
