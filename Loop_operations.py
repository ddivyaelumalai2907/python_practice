
# while n<=100:
#     print(n,end=" ")
#     n +=1
# else:
#     print("Done!!")

# for i in range(10,-4,-1):
#     print(i)


#a = [1,2,3,4,5]

# for i in a:
#     print(i)


#for i in a:
    #pass
    #print(i)
    # if i >2:
    #     print("break")
    #     break
    # if i == 3:
    #     print("continue")
    #     continue

# a = [1,2,3,4,5,6,7,8,9,0]

# for i in a :
#     if(i%2 == 0 ):
#         print(i,"even")
#     else:
#         print(i,"odd")

# a = int(input("Enter the number for  multiplication:"))
# for i in range(1,10+1):
#     print(a ,"*", i ," = ",a*i)

# a = int(input("Enter the number:"))
# count =0
# while(a < 5):
#     print(a)
#     a=a+1
#     count = count+1
# print("loop finished")
# print("count=",count)
'''SUM OF NUMBERS'''
# a = int(input("number="))
# i=1
# sumof = 0
# while(i <= a):
#     print(i)
#     sumof = sumof+i
#     i = i+1
# print("sum=",sumof)

# a = int(input("number="))
# sumof = 0
# for i in range(a+1):
#     print(i)
#     sumof = sumof+i
# print("sum=",sumof)

# a = [12,76,35,22,10,25,39,30,111,190,200,345]
# count = 0
# for i in a:
#     if(i%5 == 0):
#         print(i)
#         count = count+1
# print("count=",count)

'''COUNT DIGITS IN A NUMBER'''
# a = 121
# i=0
# countdig = 0
# while a !=0:
#     a = a//10
#     countdig = countdig + 1
# print(countdig)
'''RANGE COMPARSION'''
# m = range(3,1)
# for i in  m:
#     print(i,end=" ")
# print(m)
# n = range(3,1)
# for i in  n:
#     print(i,end=" ")
# print(n)
# print(n == m)

'''FOR ELSE'''
# a = [1,3,4,5,6]

# for i in range(4):
#     print(i,end=" ")
# else:
#     print("out")

'''PROBLEM:MOVE THE NEGATIVE NUMBER TO LAST'''
# a = [3,4,5,-2,-1,2,8,0,-4]

# n = len(a)
# i=0
# j=1
'''BUBBLE SORT'''
# for i in range(n):
#     swap = False
#     for j in range(0,n-1):
#         if a[j] < a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = temp
#             swap = True
#     if(swap!=True):
#         break
# print(a)


'''PEAK ELEMENT'''
# a = [3,4,6,7,5]
# n = len(a)
# for i in range(n):
#     if(a[i] > a[i-1]and a[i] > a[i+1]):
#         print("peak element - ",a[i])

'''BREAK'''
# for i in range(10):
#     print(i)
#     if i == 8:
#         break

'''CONTINUE'''
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

'''PASS'''
for i in range(5):
    if i == 3:
        pass
    print(i)



