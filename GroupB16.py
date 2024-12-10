def quick_sort(students,low,high):
    if(low<high):
        pi=partition(students,low,high)
        quick_sort(students,low,pi-1)
        quick_sort(students,pi+1,high)
        
def partition(students,low,high):
    pivot=students[high]
    i=low-1
    for j in range(low,high):
        if students[j]<=pivot:
            i+=1
            students[i],students[j]=students[j],students[i]
    students[i+1],students[high]=students[high],students[i+1]
    return i+1

students=[]
n=int(input("Enter number of students:"))
for i in range (0,n):
    percent=float(input("Enter percentange:"))
    students.append(percent)
quick_sort(students,0,len(students)-1)
print("Sorted array:",students)
print("Top 5 scores:",students[-5:])