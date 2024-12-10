def removeDuplicate(d):
    lst=[]
    for i in d:
        if i not in lst:
            lst.append(i)
    return lst

def union(lst1,lst2):
    lst3=[]
    lst3=lst1.copy()
    for i in lst2:
        if i not in lst3:
            lst3.append(i)
    return lst3

def intersection(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3

def difference(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i not in lst2:
            lst3.append(i)
    return lst3

def symmetric(lst1,lst2):
    lst3=[]
    d1=difference(lst1,lst2)
    d2=difference(lst2,lst1)
    lst3=union(d1,d2)
    return lst3

SE=[]
n=int(input("Enter total number of students in class:"))
for i in range(0,n):
    a=input("Enter name of students:")
    SE.append(a)
print("List of total students:",SE)

cricket=[]
n=int(input("Enter total number of students who play cricket:"))
for i in range(0,n):
    a=input("Enter name of students who play cricket:")
    cricket.append(a)
print("Original list of students who play cricket:",cricket)
cricket=removeDuplicate(cricket)
print("List of students who play cricket after removing duplicates:",cricket)

badminton=[]
n=int(input("Enter total number of students who play badminton:"))
for i in range(0,n):
    a=input("Enter name of students who play badminton:")
    badminton.append(a)
print("Original list of students who play badminton:",badminton)
badminton=removeDuplicate(badminton)
print("List of students who play badminton after removing duplicates:",badminton)

football=[]
n=int(input("Enter total number of students who play football:"))
for i in range(0,n):
    a=input("Enter name of students who play football:")
    football.append(a)
print("Original list of students who play football:",football)
football=removeDuplicate(football)
print("List of students who play football after removing duplicates:",football)

flag=1
while flag==1:
       print("1. Students who play both criket and badminton")
       print("2. Students who play either cricket or badminton but not both")
       print("3. Students who play neither cricket nor badminton")
       print("4. Students who play cricket and football but not badminton")
       print("5. Exit")
       ch=int(input("Enter your choice:"))
       
       if ch==1:
          print("List of students who play both cricket and badminton:",intersection(cricket,badminton))
          a=input("Do you want to continue(yes/no):")
          if a=='yes':
              flag=1
          else:
              flag=0
              
       elif ch==2:
          print("List of students who play either cricket or badminton but not both:",symmetric(cricket,badminton))
          a=input("Do you want to continue(yes/no):")
          if a=='yes':
              flag=1
          else:
              flag=0
              
       elif ch==3:
          print("List of students who play neither cricket nor badminton:",difference(SE,union(cricket,badminton)))
          a=input("Do you want to continue(yes/no):")
          if a=='yes':
              flag=1
          else:
              flag=0
              
       elif ch==4:
          print("List of students who play cricket and football but not badminton:",difference(intersection(cricket,football),badminton))
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
