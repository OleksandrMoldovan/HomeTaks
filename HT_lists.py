##"""Program 1""" #done
##def add_books():
##    book = input("Enter the book you would like to add to the library\n")
##    library = []
##    library.append(book)
##    print(f"The book \"{book}\" was added to the library")


##"""Program 2""" # not done
##counter = 0
##numbers = input("Enter the a few numbers\n")
##numbers.split(" ")
##check_num = input("Enter the any value\n")
##for i in range(0,len(numbers)):
##    if numbers[i]== check_num:
##        counter = counter+1
##print(f"The value {check_num} is consisted in the numbers list {counter} times")


##"""Program 3""" #---done
##res = 0
##numbers = []
##numbers = input("Enter the a few numbers\n")
##a = numbers.split(" ")
##for i in range(0,len(a)):
##    if i%2==0 and a[i].isdigit():
##        res = res+int(a[i])
##print(f"The sum of all apropriate values is {res}")
      

####"""Program 4""" #---done  
##x = []
##numbers = input("Enter the a few numbers\n")
##a = numbers.split(" ")
##max = a[0]
##for i in range(0,len(a)):
##    if a[i]>a[0]:
##        max = a[i]
##    else: max = a[0]
##print(f"The max value of the entered numbers is {max}")


######"""Program 5""" #---done    
##a = [[222], [44], ["as", "dasd", "g"], [], [" "], [3,3,1,5,6,745,64564,57457,2,452]]
##def checker(list_of_lists):
##    for i in range(0,len(list_of_lists)):
##        if len(list_of_lists[i])>0:
##            print(f"Sub_list {i} is not empty")
##        else: print(f"Sub_list {i} is empty")


######"""Program 6""" #---done
numbers = input("Enter the a few numbers\n")
res = str(numbers)
"".join(res)
print(res)
