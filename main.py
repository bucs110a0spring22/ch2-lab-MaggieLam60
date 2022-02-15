import random
#Part A
weeks = 16
print(weeks,type(weeks))
classes = 5
print(classes,type(classes))
tuition = 6000
print(tuition,type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
print(cost_per_week,type(cost_per_week))
class_per_week=3
print(class_per_week,type(class_per_week))
cost_per_class=(cost_per_week/class_per_week)
print(cost_per_class,type(cost_per_class))
print("Your cost per class is " + str(cost_per_class))



#Part B
random.randrange (0,4)
my_list=[10,20,30,40,50]
print(random.choice(my_list))