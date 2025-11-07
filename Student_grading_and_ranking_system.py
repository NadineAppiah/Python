print('How many students are there?')
students_num=int(input('Enter the number of students in the class: '))
students=[]
total_score=0

for i in range(students_num):
    name=input(f'Enter the name of the student{i+1}: ' )
    while True:
        score=float(input(f'Enter the score for {name} out of 100: ' ))
        if score >= 0 and score <= 100:
            print('Valid')
            break
        else:
         print('Invalid score, try again')
    
   
    if score >= 80 and score <= 100:
        grade='A'
    elif score >= 70 and score <= 79:
        grade='B'
    elif score >= 60 and score <= 69:
        grade='C'
    elif score >= 50 and score <= 59:
        grade='D'
    else:
        grade='F'
    total_score += score
    students.append({'name':name,'score':score,'grade':grade})
    
print('Grades')
for student in students:
    print(f'Name:'+student['name']+ ',Score:'+str(student['score'])+ ',Grade:'+student['grade'])

average_score=total_score/students_num
print('Average score of the class is:',average_score)
    
highest_score=max(student['score'] for student in students)
print('Highest score is:', highest_score)
top_student=max(student['name'] for student in students)
print('The student with the highest score is:', top_student)

lowest_score=min(student['score'] for student in students)
print('Lowest score is:', lowest_score)
worst_student=min(student['name'] for student in students)
print('The student with the lowest score is:', worst_student)

print('Ranking')
for i in range(len(students)):
    for j in range(0,len(students)-i-1):
        if students[j]['score']<students[j+1]['score']:
            students[j],students[j+1]=students[j+1],students[j]
for student in students:
    print('Name:'+student['name']+ '|Score:'+str(student['score'])+ '|Grade:'+student['grade'])
    

      



        
     