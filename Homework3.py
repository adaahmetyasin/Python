# 1-) Write a Python script to concatenate following dictionaries to create a new one.
print("1-) ********************************************")
d1={1:'a', 2:'b'}
d2={3:'c', 4:'d'}
d3={5:'e', 6:'f'}
d4={**d1,**d2,**d3}
print(d4)


# 2-) Write a Python program to map two lists into a dictionary.
print("2-) ********************************************")
x1=[1, 2, 3, 4, 5, 6]
x2=['a', 'b', 'c', 'd', 'e', 'f']
x3 = dict(zip(x1, x2))
print(x3)


# 3-) Write a Python program to get the maximum and minimum value in a dictionary.
print("3-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}

max = max(d1.keys(), key=(lambda k: d1[k]))
min = min(d1.keys(), key=(lambda k: d1[k]))

print("Maximum Value:",d1[max],"Minimum Value: ",d1[min])


# 4-) Write a Python program to check a dictionary is empty or not.
print("4-) ********************************************")
empty_dict = {} 
if (len(empty_dict) == 0):     
    print('The dictionary is empty.') 
else:
    print('The dictionary is not empty.')


# 5-) Write a Python program which takes the keys of a dictionary and convert it to a list.
print("5-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}
print(d1.keys())


# 6-) Write a Python program which delete items from a dictionary and produce empty dictionary
print("6-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}
d1.clear()
print(d1)


# 7-) Write a Python script which takes a dictionary and returns the value of a specified key and remove that key- value pair from that dictionary.
print("7-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}
print(d1[3])
d1.pop(3)
print(d1,"(result for the key = 3)")


# 8-) Write a Python script which takes a dictionary and returns last item of that dictionary and remove it from the dictionary.
print("8-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}
last=list(d1.items())
print(last[-1])
d1.pop(6)
print(d1)


# 9-) Write a Python script which check if a specified key exists in a dictionary or not.
print("9-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}
key = int(input("Search key:"))
if key in d1.keys():
    print("True")
else:
    print("False")


# 10-) Write a Python script which takes a dictionary and create new one providing that their ID is different.
print("10-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}
d2=dict()

for i in range(1,7):
    d2[i] = d1[i]

if id(d1) == id(d2):
    print("their IDs are equal")
else:
    print("their IDs are different")


# 11-) Write a Python script which takes a dictionary and returns the value of a specified key.
print("11-) ********************************************")
d1={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
key = input("For key:")
print(d1[key])


# 12-) Write a Python script which takes a dictionary and returns the value of a specified key providing that it wouldnt produce an error even if that specified key is not in the dictionary.
print("12-) ********************************************")
try:
    d1={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
    key = input("For key:")
    print(d1[key])
except:
    print("None")


# 13-) Write a Python script to insert a member into a given set.
print("13-) ********************************************")
s1 = {1, 2, 3, 4, 5}
s1.add(6)
print(s1)


# 14-) Write a Python script to insert members into a given set.
print("14-) ********************************************")
s1 = {1, 2, 3, 4, 5}
s1.update([6, 7])
print(s1)


# 15-) Write a Python script to remove specified value from a given set.
print("15-) ********************************************")
s1 = {1, 2, 3, 4, 5}
s1.remove(3)
print(s1)


# 16-) Write a Python script to remove specified value from a given set providing that it wouldnt produce an error even if that specified value is not in the dictionary.
print("16-) ********************************************")
try:
    s1 = {1, 2, 3, 4, 5}
    remove_num = int(input("Remove number: "))
    s1.remove(remove_num)
    print(s1)
except:
    print("this set is not include your number")


# 17-) Write a Python script which returns an element from a given set and at the same time removes it.
print("17-) ********************************************")
s1 = {1, 2, 3, 4, 5}
print(list(s1)[0])
s1.discard(1)
print(s1)


# 18-) Write a Python script which removes all elements from a given set.
print("18-) ********************************************")
s1 = {1, 2, 3, 4, 5}
s1.clear()
print(s1)


# 19-) Write a Python script to check if a given value is present in a set or not.
print("19-) ********************************************")
s1 = {1, 2, 3, 4, 5}
number = int(input("Check number:"))
if number in s1:
    print("True")
else:
    print("False")


# 20-) Write a Python script to check if two given sets have no elements in common.
print("20-) ********************************************")
s1 = {1, 2, 3, 4, 5}
s2 = {'a', 'b', 'c'}
print(s1.isdisjoint(s2))


# 21-) Write a Python script to remove the intersection of a 2nd set from the 1st set.
print("21-) ********************************************")
s1 = {1, 2, 3, 4, 5}
s2 = {-1, 2, 0, 5, 10}
s1.difference_update(s2)
print(s1)


# 22-) Write a Python program to create a union of two given sets.
print("22-) ********************************************")
s1 = {1, 2, 3, 4, 5}
s2 = {-1, 2, 0, 5, 10}
s3 = s2.union(s1)
print(s3)


# 23-) Write a Python script which takes a dictionary and removes the item for the specified key.
print("23-) ********************************************")
d1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'}
d1.pop(4)
print(d1)


# 24-)  Write the expression to accesses the value of 60 from the variable X.
print("24-) ********************************************")
X = ['length', 'width', {'circle': 1, 'box': { 'x' : 50, 'y' : 60, 'z' : 70}, 'cube': 2}, 'height', 'diameter']
print(list(X[2]["box"].values())[1])