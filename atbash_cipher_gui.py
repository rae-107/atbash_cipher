import tkinter as tk

class MyGUI:

  def __init__(self):
    self.window = tk.Tk()
    
    self.window.geometry('700x550')
    self.window.title("Atbash Cipher")

    self.window.mainloop()

MyGUI()