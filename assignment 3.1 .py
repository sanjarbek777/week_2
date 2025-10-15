name ="sanjarbek"
weight = 85
# float(input("enter weight") )
height =1.75
# float(input("enter height"))
age = 18 
gender = "F"
level = 1
starting_weight = 85 
goal_weight = float(input("enter gw"))
Weeks_since_started = 2
Exercise_hours_per_week = 2
current_BMI = weight / (height ** 2)
Goal_BMI = goal_weight / (height ** 2)

men = gender=="M"
men = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)

women = gender=="F"
women = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)

multiplier = (level==1)*1.2 + (level==2)*1.375 + ...

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






