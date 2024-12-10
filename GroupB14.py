def selection_sort(students):
    for i in range(len(students)-1):
        min_index=i
        for j in range(i,len(students)):
            if students[min_index]>students[j]:
                min_index=j
        students[i],students[min_index]=students[min_index],students[i]
    print("Sorted array:",students)
    print("Top 5 scores:",students[i])

def bubble_sort(students):
    for i in range(len(students)):
        for j in range(len(students)-1):
            if students[j]>students[j+1]:
                students[j],students[j+1]=students[j+1],students[j]
    print("Sorted array:",students)
    print("Top 5 scores:",students[-5:])

students=[]
n=int(input("Enter number of students:"))
for i in range (0,n):
    percent=float(input("Enter percentange:"))
    students.append(percent)
     
flag=1
while flag==1:
        print("Select a sorting method:")
        print("1.Selection sort")
        print("2.Bubble sort")
        print("3.Exit")
     
        ch=int(input("Enter your choice:"))
        
        if ch==1:
           selection_sort(students)
           a=input("Do you want to continue(yes/no):")
           if a=='yes':
              flag=1
           else:
              flag=0
            
        elif ch==2:
           bubble_sort(students)
           a=input("Do you want to continue(yes/no):")
           if a=='yes':
              flag=1
           else:
              flag=0    
   
        elif ch==3:
            print("Exit")
            flag=0
            
        else:
            print("Wrong input")
            a=input("Do you want to continue(yes/no):")  
            if a=='yes':
              flag=1
            else:
              flag=0