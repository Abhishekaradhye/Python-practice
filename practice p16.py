# -*- coding: utf-8 -*-

group = {'a':45, 'b':72,'A':5}
ans = {k.lower():group.get(k.lower(),0)+group.get(k.upper(),0) for k in group.keys()}
print(ans)


