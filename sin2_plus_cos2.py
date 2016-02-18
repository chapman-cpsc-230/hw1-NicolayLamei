#Sin & Cos
# I am using Python 3

from math import sin, cos, pi
x = pi/4
val = (sin(x))**2 + (cos(x))**2
print (val)

#Compute S in meters
v0 = 3 #m/s
t = 1 #s
a = 2 #m/s**2
s = v0 * t + 0.5*(a*t)**2
print (s)

#Verifying Equations
a = 3.3
b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*(a*b) + b2
eq2_sum = a2 - 2*(a*b) + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print ("First equation: '%g' = '%g' " % (eq1_sum, eq1_pow))
print ("Second equation: %d = %d" % (eq1_pow, eq2_pow))
