import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class SplashScreen(tk.Tk):
    def __init__(self, image_url):
        super().__init__()
        self.title("Laser Tag")
        self.geometry("1280x720")
        self.configure(background="black")

        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))

        # Resize the image to fit within the window dimensions
        image.thumbnail((1280, 720))

        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_offset = (screen_width - 1280) // 2
        y_offset = (screen_height - 720) // 2
        self.geometry(f"+{x_offset}+{y_offset}")

        self.after(3000, self.destroy)  # Close splash screen after 5 seconds

# Example usage
if __name__ == "__main__":
    splash_image_url = "https://raw.githubusercontent.com/jstrother123/photon-main/main/logo.jpg"
    splash_screen = SplashScreen(splash_image_url)
    splash_screen.mainloop()
