import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

def random_color():
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def start_survey():
    ready_confirmation = messagebox.askquestion("Ready to Sail?", "Yo, ready to join the crew?, or you gonna miss out?")

    start_button.pack_forget()
    start_output_label.pack_forget()

    if ready_confirmation == "yes":
        survey_frame.pack()
    else:
        info_label.config(text="You're missing out, but no pressure! Come back when you're ready to sail.  ⛵😎", fg=random_color(), font=("Segoe UI", 14))

def show_user_info():
    user_name = name_entry.get()
    user_age = age_entry.get()
    user_address = address_entry.get()

    color = random_color()

    confirmation = messagebox.askquestion("Confirmation", "Is this information correct?")

    if confirmation == "yes":
        output_text = "Congrats, you're officially part of the crew! Welcome to the Strawhats!"

        final_output_text = f"\n Welcome nakama! \nHey there, {user_name}! You've mastered {user_age} years of awesomeness.\nLiving it up at {user_address}, right? Nice choice, nakama! "

        final_info_label.config(text=final_output_text, fg=color, font=("Segoe UI", 16))

        change_color_button.pack()
        reset_survey_button.pack()

        survey_frame.pack_forget()
    else:
        output_text = "Whoops! Try again and drop the real 411, friend. You got this! "
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        final_info_label.config(text="", font=("Segoe UI", 12))

    info_label.config(text=output_text, fg=color, font=("Segoe UI", 14))

def change_output_color():
    final_info_label.config(fg=random_color())

def reset_survey():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    final_info_label.config(text="", font=("Segoe UI", 12))
    info_label.config(text="", font=("Segoe UI", 14))
    change_color_button.pack_forget()
    reset_survey_button.pack_forget()
    start_button.pack()

# Create the main window
window = tk.Tk()
window.title("User Information")

# Size of the window
window.attributes("-fullscreen", True)

# Open the image with Pillow
original_image = Image.open("C:/Users/admin/OneDrive/Documents/Melissa/PLD/onepiece.png")

# Convert the Pillow image to a Tkinter-compatible format
tk_image = ImageTk.PhotoImage(original_image)

# Use tk_image as the background image of the window
bg_label = tk.Label(window, image=tk_image)
bg_label.place(relwidth=1, relheight=1)

# Start Survey Frame
survey_frame = tk.Frame(window, bg='white')

# Create and place labels and entry widgets in the survey frame
tk.Label(survey_frame, text="Yo, what's your name? ", font=("Segoe UI", 14)).pack()
name_entry = tk.Entry(survey_frame)
name_entry.pack()

tk.Label(survey_frame, text="How many times have you leveled up in this game of life? ", font=("Segoe UI", 14)).pack()
age_entry = tk.Entry(survey_frame)
age_entry.pack()

tk.Label(survey_frame, text="What's your spot on the map? ", font=("Segoe UI", 14)).pack()
address_entry = tk.Entry(survey_frame)
address_entry.pack()

tk.Button(survey_frame, text="Show Information", command=show_user_info, font=("Segoe UI", 14)).pack()

# End Survey Frame

start_button = tk.Button(window, text="Start", command=start_survey, font=("Segoe UI", 16))
start_button.pack()

info_label = tk.Label(window, text="", font=("Segoe UI", 14))
info_label.pack()

start_output_label = tk.Label(window, text="", font=("Segoe UI", 14))
start_output_label.pack()

final_info_label = tk.Label(window, text="", font=("Segoe UI", 16))
final_info_label.pack()

change_color_button = tk.Button(window, text="Click me", command=change_output_color, font=("Segoe UI", 14))
reset_survey_button = tk.Button(window, text="Reset Survey", command=reset_survey, font=("Segoe UI", 14))

window.mainloop()