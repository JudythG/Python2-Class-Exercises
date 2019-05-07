# using a lambda function to calculate mean
# calld statistics.mean to validate the result

import io
from functools import reduce
import statistics

grades = [5.5,7,8,9.5,2.5,3,10,9,6,5]

mean = reduce((lambda x, y: x+y), grades) / len(grades)
mean_comp = statistics.mean (grades)
print ("%d.2 %d.2" %(mean, mean_comp))
