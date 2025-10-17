name = input("Enter name: ")
weight = int(input("Enter weight: "))
height = float(input("Enter height(e.g 1.75): "))
age = int(input("Enter age: "))
gender = input("Enter gender(M or F): ")
level = int(input("Enter the level(1-5): "))
starting_weight = int(input("Enter the starting weight(starting weight < weight): "))
goal_weight = float(input("Enter goal weight: "))
Weeks_since_started = int(input("Weeks since started: "))
Exercise_hours_per_week = int(input("Exercise hours per week: "))
current_BMI = weight / (height**2)
Goal_BMI = goal_weight / (height**2)

men = gender=="M"
men = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)

women = gender=="F"
women = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)

# Activity multipliers by level: 1.2, 1.375, 1.55, 1.725, 1.9 
multiplier = (level==1)*1.2 + (level==2)*1.375 + (level==3)*1.55 + (level==4)*1.725 + (level==5)*1.9

TDEE =  men* multiplier
TDEE =  women* multiplier

Weight_lost = starting_weight - weight
Average_weekly_loss = Weight_lost / Weeks_since_started

Remaining_weight = weight - goal_weight

Weeks_to_goal = Remaining_weight / Average_weekly_loss
Underweight = current_BMI < 18.5
Normal = current_BMI >= 18.5 and current_BMI < 25
Overweight = current_BMI >= 25 and current_BMI < 30
Obese = current_BMI >= 30
Goal_underweight =  Goal_BMI < 18.5
Goal_normal =  Goal_BMI >= 18.5  and Goal_BMI < 25
Goal_overweight = Goal_BMI >= 25 and Goal_BMI < 30
Goal_obese =  Goal_BMI >= 30
Goal_is_healthy =  Goal_BMI >= 18.5 and  Goal_BMI < 25
Progress_rate_healthy =  Average_weekly_loss >= 0.5 and Average_weekly_loss <= 1.0 
Exercise_sufficient = Exercise_hours_per_week >= 3
Overall_on_track =  Progress_rate_healthy and Exercise_sufficient

print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Height: {height}")

print(f"Starting weight: {starting_weight}")
print(f"Current weight: {weight}")
print(f"Goal weight: {goal_weight}")

print(f"Weight lost so far: {Weight_lost}")
print(f"Remaining to goal: {Remaining_weight}")

print(f"Current BMI:")
print(f"1: {Underweight}")
print(f"2: {Normal}")
print(f"3: {Overweight}")
print(f"4: {Obese}")

print(f"Goal BMI:")
print(f"1: {Goal_underweight}")
print(f"2: {Goal_normal}")
print(f"3: {Goal_overweight}")
print(f"4: {Goal_obese}")

print(f"BMR: {men or women} (calories/day)")
print(f"Activity level and multiplier: {multiplier}")
print(f"TDEE: {TDEE}(calories/day)")

print(f"Weeks since started: {Weeks_since_started}")
print(f"Average weekly loss: {Average_weekly_loss}")
print(f"Exercise hours per week: {Exercise_hours_per_week}")
print(f"Estimated weeks to goal: {Weeks_to_goal}")

print(f"Underweight: {Underweight}")
print(f"Normal: {Normal}")
print(f"Overweight: {Overweight}")
print(f"Obese: {Obese}")
print(f"Goal underweight: {Goal_underweight}")
print(f"Goal normal: {Goal_normal}")
print(f"Goal overweight: {Goal_overweight:.2f}")
print(f"Goal obese : {Goal_obese}")
print(f"Goal is healthy: {Goal_is_healthy}")
print(f"Progress rate healthy: {Progress_rate_healthy}")
print(f"Exercise sufficient: {Exercise_sufficient}")
print(f"Overall on track: {Overall_on_track}")








