#-*-coding=utf-8-*-
from collections import deque

d=deque()
d.append(2)
d.append(4)
d.append(6)
d.append(8)
d.popleft()
print(d)