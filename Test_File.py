names =  input("Enter your name: ") # get and process input for a list of names
names_list = names.split(",")
assignments =  input("Enter your missed assignment: ") # get and process input for a list of the number of assignments
assignments_list = assignments.split(",")
grades =  input("Enter your current grade: ") # get and process input for a list of grades
grades_list = grades.split(",")


# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names_list, assignments_list, grades_list):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))