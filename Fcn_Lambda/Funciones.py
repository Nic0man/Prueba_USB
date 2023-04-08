a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c=[3]
d=[4]

print(list(map(lambda num1, num2: num1 + num2, c,d)))

print(list( map(lambda x,y : x*y, a,b) ))