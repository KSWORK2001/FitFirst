import math

def calculate_bmi(height, weight):
    """Calculates the body mass index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

def calculate_bfp(height, weight, sex):
    """Calculates the body fat percentage (BFP)."""
    # Calculate the body mass index (BMI)
    bmi = calculate_bmi(height, weight)

    # Calculate the body fat percentage (BFP) for men
    if sex == "male":
        bfp = (4.95 * bmi) + 4.5

    # Calculate the body fat percentage (BFP) for women
    elif sex == "female":
        bfp = (4.95 * bmi) + 4.15

    return bfp

def calories_burned(height, weight, activity_level):
    # Calculate the basal metabolic rate (BMR)
    bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

    # Calculate the calories burned per day based on the activity level
    if activity_level == "Sedentary":
        calories_burned = bmr * 1.2
    elif activity_level == "Lightly Active":
        calories_burned = bmr * 1.4
    elif activity_level == "Moderately Active":
        calories_burned = bmr * 1.6
    elif activity_level == "Very Active":
        calories_burned = bmr * 1.8
    elif activity_level == "Extremely Active":
        calories_burned = bmr * 2.0

    return calories_burned

def calories_to_eat(current_weight, desired_weight, time_to_achieve_desired_weight):
    # Calculate the number of calories to eat per day to lose 1 pound per week
    calories_to_eat_per_day = 3500 / time_to_achieve_desired_weight

    # Calculate the number of calories to eat per day to lose weight from current weight to desired weight
    calories_to_eat = calories_to_eat_per_day * (desired_weight - current_weight)

    return calories_to_eat

# Get the user's height, weight, water intake, desired weight, and the time to achieve the desired weight
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
water_intake = float(input("Enter your daily water intake in ounces: "))
desired_weight = float(input("Enter your desired weight in pounds: "))
time_to_achieve_desired_weight = int(input("Enter the number of weeks to achieve your desired weight: "))

# Calculate the number of calories to eat per day to lose weight
calories_to_eat = calories_to_eat(weight, desired_weight, time_to_achieve_desired_weight)

# Print the number of calories to eat per day to lose weight
print("You need to eat {} calories per day to lose weight.".format(calories_to_eat))

# Print the number of ounces of water to drink per day
water_to_drink = water_intake * 28.3495
print("You need to drink {} ounces of water per day.".format(water_to_drink))

# Get the user's height, weight, and sex
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
sex = input("Enter your sex (male/female): ")

# Calculate BMI and BFP
bmi = calculate_bmi(height, weight)
bfp = calculate_bfp(height, weight, sex)

# Print BMI and BFP
print("Your BMI is {}.".format(bmi))
print("Your BFP is {}.".format(bfp))

# Check if the user is obese
if bmi >= 30:
    # Suggest
print("Unfortunately, we have discovered that you fall in the obese category. Obesity is no joke and can be lethal in the long run if left unchecked so we are here to help and suggest some activities:")
print("| Categories |          Lose Fat             |   Lose Fat and Gain Muslce  |           Gain Muslce         |    Gain Fat and Gain Muscle    |     Maintain Muslce and Fat   |")
print("|   Obese    | Cardio 96 mins and WR 24 mins |Cardio 42 mins and WR 78 mins|               NS              |               NS               |             NS                |")
print("| Overweight | Cardio 96 mins and WR 24 mins |Cardio 42 mins and WR 78 mins|               NS              |               NS               |             NS                |")
print("|   Normal   |              NS               |              NS             | Cardio 24 mins and WR 96 mins |               NS               | Cardio 60 mins and WR 60 mins |")
print("|Underweight |              NS               |              NS             |               NS              | Cardio 12 mins and WR 108 mins |             NS                |")
print()
print("WR* = Weight/Resistance Training")