
#for i in range(1,11):
 #if i%2==0:
  #      print(i)
#if i%2!=0:
   #     print(i)
#for i in range(0,10):     
 #     print(i)
#for i in range(1,10):  
 #     print(i)

#a=0
#b=1 
#num=int (input("enter the num:"))
#for i in range(num):
# c=a+b
 #a=b
 #b=c
 #print(c)

#for A in range(1,11):
  # if A%2==0 :
   #   print(A)
      #if A%2!=0:
       #  print(A)
#for A in range(0,11):
 #  print(A)
#for A in range(1,11):
 #  print(A)  
 
#for i in range(1,10):
 #  print(i,end=" ")
  # print(i*i)
  
  
  #   NESTED LOOP
#num=int(input("enter the numbwer:"))
#words=("one", "two","three","four","zero")
#a=str(num)
#for i in a:
 #  for x in words:
  #    print(i,x)
  

# ARMSTRONG METHOD:

#sum=0
#num=int(input("enter the num:"))
#a=str(num)
#for i in a:
   #sum=sum+int(i)**3
   #print(sum)
   #if sum==num:
  #  print("it is a armstrong")
 #   break  
#else:
#   print("it is not a armstrong")  


#BINARY TO DECIMAL:

#num=int(input("enter the binary number:"))
#sum=0
#x=str(num)
#for i in x:
 # sum=sum*2+int(i)
 # print(sum)

"""num=int(input("enter the number:"))
i=1
sum=1
while num!=0:
  sum=sum*2
  print(sum)
  i=i+1"""  
  
 #TABLE :
 
#for i in  range(1,11):
# print(i,"*",i,"=",end=" ")
 # print(i*i)
  
#i=0
#while i<=9:
 #i=i+1
#print(i,"*",i,"=",end=" ")
#print(i)

#FACTORIAL NUMBER
#sum=1
#num=int (input("entewr the num:"))
#for i in range(num):
 # sum=sum*i
  #print(i)
  
#n=int(input("enter the num:"))  
#i=1
#sum=1
#while i<=n:
 # sum=sum*i
  #i=i+1
#print(sum)
 #fIBONACCI NUMBERS:
 
#a=0
#b=1
#N=int(input("enter the num:"))
#for i in range(N): 
 # c=a+b
  #a=b
  #b=c
  #@print(c,"+",end=" ")   

#a,b=0,1
#while a<=N:
 #a,b=b,a+b
 #print(a,"+",end=" ")


# NUMBERS TO WORDS:

"""i,sum=0,0
num=(input("enter the num:"))
x=list(num)
y=len(x)
words={0:"zero",1:"one",2:"two",3:"three"}
while i<=y:
  print(words[int(x[i])],end=" ")
  print()
i=i+1 print(i) """


# ARM STRONG NUMBERS:

"""num=int (input("enter the num:"))
i=0
sum=0
while i<num:
  i=i+1
  sum=sum+int(i)**3
  print(sum)"""

  
#num=int (input("enter the num :"))
#b=str(num)
#sum=0
#for i in b:
 # sum=sum+int(i)**3
  #print(sum)
  #if sum==num:
   # print(sum,"its armstrong")
    #break
#else:
 # print(sum,"not")
#Q .1

# PATTERN QUETIONS:
#for rows in range(1,6):
 # for colums in range(rows):
  #  print(colums+1,end=" ")
  #print()
"""rows=0
star=0
num=int(input("enter the num:"))
while rows<num:
  star=rows+1
  while star>0:
   print(star,end=" ")
star=star+1
print()"""

#for rows in range(5):
 # for colums in range(5-rows-1,-1,-1):
  #  print(colums+1,end=" ")
  #print()
  
  
#for i in range (6):
 # for j in range(i):
  #  print(6-i,end=" ")
  #print()  
  
#for i in range(1,50+1):
 # if i%3==0:
  #  print("divya")
  # elif i%5==0:
   # print("bharthi")
   # if i%3==0  and i%5==0:
   # print("divya bharathi")
   # else:
   # 2print(i)      

#Q.2
    
#for i in range(5):
 # for j in range(i):
  #  print(5-j,end=" ")
  #print()
  
#Q.3

#for i in range (5,0,-1):
  #for j in range(i):
   # print(i,end =" ")
  #print() 


#Q.4

#for rows in range(5):
 # for colums in range(5-rows):
  #  print(colums+1,end=" ")
  #print()
  
  #Q.5

