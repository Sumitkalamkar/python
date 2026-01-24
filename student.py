students=[]

n=int(input("no. of students:"))


for i in range(n):

     print(f"Enter student details of students {i+1}:")

     name = input("Enter Name:")

     marks=[]
     for j in range(7):
          
         while True:
              mark=int(input(f"Enter mark of subject {j}"))
              if 0<= mark <=100:
                   marks.append(mark)
                   break
              else:
                   print("Invalid mark, please enter again")
         

     student={
           'Name':name,
           'Maths':marks[1],
           'Physics':marks[2],
           'DBMS':marks[3],
           'OS':marks[4],  
           'AIES':marks[5],
           'GCP':marks[6] 
     }

     students.append(student)


     for student in students:
          
            total=student['Maths']+student['Physics']+student['DBMS']+student['OS']+student['AIES']+student['GCP']
            percentage=total/6
            
            fail_count=0
            
            for key in student:
                 if key != 'Name' and student[key]<40:
                        fail_count+=1
            
            print(f"Student Name:{student['Name']}")
            print(f"Percentage:{percentage}%")
            
            if fail_count==0:
                 print("Result: PASS")
                 if percentage>=90:
                        grade='A+'
                 elif percentage>=80:
                        grade='A'
                 elif percentage>=70:
                        grade='B+'
                 elif percentage>=60:
                        grade='B'
                 elif percentage>=50:
                        grade='C'
                 else:
                        grade='D'
                 
                 print(f"Grade:{grade}")
            
            elif fail_count<=2:
                 print("Result: ATKT")
            else:
                 print("Result: FAIL")
            
            print("--------------------------------------------------------------")
print(f'failed student ',name if fail_count>0 else 'passed student',name)
                   
