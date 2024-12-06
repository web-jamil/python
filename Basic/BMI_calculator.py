# BMI Calculator: Console-Based

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    """
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """
    Interpret BMI based on standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Input from user
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    # Output results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
except ValueError:
    print("Please enter valid numbers for weight and height.")





import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    """
    Calculate BMI and show results in a message box.
    """
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Interpret BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        # Show results
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Create main application window
app = tk.Tk()
app.title("BMI Calculator")

# Weight input
tk.Label(app, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(app)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Height input
tk.Label(app, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(app)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()
