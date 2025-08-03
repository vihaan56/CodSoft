import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)
    result = determine_winner(user_choice, comp_choice)

    user_choice_var.set(f"You chose: {user_choice}")
    comp_choice_var.set(f"Computer chose: {comp_choice}")
    result_var.set(result)

def determine_winner(user, comp):
    if user == comp:
        return "It's a Tie!"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
root.config(bg="lightblue")

user_choice_var = tk.StringVar()
comp_choice_var = tk.StringVar()
result_var = tk.StringVar()

tk.Label(root, text="Choose your move", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

# Buttons
for choice in choices:
    tk.Button(root, text=choice, width=10, font=("Arial", 12), command=lambda c=choice: play(c)).pack(pady=5)

# Disp
tk.Label(root, textvariable=user_choice_var, font=("Arial", 12), bg="lightblue").pack(pady=5)
tk.Label(root, textvariable=comp_choice_var, font=("Arial", 12), bg="lightblue").pack(pady=5)
tk.Label(root, textvariable=result_var, font=("Arial", 14, "bold"), fg="darkred", bg="lightblue").pack(pady=10)

root.mainloop()
