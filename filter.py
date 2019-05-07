# lambda function to filter from a list

import io
from functools import reduce

grades = [5.5,7,8,9.5,2.5,3,10,9,6,5]

filtered_grades = list(filter(lambda x: (x <= 4 or x >= 8), grades))
print (grades)
print (filtered_grades)
