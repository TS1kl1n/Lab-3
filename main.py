import tkinter as tk
import random
from PIL import Image, ImageTk

def generate_key(input_word):
    letters_part = input_word[:3].upper()
    numbers_part = ''.join(str(ord(char) - 64) for char in letters_part)
    numbers_part = ''.join(num.lstrip('0') for num in numbers_part)  

    
    generated_key = f"{letters_part}-{numbers_part}-{letters_part}"
    return generated_key


root = tk.Tk()
root.title("Keygen")

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(row=0, column=0, columnspan=2)


background_img = Image.open("chess_bg.jpg")
background_img = background_img.resize((400, 300)) 
background_img = ImageTk.PhotoImage(background_img)
canvas.create_image(0, 0, anchor="nw", image=background_img)

input_word_entry = tk.Entry(root)
input_word_label = tk.Label(root, text="Введите 6-ти буквенное слово:")
generate_key_button = tk.Button(root, text="Генерировать ключ")
generated_key_label = tk.Label(root, text="Сгенерированный ключ:")


input_word_label.grid(row=0, column=0)
input_word_entry.grid(row=0, column=1)
generate_key_button.grid(row=1, column=0, columnspan=2)
generated_key_label.grid(row=2, column=0, columnspan=2)


def on_generate_key_button_click():
    input_word = input_word_entry.get()
    generated_key = generate_key(input_word)
    generated_key_label.config(text="Generated Key: " + generated_key)


generate_key_button.config(command=on_generate_key_button_click)

root.mainloop()
