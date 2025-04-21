import matplotlib.pyplot as plt

# Data storage (simulated as a dictionary)
health_data = {
    "steps": [5000, 6000, 5500, 7000],  # Daily steps
    "sleep": [6, 7, 6.5, 8],           # Hours of sleep
    "calories": [2000, 2200, 2100, 2300],  # Daily calories
    "water_intake": [6, 7, 5, 8]        # Glasses of water
}

# Goals
goals = {
    "steps": 10000,
    "sleep": 7,
    "calories": 2000,
    "water_intake": 8
}

# BMI and Calorie Calculator
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def calculate_calories(weight_kg, height_cm, age, gender, activity_level):
    # Simplified Harris-Benedict Equation
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    return bmr * activity_level  # Activity level: 1.2 (sedentary) to 1.9 (very active)

# Weekly Health Report
def generate_report():
    print("\nWeekly Health Report:")
    for metric, values in health_data.items():
        avg = sum(values) / len(values)
        goal = goals[metric]
        print(f"{metric.capitalize()}: Avg = {avg:.1f}, Goal = {goal}, Status = {'Met' if avg >= goal else 'Not Met'}")

# Hydration Reminder
def hydration_reminder(target_glasses):
    current = health_data["water_intake"][-1]
    if current < target_glasses:
        glasses_left = target_glasses - current
        print(f"\nHydration Reminder: Drink {glasses_left} more glasses of water today!")

# Graphical Health Progress
def plot_progress(metric):
    days = range(len(health_data[metric]))
    plt.plot(days, health_data[metric], label=metric.capitalize())
    plt.axhline(y=goals[metric], color='r', linestyle='--', label='Goal')
    plt.title(f"{metric.capitalize()} Progress")
    plt.xlabel("Days")
    plt.ylabel(metric.capitalize())
    plt.legend()
    plt.show()

# Main Program
if __name__ == "__main__":
    # Example usage
    print("Health & Fitness Tracker")
    
    # BMI Calculation
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI: {bmi:.1f}")

    # Calorie Calculation
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))
    age = int(input("Enter age: "))
    gender = input("Enter gender (male/female): ")
    activity = float(input("Enter activity level (1.2-1.9): "))
    calories_needed = calculate_calories(weight, height, age, gender, activity)
    print(f"Daily Calories Needed: {calories_needed:.0f}")

    # Generate Report
    generate_report()

    # Hydration Reminder
    hydration_reminder(goals["water_intake"])

    # Plot Progress (e.g., steps)
    plot_progress("steps")