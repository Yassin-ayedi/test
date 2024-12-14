import tkinter as tk
from tkinter import messagebox


def create_interface():
    result = ""  # Variable to store the result

    def get_value():
        nonlocal result  # Allow modification of the outer variable
        result = entry.get()  # Get the string from the entry widget
        root.destroy()  # Close the tkinter window

    # Create the tkinter root window
    root = tk.Tk()
    root.title("Input Value")  # Title of the window
    root.geometry("300x150")  # Set the window size

    # Label widget to instruct the user
    label = tk.Label(root, text="Enter a string:")
    label.pack(pady=5)

    # Entry widget for user input
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)

    # Button to trigger the function
    submit_button = tk.Button(root, text="Submit", command=get_value)
    submit_button.pack(pady=10)

    # Start the tkinter main loop
    root.mainloop()

    return result  # Return the string after the GUI closes


# Call the function and store the result
user_input_string = create_interface()
print(f"User entered: {user_input_string}")
