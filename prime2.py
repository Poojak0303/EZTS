n=int(input("enter a num"))
flag=0
if n<1:
    flag=1
elif n==1:
    flag=0
else :
    for i in range(2,(n//2)+1):
       if n%i==0:
           flag=1
           break
if flag ==1:
    print("not prime number")
else:
    print("prime number")
    