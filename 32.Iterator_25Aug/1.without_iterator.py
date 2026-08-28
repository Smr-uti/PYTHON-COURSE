L = [x for x in range(1, 100001)]
for i in L:
    print(i * 2)

import sys
print(sys.getsizeof(L)/1024)