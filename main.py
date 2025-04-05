#create a basic type of 
import tkinter as tk
import threading
from PIL import Image, ImageTk, ImageDraw, ImageFilter, ImageFont
from tkinter import ttk, messagebox


class HealthChecker:
    def __init__(self, root):
        # Create Tk
        self.root = root
        self.root.title("Health Reminder")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Call the background method to set up the UI
        self.setup_background()
    
    def setup_background(self):
        # Load or create background image
        bg_image = Image.new('RGB', (400, 500), color="#f5f6fa")  # Simple color background
        # Or load an image file:
        # bg_image = Image.open("your_background.png")
        
        # Convert to PhotoImage
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        # Create canvas
        canvas = tk.Canvas(self.root, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Add background image
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # This goes brr when it creates need add things
        #also why this has more odd way set up
        main_frame = tk.Frame(canvas, bg="#ffffff", bd=0)
        main_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        label = tk.Label(main_frame, text="Health Reminder", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = HealthChecker(root)
    root.mainloop()