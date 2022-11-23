from tkinter import *
import pandas as pd
import random

# ---------- Start Datas ----------

data = pd.read_csv("data/words.csv")
all_word = data.to_dict(orient="records")
# selected_word = random.choice(all_word)
selected_word = {}
learned_words = []
saved_words = []
flip_timer = None

# ---------- Flip card ----------
def flip_card():
    global flip_timer
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=selected_word["English"])
    window.after_cancel(flip_timer)
    

# ---------- Next card ----------
def next_card():
    global selected_word
    if len(selected_word) == 0:
        selected_word = random.choice(all_word)
        canvas.itemconfig(title_text, text="Germany")
        canvas.itemconfig(word_text, text=selected_word["Germany"])
        flip_timer = window.after(3000, flip_card)
    elif len(all_word) > 0:
        learned_words.append(selected_word)
        all_word.remove(selected_word)
        print(learned_words)
        print(all_word)
        if len(all_word) != 0:
            selected_word = random.choice(all_word)
            canvas.itemconfig(title_text, text="Germany")
            canvas.itemconfig(word_text, text=selected_word["Germany"])
            flip_timer = window.after(3000, flip_card)
    else:
        canvas.itemconfig(title_text, text="No more")
        canvas.itemconfig(word_text, text="card!")
        try:
            window.after_cancel(flip_timer)
        except:
            canvas.itemconfig(title_text, text="No more")
            canvas.itemconfig(word_text, text="card!")

# ---------- Save card ----------
def save_card():
    global selected_word
    if len(all_word) >= 1:
        saved_words.append(selected_word)
        all_word.remove(selected_word)
        print(saved_words)
        if len(all_word) != 0:
            selected_word = random.choice(all_word)
            canvas.itemconfig(title_text, text="Germany")
            canvas.itemconfig(word_text, text=selected_word["Germany"])
            flip_timer = window.after(3000, flip_card)
    else:
        canvas.itemconfig(title_text, text="No more")
        canvas.itemconfig(word_text, text="card!")
        try:
            window.after_cancel(flip_timer)
        except:
            canvas.itemconfig(title_text, text="No more")
            canvas.itemconfig(word_text, text="card!")

# ---------- UI ----------
window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg="lightyellow", highlightthickness=0)
# flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=300, height=200, bg="lightyellow", highlightthickness=0)
title_text = canvas.create_text(150, 50, text="Press the green", font=("Ariel", 26, "italic"))
word_text = canvas.create_text(150, 125, text="button", font=("Ariel", 36, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

accept_img = PhotoImage(file="pics/accept.png")
accept_btn = Button(image=accept_img, bg="lightyellow", highlightthickness=0, activebackground="lightyellow", command=next_card)
accept_btn.grid(row=1, column=0)

decide_img = PhotoImage(file="pics/wrong.png")
decide_btn = Button(image=decide_img, bg="lightyellow", highlightthickness=0, activebackground="lightyellow", command=save_card)
decide_btn.grid(row=1, column=1)


window.mainloop()
