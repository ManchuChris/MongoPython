#Convert list to dictionary using dictionary

s = ['a',1,'b',2,'c',3,'d',4]
dic = {s[i]:s[i+1] for i in range(1,7,2)}
print(dic)

num = [1,2,3,4,5,6,7]
alpha = ['a','b','c','d','e','f','g']
print(set(zip(num, alpha))) #zip returns tuple (x,y)
print({x: y for x, y in set(zip(num, alpha))})

# list to set
num = [1,2,3,4,5,6,7]
print(set(num))

# set to list
set = {1,2,3,4,5,6,7}
print(list(set))

# list to tuple