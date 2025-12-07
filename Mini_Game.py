import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Mini Fun Space Adventure 🚀💖")
root.geometry("600x400")

story = [
    "You wake up on a sparkly spaceship filled with glitter...",
    "A talking cat in a tiny spacesuit jumps on your shoulder.",
    "The cat asks: 'Do you want to join my dance party on Mars?'"
]

choices = [
    ["Yes, let's dance! 💃", "No, I want coffee first ☕"],
    ["Follow the cat 🐱", "Hide behind a glitter pillow ✨"]
]

current_scene = 0

def next_scene(choice=None):
    global current_scene
    if current_scene < len(story):
        text_label.config(text=story[current_scene])
        if current_scene < len(choices):
            button1.config(text=choices[current_scene][0])
            button2.config(text=choices[current_scene][1])
        else:
            button1.pack_forget()
            button2.pack_forget()
            # فان ترین پایان
            endings = [
                "You danced so much that you floated to the moon! 🌙💃",
                "The cat stole your socks and became the new ruler of Mars! 🐱👑",
                "You drank the coffee and suddenly grew rainbow wings! 🌈🪽"
            ]
            import random
            messagebox.showinfo("The End 😎", random.choice(endings))
        current_scene += 1

text_label = tk.Label(root, text="", font=("Comic Sans MS", 16), wraplength=500)
text_label.pack(pady=50)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

button1 = tk.Button(button_frame, text="", width=25, command=lambda: next_scene(0), bg="#ff69b4")
button1.pack(side="left", padx=10)

button2 = tk.Button(button_frame, text="", width=25, command=lambda: next_scene(1), bg="#ffb6c1")
button2.pack(side="left", padx=10)

next_scene()

root.mainloop()
