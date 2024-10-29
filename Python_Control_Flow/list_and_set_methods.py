#!/usr/bin/python3
"""demostrating list and sets methods"""
my_lists = [2, 5, 7, 6, 8]
print(my_lists)

"""using the append() method in list"""
my_lists.append(9)
print(my_lists)

"""using the remove() method in list"""
my_lists.remove(7)
print(my_lists)

"""using the pop()method in list"""
my_lists.pop()
print(my_lists)

"""using the sort() method in list"""
my_lists.sort()
print(my_lists)

"""using the reverse() method in list"""
my_lists.reverse()
print(my_lists)

"""using the extend() method in list"""
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]
my_list1.extend(my_list2)
print(my_list1)


"""set methods"""
my_sets = {2, 6, 4, 3}

"""using the add() method in sets"""
my_sets.add(1)
print(my_sets)

"""using the remove() method in sets"""
my_sets.remove(4)
print(my_sets)

"""using the union() method in sets"""
my_other_sets = {5, 6, 4, 7}
print(my_sets.union(my_other_sets))

"""using the intersection() method in sets"""
print(my_sets.intersection(my_other_sets))

"""using the difference() method in sets"""
print(my_sets.difference(my_other_sets))