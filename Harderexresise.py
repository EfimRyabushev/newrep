#Упражнения "посложнее"
#1
for i in range (0, len(A) - 1, 2):
   A[i], A[i + 1] = A[i +1], A[i]
print (A)
#2
A = [1,2,3,4,5]
print ([A[-1]] + A[1:len(A) - 1] + [A[0]])
#3
for i in range(len(A)):
   if A[i] not in A[i + 1:]
      print A[i]
#4