#for i in range(6):
 # for j in range(6-i-1):
  #  print(" ",end=" ")
  #for j in range(i):
   # print(j+1,end=" ")
  #print()

#Q.6

#for rows in range(5):
 # for colums in range(5-rows-1):
  #  print(" ",end=" ")
  #for colums in range(rows,-1,-1):
   # print(colums+1,end=" ")
  #print()   
  
 #Q.7
  
#for rows in range(5):
 # for colums in range(5-rows-1):
  #  print(" ",end=" ")
  #for colums in range(rows,-1,-1):
   # print(colums+1,end=" ")
  #print()   
  #print() 

#Q.8

#num=1
#for i in range(5):
 # for j in range(i):
  #  print(num,end=" ")
   # num=num+1
  #print() 
   
 # Q.9 
 
#for i in range(1,5):
 # for j in range(i+1):
  #  print(j*i,end=" ")
  #print()  
 
# Q.10

#for i in range(1,11,2):
 # for j in range(i):
  #  print(i,end=" ")
  #print()
  
 # Q.11
 
#for i in range(5):
 # for j in range(i):
  #  print("*",end=" ")
  #print() 
  
  #Q.12
  
#n=int (input("enter the num:"))
#for i in range(n):
 #  print(i,"*",i,"=",i*i,end=" ")
 #  print(i*i)
 
# Q.13
#n=input("enter the string:")
#length=len(n)
#for i in range(length):
 # for j in range(i+1):
  # print(n[i],end=" ")
  #print()
  
  
 # Q.14
 
#n=input("enter the charectores:")
#length=len(n)
#for i in range(1,6):
 # for j in range(5):
  #   print(i,end=" ")
 # print() 
 
 #Q.15
 
#for i in range(4):
 #  for j in range(4-i-1):
  #  print("",end=" ")
   #for k in range(2*i+1):
    #print("*",end=" ")  
   #print()   
   
   # out put quetions:
   
#for i  in (4,3,2,1,0):
 #   print(i,end=" ") 

#for i in range(10):
 # if(i%2!=0):
  #  print(i)
  
#for i in range(10,2,-2):
 # print("hello")  
 
 
#str="python Output baseed Quetions"
#word=str.split()
#for i in word:

#for i in range(7,10):
 # print("python output")
#print("python output ")


#for i in range(7,-2,-9):
 # for j in range(i):
  #  print(j)
  
#i="9"  
#for k in i:
 # print(k)


#for i in range(4,7):
 # i=i+3
  #print("hello",i)
  
  
#i=4
#while i<10:
 # i=i+3
  #print(i)
  
  
#for i in range(20):
 # if i//4==0:
  #  print(i)
  
  
#x=1234
#while x%10:
 # x=x//10
  #print(x)

 # Q
 #HAPPY NUMBER
 
 
#num=int(input("enter number:"))
#x=num
#while x>=10:
 # sum=0
  #while x>0:
   # r=x%10
    #sum=sum+r*r
    #x=x//10
  #print(sum)
  #x=sum
#if x==1:
 #     print(num,"num is happy number") 
#else:
 #     print(num,"num not a happy number")
 
 #  STRONG NUMBER:
 
#num =int(input("enter the num:"))
#x=num
#fact=1
#r=0
#sum=0
#while x>0:
 # r=x%10
  #for i in range(1,r+1):
   #fact=fact*i
  #sum=sum+fact
  #print(sum,"sum")
  #x=x//10
  #if sum==x:
   # print("it is a strong number")
  #else:
   # print("it is a not a strong number")
   
# PERFECT NUMBER

#num=int(input("enter the number:"))
#sum=0
#for i in range(1,num):
#  if num%i==0:
 #   sum=sum+i
  #  print(sum)
   # if num ==sum:
    #  print("it is a perfect number")
    #else:
     # print("it is not a perfect number")
     
     
     
# HARSHAD NUMBER:

#num=int(input("enter the number"))
#x=num
#sum=0
#while x>0:
 # a=x%10
  #sum=sum+a
  #print(sum)
  #x=x//10
#if num%sum==0:
 #  print(num,"it is a harshad number ")
#else:
 # print(num,"it is not a harshad number")
   
   
  
 # MAGIC NUMBER
 
#num=int(input("enter the num"))
#x=num
#while x>=10:
 #   sum=0
  #  while x>0:
   #   a=x%10
    #  sum=sum+a
     # x=x//10
    #x=sum
#if x==1:
 #   print(num," it is a magic number")
#else:
 #   print(num,"not a magic number")
 
   
  