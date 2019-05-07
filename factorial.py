# lambda function to calcuate a factorial
# calls math.factorial to validate the result

import io
from functools import reduce
import math

n = 6
fact = reduce((lambda x, y: x*y), list(range(1,n+1)))
fact_comp = math.factorial (n)
print ("%d %d" %(fact, fact_comp))
