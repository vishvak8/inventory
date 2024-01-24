import tkinter as tk
from tkinter import messagebox

def calculate_cost(athlete):
    cost_of_training_plan = {
        "Beginner": 25.00,
        "Intermediate": 30.00,
        "Elite": 35.00,
        "Private": 0.00  # Private coaching is handled separately
    }

    competition_entry_fee = 22.00
    private_coaching_hourly_rate = 9.50

    # Calculate training cost
    cost_for_training = cost_of_training_plan.get(athlete["training_plan"], 0.00)

    # Calculate private coaching cost
    coaching_cost = athlete["private_coaching_hours"] * private_coaching_hourly_rate

    # Calculate competition cost (only for Intermediate and Elite athletes)
    if athlete["training_plan"] in ["Intermediate", "Elite"]:
        competition_cost = athlete["competitions_entered"] * competition_entry_fee
    else:
        competition_cost = 0.00

    # Calculate total cost
    total_cost = cost_for_training + coaching_cost + competition_cost

    return {
        "Training Cost": cost_for_training,
        "Coaching Cost": coaching_cost,
        "Competition Cost": competition_cost,
        "Total Cost": total_cost
    }

def comparison_of_display(athlete):
    weight_difference = athlete["current_weight"] - athlete["competition_weight"]

    if weight_difference < 0:
        return f"{athlete['name']} is underweight for their competition category by {-weight_difference} kg."
    elif weight_difference > 0:
        return f"{athlete['name']} is overweight for their competition category by {weight_difference} kg."
    else:
        return f"{athlete['name']}'s weight is within the competition category."

def process_data():
    try:
        athlete_data = {
            "name": name_entry.get(),
            "training_plan": training_plan_var.get(),
            "current_weight": float(current_weight_entry.get()),
            "competition_weight": float(competition_weight_entry.get()),
            "competitions_entered": int(competitions_entered_entry.get()),
            "private_coaching_hours": int(private_coaching_hours_entry.get())
        }

        result_label.config(text=f"{comparison_of_display(athlete_data)}\n\nCost Summary for {athlete_data['name']}:\n{calculate_cost(athlete_data)}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

# Create Tkinter window
window = tk.Tk()
window.title("Athlete Information and Cost Calculator")

# Create and pack widgets
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

training_plan_label = tk.Label(window, text="Training Plan:")
training_plan_label.grid(row=1, column=0)

training_plan_var = tk.StringVar()
training_plan_var.set("Beginner")  # Default value

training_plan_options = ["Beginner", "Intermediate", "Elite", "Private"]
training_plan_menu = tk.OptionMenu(window, training_plan_var, *training_plan_options)
training_plan_menu.grid(row=1, column=1)

current_weight_label = tk.Label(window, text="Current Weight (kg):")
current_weight_label.grid(row=2, column=0)

current_weight_entry = tk.Entry(window)
current_weight_entry.grid(row=2, column=1)

competition_weight_label = tk.Label(window, text="Competition Weight (kg):")
competition_weight_label.grid(row=3, column=0)

competition_weight_entry = tk.Entry(window)
competition_weight_entry.grid(row=3, column=1)

competitions_entered_label = tk.Label(window, text="Competitions Entered:")
competitions_entered_label.grid(row=4, column=0)

competitions_entered_entry = tk.Entry(window)
competitions_entered_entry.grid(row=4, column=1)

private_coaching_hours_label = tk.Label(window, text="Private Coaching Hours:")
private_coaching_hours_label.grid(row=5, column=0)

private_coaching_hours_entry = tk.Entry(window)
private_coaching_hours_entry.grid(row=5, column=1)

calculate_button = tk.Button(window, text="Calculate", command=process_data)
calculate_button.grid(row=6, column=0, columnspan=2)

result_label = tk.Label(window, text="")
result_label.grid(row=7, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()                                            