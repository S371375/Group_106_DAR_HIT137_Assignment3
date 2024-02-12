#https://github.com/S371375/Group_106_DAR_HIT137_Assignment3
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("English to Nepali Language Translation App")
        self.geometry("400x200")

        self.translator = Translator()

        self.input_label = ttk.Label(self, text="Enter Text:")
        self.input_label.pack()

        self.input_entry = ttk.Entry(self)
        self.input_entry.pack()

        self.translate_button = ttk.Button(self, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.output_label = ttk.Label(self, text="Translation:")
        self.output_label.pack()

        self.output_text = tk.StringVar()
        self.output_entry = ttk.Entry(self, textvariable=self.output_text, state='readonly')
        self.output_entry.pack()

    def translate_text(self):
        input_text = self.input_entry.get()
        translated_text = self.translator.translate(input_text, dest='ne').text  # Translate to Nepali
        self.output_text.set(translated_text)

if __name__ == "__main__":
    app = LanguageTranslationApp()
    app.mainloop()
