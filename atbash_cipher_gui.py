import tkinter as tk

class MyGUI:

  def __init__(self):
    self.window = tk.Tk()

    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
    self.capital_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    self.window.geometry('700x550')
    self.window.title("Atbash Cipher")

    self.welcome = tk.Label(self.window, text='Welcome', font=('Arial', 34))
    self.welcome.pack(pady=20)

    self.get_started = tk.Label(self.window, text='Get Started By Typing In A Message', font=('Arial', 18))
    self.get_started.pack()  

    self.message = tk.StringVar()

    self.user_input = tk.Entry(self.window, font=('Arial', 20), textvariable=self.message)
    self.user_input.pack(pady=20)

    self.buttonframe = tk.Frame(self.window)
    self.buttonframe.columnconfigure(0, weight=1)
    self.buttonframe.columnconfigure(1, weight=1)

    self.encode_button = tk.Button(self.buttonframe, text='Encode Message', font=('Arial', 14),command=self.encode_handler)
    self.encode_button.grid(row=0, column=0)

    self.decode_button = tk.Button(self.buttonframe, text='Decode Message', font=('Arial', 14), command=self.decode_handler)
    self.decode_button.grid(row=0, column=1)

    self.buttonframe.pack()

    self.original_message_label = tk.Label(self.window, font=('Arial', 14))
    self.original_message_label.pack()

    self.original_message = tk.Label(self.window, font=('Arial', 18))
    self.original_message.pack(pady=10)

    self.output_label = tk.Label(self.window, font=('Arial', 14))
    self.output_label.pack()

    self.output = tk.Label(self.window, font=('Arial', 18))
    self.output.pack(pady=10)

    self.window.mainloop()

  def encode_message(self, phrase):
    encoded_message = ''
    for char in phrase: 
      if char in self.alphabet:
        alphabet_index = self.alphabet.find(char)
        encoded_message += self.alphabet[(-alphabet_index - 1)]
      elif char in self.capital_alphabet:
        capital_index = self.capital_alphabet.find(char)
        encoded_message += self.capital_alphabet[(-capital_index - 1)]
      else:
        encoded_message += char
    return encoded_message

  def decode_message(self, phrase):
    decoded_message = ''
    for char in phrase:
      if char in self.alphabet:
        alphabet_index = self.alphabet.find(char)
        decoded_message += self.alphabet[(-alphabet_index - 1)]
      elif char in self.capital_alphabet:
        capital_index = self.capital_alphabet.find(char)
        decoded_message += self.capital_alphabet[(-capital_index - 1)]
      else:
        decoded_message += char
    return decoded_message

MyGUI()