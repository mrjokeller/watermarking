import shutil
import tkinter as tk
from tkinter import filedialog, ttk
import os
from PIL import Image, ImageTk

class UI:
    
    def __init__(self, image_processor):
        self.image_processor = image_processor
        self.window = tk.Tk()
        self.window.title("Image Watermarking")
        self.window.geometry("300x300")
        self.window.resizable(False, False)
        
        self.watermark_text = tk.Entry(self.window)
        self.watermark_text.grid(row=1, column=2)
        
        self.button = tk.Button(self.window, text="Open Image", command=self.open_image)
        self.button.grid(row=0, column=1)
        
        self.button_wm = tk.Button(self.window, text="Set Watermark", command=self.image_processor.set_watermark, state=tk.DISABLED)
        self.button_wm.grid(row=0, column=2)
        
        self.panel = tk.Label(self.window, text=f"Image: {self.image_processor.has_image()}")
        self.panel.grid(row=1, column=1)
        self.window.mainloop()
        
    def open_image(self):
        file_name = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetypes=(("jpeg","*.jpg"),("png","*.png")))
        self.image_processor.set_image(file_name)
        self.image_processor.set_watermark_text(self.watermark_text.get())
        self.panel.configure(text=f"Image: {self.image_processor.has_image()}")
        self.button_wm.configure(state=tk.NORMAL)
    