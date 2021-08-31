# Permutations and combinations

Lookout for or and and scenario.

Example : Given 3 pens and 2 markers, how many ways, can you pick any one of them? How many ways can you pick a pen and a marker?

The first case is an or scenario, the second, is an or, with an and scenario.

For first, we can pick 1 of 3 pens or 1 of 2 markers. So it can be done in a total of 3 + 2 ways.
For second we pick any 1 of 3 pens and 1 of 2 markers. So it can be done in a total 3 * 2 ways.

In permutations, order matter. In combinations, order does not matter.

In python, we can do the following :

```python
from itertools import combinations
from itertools import permutations
import numpy as np
import math
arr=np.array(['H','O','R','S','E'])
print(len(list(combinations(arr, 2)) ))
print(len(list(permutations(arr,2) )))  
```

Some libraries itertools, numpy, math, scipy, statistics

In how many ways can 10 balls be picked, from 7 red out of 10, and 3 blue out of 8?

```python
import math
red=math.factorial(10)/((math.factorial(7))*math.factorial(3))
blue=math.factorial(8)/((math.factorial(3))*math.factorial(5))
print(red*blue)
```
