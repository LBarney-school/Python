list1 = []
for i in range(100):
    list1.append(i)
print(list1)

list2 = ['Cat', 'Dog', 'Parrot', 'Bunny']
print(list2.pop())
print(list2)

list3 = ['Hat', 'Coat', 'Coat', 'Gloves', 'Hat', 'Coat', 'Socks']
print(list3.count('Hat'))

lst = [1,2,3]
print(lst)
lst.clear()
print(lst)

lst1 = [1,2,3]
print(lst1)
lst2 = lst1.copy()
print(lst2)
lst2.append(4)
print("List 1",lst1)
print("List 2",lst2)

lst = [1, 2, 3]
print(lst)
lst.insert(0, 0)
print(lst)
lst.insert(1,7)
print(lst)