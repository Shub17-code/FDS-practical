def linear(roll):
    print("Using linear search")
    key=int(input("Enter roll number to search:"))
    for i in range(0,len(roll)):
        if(roll[i]==key):
            print("Student with roll number",key,"attended training program")
            break
    else:
        print("Student with roll number",key,"did not attended training program")
            
def sentinel(roll):
    print("Using sentinel search")
    key=int(input("Enter roll number to search:"))
    last=roll[n-1]
    roll[n-1]=key
    i=0
    while(roll[i]!=key):
        i+=1
    roll[n-1]=last
    if((i<n-1) or (roll[n-1]==key)):
        print("Student with roll number",key,"attended training program")
    else:
        print("Student with roll number",key,"did not attended training program")
        
roll=[]
n=int(input("Enter number of students:"))
for i in range (0,n):
    roll_no=int(input("Enter roll no:"))
    roll.append(roll_no)
     
flag=1
while flag==1:
        print("Select a search method:")
        print("1.Linear search")
        print("2.Sentinal search")
        print("3.Exit")
     
        ch=int(input("Enter your choice:"))
        
        if ch==1:
           linear(roll)
           a=input("Do you want to continue(yes/no):")
           if a=='yes':
              flag=1
           else:
              flag=0
            
        elif ch==2:
           sentinel(roll)
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