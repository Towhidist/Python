"""while True:
    msg= input("Enter a message: ")
    if msg=="x":
        break
    print(msg)
"""
# i=1
# sum=0
# while i<=10:
#     #sum=sum+i
#     print(i,end="+")
#     if i==10:
#         print(i, end="")
#     sum+=i
#     i+=1

# print("=",sum)
i=1
sum=0
while i<=10:
    #sum=sum+i
    print(i,end="+")
           
    sum+=i
    i+=1

print("\b=",sum)

#simple fibonacci series

# a,b=0,1
# while b<10:
#     print(b,end="\t")
#     a,b=b,b+a 
#factorial of a given number
"""
4!=4*3*2*1=24

"""

n=int(input("Enter the value of n: "))
f=1
i=1
while i <=n:
    f*=i
    i+=1
print(f"the factorial of {n} is {f}")