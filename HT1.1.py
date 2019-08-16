##"""First programm""" 
##s= 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti.'
##if len(s)%2 == 0:
##    print("Symbols amount is chetnoe")
##else: print("Symbols amount is nechetnoe")

"""The 2 program"""
i = True
num = str([0,2,4,6,8])
s1 = input("Enter the value\n")
while i == True:
    if len(s1)!= 10:
        print("The string has not 10 symbols")
        s1 = input("Enter the value\n")
        if len(s1)== 10:
            for i in range(0, len(s1)):
                if i%2 == 0 and s1[i] in num and i+1%2 ==1 and (s1[i].isalpha  s1[i] not in num):
                    print("String has correct format"))


##"""The 3 program"""
##res = []
##s1 = input("Enter the value\n")
##a = s1[-1]
##for i in range(0,len(s1)):
##    if s1[i] == a:
##        res.append(i)
##print(res)


##"""The 4 program"""
##x_list=[]
##y_list=[]
##s1 = input("Enter the value\n")
##for i in range(0,len(s1)):
##	if s1[i] == "x":
##		 x_list.append(i)
##	elif s1[i] == "y":
##		y_list.append(i)
##if len(x_list)>0 and len(y_list)>0:
##	xmin = min(x_list)
##	ymin = min(y_list)
##	if xmin>ymin:
##		print("The y value is first")
##	elif xmin<ymin:
##		print("The x value is first")
##if len(x_list) == 0 and len(y_list)>0:
##    print("There is no x in the list. The y value is first")
##elif len(y_list) == 0 and len(x_list)>0:
##    print("There is no y in the list. The x value is first")
##else:print("There are no x and y values")


"""fifth programm"""
##s = input("Enter symbols\n")
##if len(s)> 10:
##    s = s[:6]
##else:
##    while len(s)<12:
##        s = s+'o'
##''.join(s)
##print(s)
##


##"""sixth programm""" 
##s = input("Enter symbols\n")
##counter = 0
##for i in s:
##    if i == " ":
##        counter +=1
##print(f'There amount of words is:',counter+1)

    
##"""seventh programm""" 
##s = input("Enter the value\n")
##new_s = list(s)
##if new_s[0]=="a" and new_s[1]=="b" and new_s[2]=="c":
##    new_s[0]="w"
##    new_s[1]="w"
##    new_s[2]="w"
##else: new_s.extend(["zzz"])
##print("".join(new_s))    
## 
	

"""eigth programm""" 
s = input("Enter symbols\n")
if s.startswith('abc'):
    s.replace('abc','www',1)
    print(s)

"""Progr 9"""
##s1 = input("Enter the value\n")
##s2 = input("Enter the value\n")
##s1_StartSlice = s1[:4]
##s2_StartSlice = s2[:4]
##s1_EndSlice = s1[-4:]
##s2_EndSlice = s2[-4:]
##if s1_StartSlice == s2_StartSlice and s1_EndSlice == s2_EndSlice:
##    print("The first 4 symbols and the last 4 symbols are equal in both")
##else: print("The first 4 symbols and the last 4 symbols are NOT equal in both"

##"""The 10 program"""
##s1 = input("Enter the value\n")
##res = s1[round(len(s1)/2)].lower()
##print(res)


    
