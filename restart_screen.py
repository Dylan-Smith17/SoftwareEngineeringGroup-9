import sys
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

import os
import tkinter as tk
from PIL import Image, ImageTk


class RestartScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Laser Tag")
        self.geometry("1280x720")
        self.configure(background="black")

        # Get the current working directory securely
        self.current_dir = os.path.dirname(os.path.realpath(__file__))

        # Load the image securely by handling potential errors
        try:
            image_path = os.path.join(self.current_dir, "restart.jpg")  # Replace with your image name and format
            image = Image.open(image_path)
        except FileNotFoundError:
            print("Error: Splash image not found. Using a placeholder.")
            image = Image.new('RGB', (1280, 720), color='black')  # Placeholder image

        # Resize the image to fit within the window dimensions
        image.thumbnail((1280, 720))

        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()

        # Create the button first
        start_button = tk.Button(self, text="Click to Restart Game", command=self.start_game)
        start_button.pack(pady=20)  # Add padding below the button

        self.geometry("1400x800")

    def start_game(self):
        # Execute the bash script using os.system
        self.destroy()
        os.system(os.path.join(self.current_dir, "start.bash"))  # Secure path construction

# Create the splash screen instance with error handling
try:
    splash_screen = RestartScreen()
    splash_screen.mainloop()
except (ImportError, tk.TclError) as e:
    print("Error:", e)
    print("Failed to create splash screen. Exiting.")

        

# Example usage
def main():
    cwd = os.getcwd()
    sys.path.insert(0, cwd)
    executable_path = cwd  # Replace with your actual path
    splash_screen = RestartScreen(executable_path)
    splash_screen.mainloop()

if __name__ == '__main__':
    main()
