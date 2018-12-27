# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?
import time
t=time.time()
def project_7(n):
   l=[]
   num=2
   l.append(2)
   while len(l)-1<n:
        if all(num%i!=0 for i in range(2,int((num)**0.5)+1)):
            l.append(num)
        num += 1
   print(l[n])
project_7(10001)
print(time.time()-t)
