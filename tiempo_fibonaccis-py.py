# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:55:45 2023

@author: Andres Florez
"""

import time as t
import fibonacci as fb
import fibonacci1 as fb1
for i in range(30,36): 
    ini = t.time()
    print('k =',i,', F:',fb.fibo(i),', fibo:', 
          round(t.time()-ini,3), end=' ')
    ini=t.time()
f=fb1.fiboI(i)
print(', fiboI: %.15f' % (t.time()-ini))
