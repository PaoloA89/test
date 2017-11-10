print('Hello World')
import numpy as np
a = 53+47
print(a)

def circumference(radius):
    b =2*np.pi*radius    
    return b
def circle_area(radius):
    return np.pi*radius**2
c = float(input("Dammi in ingresso valore raggio: "))
print(circumference(c),circle_area(c))



