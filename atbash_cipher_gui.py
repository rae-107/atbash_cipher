import tkinter as tk

class AtbashCipherGUI:
  def __init__(self):
    self.window = tk.Tk()
    self.window.geometry('700x550')
    self.window.title("Atbash Cipher")

    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
    self.capital_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
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


AtbashCipherGUI()