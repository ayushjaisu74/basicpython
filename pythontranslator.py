import tkinter as tk
from deep_translator import GoogleTranslator

def translate_text():
    text = entry.get()

    if text == "":
        result_label.config(text="Please enter a word")
    else:
        try:
            translated = GoogleTranslator(source='en', target='hi').translate(text)
            result_label.config(text=translated)
        except:
            result_label.config(text="Translation Error")

root = tk.Tk()
root.title("English to Hindi Translator")
root.geometry("400x250")

title = tk.Label(root, text="English to Hindi Translator", font=("Arial",16,"bold"))
title.pack(pady=10)

label = tk.Label(root, text="Enter English Word:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Translate", command=translate_text)
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial",14), fg="blue")
result_label.pack(pady=10)

root.mainloop()