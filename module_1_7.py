grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

stud_names = sorted(list(students))
median_grades = [sum(i)/len(i) for i in grades]
stud_grades = {stud_names[s]: median_grades[s] for s in range(len(stud_names))}
print(stud_grades)
