# You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# add computer science subject and grade
gradebook.append(["computer science", 100])

# add visual arts subject and grade
gradebook.append(["visual arts", 93])
# Access the index of the grade for visual arts and modify it to be 5 points greater
gradebook[-1][1] = 98

# Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it
gradebook[2].remove(85)
# append() a new "Pass" value to the sublist where your poetry class is located
gradebook[2].append("Pass")

# combine both lists to have one complete grade book
full_gradebook = last_semester_gradebook + gradebook

print(subjects)
print(grades)
print(gradebook)
print(full_gradebook)