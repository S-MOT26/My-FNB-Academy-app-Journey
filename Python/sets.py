#sets
'''
my_sets={1,2,3,4,5}

print(my_sets)

my_sets.add(6)
print(my_sets)

my_sets.remove(3)
print(my_sets)

'''

set1={1,2,3}
set2={3,4,5}

#union
union_set=set1.union(set2)
print(union_set)

#intersection
inter_set=set1.intersection(set2)
print(inter_set)

#Difference
diff_set=set1.difference(set2)
print(diff_set)
