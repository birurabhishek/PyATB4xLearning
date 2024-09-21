from PIL.ImageChops import difference
from pandas.core.computation.expr import intersection

unique_items = {1,2,3,3,4,4,4,4,5}

print(unique_items)

set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5}
set3 = {4,5,6,7,8}
union1 = set1.union(set3)
intersection1 = set1.intersection((set3))
difference1 = set1.difference(set3)
print("Union numbers are: ",union1)
print("Intersection numbers are: ",intersection1)
print("Difference numbers are: ",difference1)

subset = set3.issubset(set1)
subset2 = set1.issubset(set2)

print("Subsets are: ",subset)
print("Subsets are: ",subset2)