import tkinter as tk

def calculate_prices():
    User_apple = apple_var.get()
    User_orange = orange_var.get()

    Total_apple_price = User_apple * apple_price
    Total_orange_price = User_orange * orange_price
    Total_overall_price = Total_apple_price + Total_orange_price

    result_label.config(text=f"The total price of {User_apple} apple(s) is {Total_apple_price} Pesos\n"
                             f"The total price of {User_orange} orange(s) is {Total_orange_price} Pesos\n"
                             f"The total price of apple and orange is {Total_overall_price} Pesos")

def add_apple():
    apple_var.set(apple_var.get() + 1)

def add_orange():
    orange_var.set(orange_var.get() + 1)

# Prices
apple_price = 20
orange_price = 25

# Tkinter setup
root = tk.Tk()
root.geometry("800x500")
root.title("Welcome to my fruit shop")

# Labels and OptionMenus
label = tk.Label(root, text="How many fruits are you going to buy?", font=('Arial', 20))
label.pack(padx=50, pady=10)

apple_label = tk.Label(root, text="Apples:")
apple_label.pack()
apple_var = tk.IntVar()
apple_var.set(0)  # Default value
apple_menu = tk.OptionMenu(root, apple_var, *range(11))
apple_menu.pack()

orange_label = tk.Label(root, text="Oranges:")
orange_label.pack()
orange_var = tk.IntVar()
orange_var.set(0)  # Default value
orange_menu = tk.OptionMenu(root, orange_var, *range(11))
orange_menu.pack()

# Buttons to add one at a time
apple_button = tk.Button(root, text="Add Apple", command=add_apple)
apple_button.pack(pady=5)

orange_button = tk.Button(root, text="Add Orange", command=add_orange)
orange_button.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Prices", command=calculate_prices)
calculate_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=('Arial', 16))
result_label.pack()

# Run Tkinter main loop
root.mainloop()
