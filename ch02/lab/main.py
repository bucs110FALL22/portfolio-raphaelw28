import random

#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))

cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))

classes_per_week = 5
print("Classes per week:", classes_per_week, type(classes_per_week))

cost_per_class = float(cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class, type(cost_per_class))

cost_per_class = str(cost_per_class)
print(cost_per_class + " is very expensive!")


#Part B
rand = ("dog", "cat", "fish", "frog", "bird")
print(random.choices(rand))