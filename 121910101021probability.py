# -*- coding: utf-8 -*-
"""121910101021probability.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rczbpfPnlJb5YPZhmQkinIamk3kiYx1W
"""

A ={1,2,3,4,5}
B ={5,6,7}
print(2 in A)
type(2 in A)

A ={1,2,3,4,5}
B ={5,6,7}
C ={3,4,5}
B.issubset(A)
C.issubset(A)

def is_subset(A,B):
  for i in A:
    if i in B:
      pass
    else:
      return False 
  return true
A ={1,2,3,4,5}
B ={2,3,4}
print(is_subset(A,B))

import numpy as np
uni =set(np.arange(10))
print(uni)
A = set(np.arange(0,9,2))
print(A)
B =set(np.arange(0,9,3))
print(B)
P=A.union(B)
print(P)