# Personal Fitness Tracker
#
# Test results:
# Low: 180 calories, 45 minutes -> 4.0 cal/min -> Low
# Moderate: 300 calories, 40 minutes -> 7.5 cal/min -> Moderate
# High: 320 calories, 30 minutes -> 10.7 cal/min -> High
# Boundary 5.0: 250 calories, 50 minutes -> 5.0 cal/min -> Moderate
# Boundary 10.0: 200 calories, 20 minutes -> 10.0 cal/min -> High


# Calculate calories burned per minute
def calories_per_minute(calories, duration):
    return round(calories / duration, 1)


# Determine workout intensity
def get_intensity(rate):
    if rate < 5.0:
        return "Low"
    elif rate < 10.0:
        return "Moderate"
    else:
        return "High"


# Greet the user
print("Welcome to the Personal Fitness Tracker!")
print("You will log 3 workouts.")

# Store workout data
workouts = []

# Collect exactly 3 workouts
for i in range(3):
    print(f"\n--- Workout {i + 1} ---")

    workout_name = input("Workout name: ")
    duration = float(input("Duration (minutes): "))
    calories_burned = float(input("Calories burned: "))

    # Store all three values for this workout in a list
    workout = [workout_name, duration, calories_burned]
    workouts.append(workout)

    # Calculate rate and intensity
    rate = calories_per_minute(calories_burned, duration)
    intensity = get_intensity(rate)

    # Display workout result
    print(
        f"Result: {workout_name} | "
        f"{duration:g} min | "
        f"{calories_burned:g} cal | "
        f"{rate:.1f} cal/min | "
        f"Intensity: {intensity}"
    )

# Closing message
print("\nAll workouts logged. Great job staying active!")