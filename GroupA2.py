def average(marks):
    sum=0
    count=0
    for i in range(0,len(marks)):
        if(marks[i]!=-1):
            sum+=marks[i]
            count+=1
    avg=sum/count
    print("Average score:",avg)

def highest(marks):
    max=0
    for i in range(0,len(marks)):
        if(marks[i]>max):
            max=marks[i]
    print("Highest score:",max)

def lowest(marks):
    min=31
    for i in range(0,len(marks)):
        if(marks[i]<min and marks[i]!=-1):
            min=marks[i]
    print("Lowest score:",min)

def absent(marks):
    count=0
    for i in range(0,len(marks)):
        if marks[i]==-1:
            count+=1
    print("Number of students who were absent:",count)

def frequency(marks):
    max=0
    h=0
    count=0
    for i in range(0,len(marks)):
        for j in range(i+1,len(marks)):
            if(marks[i]==marks[j]):
                count+=1
                if count>max:
                    max=count
                    h=marks[i]
    print("Highest frequency marks:",h,"with frequency:",max)
    
n=int(input("Enter total no of students:"))
print("Enter -1 for absent no")
marks=[]
for i in range(0,n):
    b=int(input("Enter marks:"))
    marks.append(b)
flag=1
while flag==1:
    print("\n Menu")
    print("1.Average")
    print("2.Highest and lowest")
    print("3.No of students absent")
    print("4.Marks with highest frequency")
    print("5.Exit")

    ch=int(input("Enter your choice:"))
    if ch==1:
        average(marks)
        a=input("Do you want to continue(yes/no):")
        if a=='yes':
            flag=1
        else:
            flag=0
            
    elif ch==2:
        highest(marks)
        lowest(marks)
        a=input("Do you want to continue(yes/no):")
        if a=='yes':
            flag=1
        else:
            flag=0
            
    elif ch==3:
        absent(marks)
        a=input("Do you want to continue(yes/no):")
        if a=='yes':
            flag=1
        else:
            flag=0
            
    elif ch==4:
        frequency(marks)
        a=input("Do you want to continue(yes/no):")
        if a=='yes':
            flag=1
        else:
            flag=0
            
    elif ch==5:
        print("Exit")
        flag=0
    else:
        print("Wrong input")
        a=input("Do you want to continue(yes/no):")  
        if a=='yes':
            flag=1
        else:
            flag=0
