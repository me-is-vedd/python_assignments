#List Operations
students_list = ["Ved", "Rahul", "Aman"]
print("Original List:", students_list)
# Add
students_list.append("Riya")
print("After Adding:", students_list)
# Update
students_list[1] = "Rohan"
print("After Updating:", students_list)
# Delete
students_list.remove("Aman")
print("After Deleting:", students_list)

# -----------------------------------------

#Tuple Operations
students_tuple = ("Ved", "Rahul", "Aman")
print("Original Tuple:", students_tuple)
# Add
students_tuple = students_tuple + ("Riya",)
print("After Adding:", students_tuple)
# Update
students_tuple = list(students_tuple)
students_tuple[1] = "Rohan"
students_tuple = tuple(students_tuple)
print("After Updating:", students_tuple)
# Delete
students_tuple = list(students_tuple)
students_tuple.remove("Aman")
students_tuple = tuple(students_tuple)
print("After Deleting:", students_tuple)

# -----------------------------------------

#Dictionary Operations
students_dict = {1: "Ved",2: "Rahul",3: "Aman"}
print("Original Dictionary:", students_dict)
# Add
students_dict[4] = "Riya"
print("After Adding:", students_dict)
# Update
students_dict[2] = "Rohan"
print("After Updating:", students_dict)
# Delete
del students_dict[3]
print("After Deleting:", students_dict)



l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)