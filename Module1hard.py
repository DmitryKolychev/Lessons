grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(sorted(students))
grades1 = grades[0]
grades1_1 = sum(grades1[:])/len(grades1)
students1 = students_list[0]
grades2 = grades[1]
grades2_1 = sum(grades2[:])/len(grades2)
students2 = students_list[1]
grades3 = grades[2]
grades3_1 = sum(grades3[:])/len(grades3)
students3 = students_list[2]
grades4 = grades[3]
grades4_1 = sum(grades4[:])/len(grades4)
students4 = students_list[3]
grades5 = grades[4]
grades5_1 = sum(grades5[:])/len(grades5)
students5 = students_list[4]
gruppa = ({students1: grades1_1, students2: grades2_1, students3: grades3_1, students4: grades4_1, students5: grades5_1})
print("Список учеников:", students_list)
Name = input('Введите имя из списка:')
print('Средний балл ученика', Name + ":", gruppa[str(Name)])
print('Список всех учеников и их средний балл:', gruppa)