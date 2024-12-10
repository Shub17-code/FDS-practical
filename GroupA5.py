def word_with_longest_length(string):
    max_len=0
    current_word=""
    longest_word=""
    
    for char in string +' ':
        if char!=' ':
            current_word+=char
        else:
            if max_len<len(current_word):
                max_len=len(current_word)
                longest_word=current_word
            current_word=""
    return longest_word

def frequency(string,c):
    count=0
    for char in string:
        if char==c:
            count+=1
    return count

def is_pallindrome(string):
    pallindrome=""
    for char in string:
        if char!=' ':
            pallindrome+=char.lower()
    
    left,right=0,len(pallindrome)-1
    while left<right:
        if pallindrome[left]!=pallindrome[right]:
            return False
        left+=1
        right+=1
    return True

def first_appearance(string,substring):
    n=len(string)
    m=len(substring)
    for i in range(n-m+1):
        match=True
        for j in range(m):
            if string[i+j]!=substring[j]:
                match=False
                break
        if match:
            return i
    return -1

def occurence(string):
    words=string.lower().split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
            
    print("Word occurences:")
    for word,count in word_count.items():
        print(f"{word}:{count}")
        
string=input("Enter string:")
flag=1
while flag==1:
    print("1.To display word with longest length")
    print("2.To determine the frequency of particular character in the string")
    print("3.TO check whether given string is pallindrome or not")
    print("4.To display index of first appearance of substring")
    print("5.To count the occurences of each word in a given string")
    print("6.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
      print("Word with longest length:",word_with_longest_length(string))
      m=input("Do you want to continue:(Yes/No):")
      if m=='yes':
         flag=1
      else:
         flag=0
    elif ch==2:
       s=input("Enter character to find frequency:")
       print("Frequency of:",s,frequency(string,s))
       m=input("Do you want to continue:(Yes/No):")
       if m=='yes':
          flag=1
       else:
          flag=0
    elif ch==3:
       print("Is the string a pallindrome?",is_pallindrome(string))
       m=input("Do you want to continue:(Yes/No):")
       if m=='yes':
          flag=1
       else:
          flag=0
    elif ch==4:
       substring=input("Enter substring:")
       print("Index of first appearance of substring:",first_appearance(string,substring))
       m=input("Do you want to continue:(Yes/No):")
       if m=='yes':
        flag=1
       else:
         flag=0
    elif ch==5:
       occurence(string)
       m=input("Do you want to continue:(Yes/No):")
       if m=='yes':
         flag=1
       else:
         flag=0
    elif ch==6:
       print("Exit")
       flag=0
    else:
       print("Invalid choice")
   

    