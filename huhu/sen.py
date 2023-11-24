import customtkinter as ctk
from tkinter import PhotoImage, Label, Text, Canvas, ttk
import tkinter as tk


# Create the main window
app = ctk.CTk()
app.title('My Fruit Shop')
app.geometry("750x600")
app.config(bg="#FFA5B8")
app.resizable(False, False)

# Fonts
font1 = ('Franklin Gothic Book', 20, 'bold')
font2 = ('Franklin Gothic Book', 15, 'bold')
font3 = ('Franklin Gothic Book', 17, 'italic', 'bold')
font5 = ('Plantagenet Cherokee', 30, 'italic', 'bold')

# Load and subsample the image
image1 = PhotoImage(file='C:/Users/admin/OneDrive/Documents/Melissa/My Fruit Shop/Seller.png').subsample(1,1 )
image2 = PhotoImage(file='C:/Users/admin/OneDrive/Documents/Melissa/My Fruit Shop/bubble.png').subsample(1,2 )
image3 = PhotoImage(file='C:/Users/admin/OneDrive/Documents/Melissa/My Fruit Shop/bubble1.png').subsample(1,2 )

image1_label = Label(app, image=image1, fg="#FFA5B8", bg="#FFA5B8", compound="top", anchor="n", width=450, height=570)
image1_label.place(x=10, y=70)

image2_label = Label(app, image=image2, fg="#FFA5B8", bg="#FFA5B8", compound="top", anchor="n", width=480, height=220)
image2_label.place(x=450, y=220)

image3_label = Label(app, image=image3, fg="#FFA5B8", bg="#FFA5B8", compound="top", anchor="n", width=480, height=220)
image3_label.place(x=450, y=5)

label_price = Label(app, text="Buy Apples. For only\n                 Php", bg='#FDFCDC', font=font3)
label_price.place(x=590,y=100)


title_frame = ctk.CTkFrame(app, width=360, height=50, fg_color="#AD6E8C", bg_color="#FFA5B8", corner_radius=50)
title_frame.place(x=10, y=8)

label_title = ctk.CTkLabel(app, text="Mishy Freshie Fruities", bg_color='#AD6E8C', text_color='#403F3F', font=font5)
label_title.place(x=30, y=15)

label_price2 = Label(app, text="How much money do you have?\n              Php", bg='#FDFCDC', font=font3)
label_price2.place(x=540,y=320)

quantity1_entry = ctk.CTkEntry(app, font=font1, text_color="#000000", bg_color="#FDFCDC", fg_color="#FFFFFF", width=80)
quantity1_entry.place(x=510, y=105)

quantity2_entry = ctk.CTkEntry(app, font=font1, text_color="#000000", bg_color="#FDFCDC", fg_color="#FFFFFF", width=80)
quantity2_entry.place(x=510, y=280)

message_frame = ctk.CTkFrame(app, width=320, height=150, fg_color="#AD6E8C", bg_color="#FFA5B8", corner_radius=30)
message_frame.place(x=400, y=400)
message_frame.pack_propagate(False)  # Fix the size of the frame

result_label = Label(message_frame, text="", font=font3, bg='#AD6E8C', fg='#FFFFFF')
result_label.pack(pady=20)


def pay():
    try:
        User_apple = int(quantity1_entry.get())
        User_money = int(quantity2_entry.get())

        if User_money < User_apple:
            result_label.config(text="\nUnfortunately,\n you can't buy any apple at my shop \nwith that amount of money.")
        elif User_money == User_apple:
            result_label.config(text="\nPerfect! You have the exact change \nfor one apple. Enjoy your purchase!")
        elif User_money == 0:
            result_label.config(text="\nLooks like you're out of money. \nTime to save up for more apples!")
        elif User_money % User_apple == 0:
            num_apples = User_money // User_apple
            result_label.config(text=f"\nYou can buy exactly \n{num_apples} apple/s with your money! \nEnjoy your apples!")
        else:
            max_apple = User_money // User_apple
            remaining_money = User_money % User_apple
            result_label.config(text=f"\nYou can buy up to {max_apple} apple/s \nwith your money. You'll have \n{remaining_money} Php left for a sweet treat.")

    except ValueError:
        result_label.config(text="\nPlease enter valid numeric \nvalues for Apples and Money.")


pay_button = ctk.CTkButton(app, command=pay, text="Pay", font=font1, fg_color="#ad0c78", bg_color="#FFA5B8", hover_color="#D4A0CB", corner_radius=20, cursor="hand2", width=130)
pay_button.place(x=495, y=350)


app.mainloop()
