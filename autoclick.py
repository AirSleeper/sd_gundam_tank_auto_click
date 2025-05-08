import pyautogui
import threading
from pynput import mouse, keyboard
import tkinter as tk
from tkinter import messagebox

# Global variables
auto_clicking = False
click_thread = None
click_select_x = 0
click_select_y = 0
click_confirm_x = 0
click_confirm_y = 0
click_select_sleep = 2.5
click_confirm_sleep = 5

def auto_click():
    """Function to perform auto-clicking."""
    while auto_clicking:
        pyautogui.click(x=click_select_x, y=click_select_y)  # Coordinates for the click
        pyautogui.sleep(click_select_sleep)  # Adjust the sleep time as needed
        pyautogui.click(x=click_confirm_x, y=click_confirm_y)  # Coordinates for the clickg
        pyautogui.sleep(click_select_sleep)  # Adjust the sleep time as needed
        pyautogui.click(x=click_confirm_x, y=click_confirm_y)  # Coordinates for the click
        pyautogui.sleep(click_confirm_sleep)  # Adjust the sleep time as needed
        pyautogui.click(x=click_select_x, y=click_select_y)  # Coordinates for the click
        pyautogui.sleep(click_select_sleep)  # Adjust the sleep time as neededs

def start_auto_clicking():
    """Start the auto-clicking thread."""
    global auto_clicking, click_thread
    auto_clicking = True
    click_thread = threading.Thread(target=auto_click)
    click_thread.start()

def stop_auto_clicking():
    """Stop the auto-clicking thread."""
    global auto_clicking, click_thread
    auto_clicking = False
    if click_thread:
        click_thread.join()

def on_click(x, y, button, pressed):
    """Handle mouse click events."""
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

def on_press(key):
    """Handle keyboard press events."""
    try:
        if key.char == 's':  # Start auto-clicking with 's'
            print("Starting auto-clicking...")
            start_auto_clicking()
        elif key.char == 'e':  # End auto-clicking with 'e'
            print("Stopping auto-clicking...")
            stop_auto_clicking()
        elif key.char == 'g':  # Open GUI with 'g'
            print("Opening settings GUI...")
            open_gui()
    except AttributeError:
        pass

def update_variables():
    """Update global variables from the GUI inputs."""
    global click_select_x, click_select_y, click_confirm_x, click_confirm_y, click_select_sleep, click_confirm_sleep
    try:
        click_select_x = int(entry_select_x.get())
        click_select_y = int(entry_select_y.get())
        click_confirm_x = int(entry_confirm_x.get())
        click_confirm_y = int(entry_confirm_y.get())
        click_select_sleep = float(entry_select_sleep.get())
        click_confirm_sleep = float(entry_confirm_sleep.get())
        messagebox.showinfo("Success", "Variables updated successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def record_click(variable_name):
    """Record the next mouse click and update the specified variable."""
    def on_click(x, y, button, pressed):
        if pressed:
            if variable_name == "select_x":
                global click_select_x, click_select_y
                click_select_x, click_select_y = x, y
                entry_select_x.delete(0, tk.END)
                entry_select_x.insert(0, str(x))
                entry_select_y.delete(0, tk.END)
                entry_select_y.insert(0, str(y))
            elif variable_name == "confirm_x":
                global click_confirm_x, click_confirm_y
                click_confirm_x, click_confirm_y = x, y
                entry_confirm_x.delete(0, tk.END)
                entry_confirm_x.insert(0, str(x))
                entry_confirm_y.delete(0, tk.END)
                entry_confirm_y.insert(0, str(y))
            mouse_listener.stop()

    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

def open_gui():
    """Open the GUI for updating variables."""
    global entry_select_x, entry_select_y, entry_confirm_x, entry_confirm_y, entry_select_sleep, entry_confirm_sleep

    gui = tk.Tk()
    gui.title("Auto Clicker Settings")

    tk.Label(gui, text="Click Select X:").grid(row=0, column=0, padx=10, pady=5)
    entry_select_x = tk.Entry(gui)
    entry_select_x.grid(row=0, column=1, padx=10, pady=5)
    entry_select_x.insert(0, str(click_select_x))
    tk.Button(gui, text="Record", command=lambda: record_click("select_x")).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(gui, text="Click Select Y:").grid(row=1, column=0, padx=10, pady=5)
    entry_select_y = tk.Entry(gui)
    entry_select_y.grid(row=1, column=1, padx=10, pady=5)
    entry_select_y.insert(0, str(click_select_y))

    tk.Label(gui, text="Click Confirm X:").grid(row=2, column=0, padx=10, pady=5)
    entry_confirm_x = tk.Entry(gui)
    entry_confirm_x.grid(row=2, column=1, padx=10, pady=5)
    entry_confirm_x.insert(0, str(click_confirm_x))
    tk.Button(gui, text="Record", command=lambda: record_click("confirm_x")).grid(row=2, column=2, padx=10, pady=5)

    tk.Label(gui, text="Click Confirm Y:").grid(row=3, column=0, padx=10, pady=5)
    entry_confirm_y = tk.Entry(gui)
    entry_confirm_y.grid(row=3, column=1, padx=10, pady=5)
    entry_confirm_y.insert(0, str(click_confirm_y))

    tk.Label(gui, text="Click Select Sleep (s):").grid(row=4, column=0, padx=10, pady=5)
    entry_select_sleep = tk.Entry(gui)
    entry_select_sleep.grid(row=4, column=1, padx=10, pady=5)
    entry_select_sleep.insert(0, str(click_select_sleep))

    tk.Label(gui, text="Click Confirm Sleep (s):").grid(row=5, column=0, padx=10, pady=5)
    entry_confirm_sleep = tk.Entry(gui)
    entry_confirm_sleep.grid(row=5, column=1, padx=10, pady=5)
    entry_confirm_sleep.insert(0, str(click_confirm_sleep))

    tk.Button(gui, text="Update", command=update_variables).grid(row=6, column=0, columnspan=2, pady=10)

    tk.Button(gui, text="Start Auto-Clicking", command=start_auto_clicking).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(gui, text="Stop Auto-Clicking", command=stop_auto_clicking).grid(row=8, column=0, columnspan=2, pady=10)

    gui.mainloop()

if __name__ == "__main__":
    open_gui()