##############PRACTICE##############

#FIRST AND SECOND PRACTICE 
#here we are going to add one of my fav. fruit
my_favorite_fruits = ["mango", "watermelon", "pineapple", "kiwi"]
my_favorite_fruits.append("orange")
print("adding_fav._fruit:", my_favorite_fruits)

#for removing the 3rd fruit we are using same list
my_favorite_fruits.pop(2)
print("removing_the_wrong_one:", my_favorite_fruits)


#THIRD AND FORTH PRACTICE
#creating two lists of numbers
x = [2,4,6,8,10]
y = [3,5,7,9,11]
#now concatenated both lists
final_list = x + y 
print("concatenated_list:", final_list)

#now we are using our final_list to multiple with 2
multiplied_by_2 = [num * 2 for num in final_list]
print("concatenated_multiplied_list:", multiplied_by_2)


#FIFTH AND SIXTH PRACTICE 
#in this one we will cover both we are making weekdays using tuple and extract the third day of the week.... which is monday
weekdayz = ("saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday")
third_day = weekdayz[2]
print("3rd_day_of_the_week_is:", third_day)


#SEVENTH PRACTICE
#we are making a list of people using tuple with their names and ages
person_data = ("Azam", 34), ("Victor", 24), ("Sebastián", 50)

# execute and print the data from the list of tuples
for person in person_data:
    name, age = person
    print("Name:", name, "| Age:", age)
#================CLOSED==================