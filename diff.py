set1= {1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,33,3,4,4,4,4,4,4}
print(set1)

set1.add(5)
print(set1)
set2= {1,2,3,4,5,6,7,8,9}

diff= set2.difference(set1)
print(diff)

symmetric_diff= set1.symmetric_difference(set2)
print(symmetric_diff)