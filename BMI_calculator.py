import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100 # Convert the height in meters
        bmi = weight / (height ** 2)
        bmi_result_label.config(text = f"BMI: {bmi: .2f}")

        if bmi < 18.5:
            suggestion = "You are underweight. Try to gain some weight by consuming more calories."
        elif 18.5 <= bmi < 25:
            suggestion = "You are in healthy weight range. Keep up the good work!"
        elif 25 <= bmi < 30:
            suggestion = "You are overweight. Consider exercising more and eating healthier."
        else:
            suggestion = " You are obese. It's important to consult with a healthcare professional for guidance."

        suggestion_label.config(text = suggestion)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric values for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI calculator")

# Create labels
weight_label = tk.Label(root, text = "Weight (kg):")
weight_label.grid(row = 0, column = 0, padx = 10, pady = 5)
weight_entry = tk.Entry(root)
weight_entry.grid(row = 0, column = 1, padx = 10, pady = 5)

height_label = tk.Label(root, text = "Height (cm):")
height_label.grid(row = 1, column = 0, padx = 10, pady = 5)
height_entry = tk.Entry(root)
height_entry.grid(row = 1, column = 1, padx = 10, pady = 5)

calculate_button = tk.Button(root, text = "Calculate BMI", command = calculate_bmi)
calculate_button.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 5)

bmi_result_label = tk.Label(root, text = "")
bmi_result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

suggestion_label = tk.Label(root, text="")
suggestion_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()