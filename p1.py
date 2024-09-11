count_student=int(input('count students:'))
students=[]
for i in range(count_student):
  student_id=input(f'student_id {i+1}:')
  name=input(f'name of student {i+1}:')
  score=float(input(f'score of student {i+1}:'))
  students.append((student_id,name,score))
search_name=input('Enter name to search:')
for student in students:
  if student[1]==search_name:
    print(f'id:{student[0]},name:{student[1]},score:{student[2]}')
    break
else:
  print('student not found.')