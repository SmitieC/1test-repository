BIKE = 200
JOG = 475
SWIM = 275
# all in hours
weight_lost = 454 / 3500 # mg / calories

bike_hours = int(input("How many hours did you bike? "))
jog_hours = int(input("How many hours did you jog? "))
swim_hours = int(input("How many hours did you swim? "))

total_calories = bike_hours * BIKE + JOG * jog_hours + SWIM * swim_hours
# add them all together

print("you lost", round(total_calories * weight_lost / 1000, 2), "kg")
#divide by 1000 to get kg and round to 2 decimal places
