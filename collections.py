# Data Collections
## Lists, Tuples & Dict

#### Lists
# What are lists?
# correct syntax []
# lists are mutable
# indexing same concept allies

#shopping_list = ["bat", "milk", "bread"]
#               #   0       1        2
# print(shopping_list)
# # find out the type of shopping list
# # find out the len of shopping list
#
# # how to add to our shopping list
# shopping_list.append("oreos ") # append() adds an item at the end of the list
#
#print(shopping_list)
#
# # how to delete an item from our shopping list
#shopping_list.remove("bat")
# print(shopping_list)

# find out out to replace an item from the list and replace bat with "milk"
#
#mixed_list = [1, 2, 3, "one ", "two", "three", ""]
# #             0  1  2    3       4       5
# #print(mixed_list)
#
# # print 2 & 3 from the above list
# print(mixed_list[1]) # outcome would be 3
# print(mixed_list[2]) # outcome would be 3
# print(mixed_list[1:3]) # outcome would be 2, 3


# Tuple
# Why do we need Tuple?
# Lists [] are mutable VS Tuples() are immutable
# syntax for tuple ()
# what are the use cases?
# essential = ("city", "DOB", "place of birth")
#              #  0       1       2
#
# print(essential)
# print(type(essential))
# print(essential[1])
# # essential[0] = "town" # IMMUTABLE
# print(essential) # What would be the outcome: error

# essential ()
# essential []
# essential {} Dict

# what is a Dict {}?
# Dictionary can have all types of data collections -
# Dict work as "KEY": "VALUE" pair
devops_student_1 = {
    "key": "value",
    "name": "James",
    "stream": "tech",
    "completed_lessons": 3, #int
    "complete_lessons_names": ["lists", "operations", "builtin methods"]

}
#print(devops_student_1)
#print(devops_student_1.keys())
#print(devops_student_1.values())
#print(type(devops_student_1))
#print(devops_student_1["name"])



# # delete  item from dict and delete operations
# devops_student_1["complete_lessons_names"].remove("operations")









# print(devops_student_1)
# find out how to change completed lesson from 3 to 2

# Control Flow

# if , elif, else statements - conditional statements

# sudo coding
# #
# weather = "dry" # True or False
#
# if weather >= "12" :
#     print("Let's do a BBQ") # execute this line if sunny
#
# elif weather >= "15":
#     print("getting there")
#
# else:
#     print("hope for the best") # this will be executed if weather isn't sunny
















