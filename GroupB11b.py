def binary(roll,low,high,key):
    if(low<=high):
        mid=int((high+low)/2)
        if roll[mid]==key:
            return mid
        elif roll[mid]>key:
            return binary(roll,low,mid-1,key)
        else:
            return binary(roll,mid+1,high,key)
    else:
        return -1
    
def fibonacci(roll,key):
    fib1,fib2=1,0
    fibn=fib2+fib1
    n=len(roll)
    
    while fibn<n:
        fib2=fib1
        fib1=fibn
        fibn=fib2+fib1
        
    offset=-1
    while fibn>1:
        index=min(offset+fib2,n-1)
        if roll[index]>key:
            fibn=fib2
            fib1=fib1-fib2
            fib2=fibn-fib1
            
        elif roll[index]<key:
            fibn=fib1
            fib1=fib2
            fib2=fibn-fib1
            offset=index
        
        else:
            return index
    
    if offset + 1 < len(roll) and roll[offset+1]==key and fib1==1:
        return offset + 1
      
    return -1
    
roll=[]
n=int(input("Enter number of students:"))
for i in range (0,n):
    roll_no=int(input("Enter roll no:"))
    roll.append(roll_no)
for i in range(0,len(roll)):
    for j in range(i+1,len(roll)):
        if roll[i]>roll[j]:
            roll[i],roll[j]=roll[j],roll[i]
print("The roll numbers of students in sorted order:",roll)
     
flag=1
while flag==1:
        print("Select a search method:")
        print("1.Binary search")
        print("2.Fibonacci search")
        print("3.Exit")
     
        ch=int(input("Enter your choice:"))
        
        if ch==1 or ch==2:
            key=int(input("Enter roll number to search:"))
            
            if ch==1:
               result=binary(roll,0,len(roll)-1,key)
               if result!=-1:
                   print("Student with roll number",key,"attended the program")
               else:
                   print("Student with roll number",key,"did not attended the program")
               a=input("Do you want to continue(yes/no):")
               if a=='yes':
                flag=1
               else:
                flag=0
            
            elif ch==2:
               result=fibonacci(roll,key)
               if result!=-1:
                   print("Student with roll number",key,"attended the program")
               else:
                   print("Student with roll number",key,"did not attended the program")
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