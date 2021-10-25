#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

x = 3
y = 5
li=[]

while x < 1000:
    li.append(x)
    x += 3
while y < 1000:
    li.append(y)
    y += 5
print(sum(li))




