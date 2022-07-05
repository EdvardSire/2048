import numpy as np

x = np.array([[1,3],
              [2,4]], dtype=np.uint16)

y = np.array([[2,2],
              [2,2]], dtype=np.float16)

print(x)
print(y)
print(np.multiply(x,y))            
print(np.multiply(x,y).sum())            

