student=[[44,'prasad',75,87],[13,'ganguly',82,79],[53,'sasikala',72,80],[35,'manohar',86,85]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
