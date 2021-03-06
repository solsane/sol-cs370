#!/usr/bin/env python3
# Template for COSC 370 Hwk #8
# Approximation of derviatives using FDA, Richardson extrapolation,
# and polynomial interpolation
#
'''
Homework 8: Finite Difference Approximations and Polynomial Interpolation for Derivatives
Author: Aiden Rutter
netid: arutter1
Description:
Solves problems 9 and 11 in problem set 5.1
'''

from numpy import round, array, polyfit, polyder, polyval, poly1d
#
# Problem 5.1.9
#
print("Problem 5.1.9\n=============")
#
# This is an example of a dictionary with key:value pairs,
# data9[0.1]=0.078348 and data9[0.3]=0.192916, for example.
#
data9 = { 0.0: 0.0, 0.1: 0.078348, 0.2: 0.138910, 0.3: 0.192916, 0.4: 0.244981 }
#
# We want to approximate f'(0.2) using two different values of h (=0.2, 0.1)
#
# First use central difference FDA, i.e., 2hf'(x) = -f(x-h) + f(x+h), with h=0.2
#
h1 = 0.2
x = 0.2
# Calculate first central difference approximation
centralApprox1 = (-data9[x-h1] + data9[x+h1]) / (2 * h1)
print("Central FDA Approximation (h = 0.2): %f" % centralApprox1)
#
# Now, half the stepsize and set h=0.1
# and use the function all round(x+h2, decimals=1) so that you can
# insure the proper key from the data9 dictionary will be selected.
#

h2 = h1 / 2.0
# Calculate second central difference approximation
centralApprox2 = (-data9[round(x-h2, 1)] + data9[round(x+h2, decimals=1)]) / (2 * h2)
#
# Now, apply Richardson Extrapolation to improve the approximation of f'(0.2)
# using centralApprox1 and centralApprox2

p = 2.0
# Using central difference approx (h1, h1/2), calculate improved
# approximation with richardson extrapolation
richardsonExtrap = (2 ** p * centralApprox2 - centralApprox1) / (2 ** p - 1)
print("Richardson Extrapolation (h2 = h1 / 2, p = 2): %f" % richardsonExtrap)

#
# Problem 5.1.11
#
print("\nProblem 5.1.11\n==============")
#
# Here are the interpolation data points...
#
xData = array([-2.2, -0.3, 0.8, 1.9])
yData = array([15.18, 10.962, 1.92, -2.04])
m = 3
# Using polyfit and polyder from Numpy...

# First compute the coefficients for a cubic interpolating
# polynomial using polyfit

p = polyfit(xData, yData, m)
#
# Then, use those coefficients to construct the first (d1) and
# second (d2) derivative functions via polyder...
#
d1 = polyder(p)
d2 = polyder(p, 2)
#
# Here are the coeffcients of the actual polynomial, whose derivatives
# we are approximating.
#
pActual = array([1, -0.3, -8.56, 8.448])

# Use those coefficients to construct the first (d1Actual) and
# second (d2Acutal) derivative functions via polyder...

d1Actual = polyder(pActual)
d2Actual = polyder(pActual, 2)

# Now, evaluate the first derivative of your cubic interpolating polynomial
# at x=0, and then do the same for the first derivative of the actual
# polynomial whose coefficients are given in pActual.
def evalPoly(nparr, x):
    y = 0
    for i in range(len(nparr)):
        y += nparr[len(nparr)-i-1] * x ** i
    return y

# fd = d1(0.)
# fdActual = d1Actual(0.)
fd = evalPoly(d1, 0.)
fdActual = evalPoly(d1Actual, 0.)

print("Interpolated f'(0): %f" % fd)
print("Actual f'(0): %f" % fdActual)
print("Error: %f\n" % (fdActual - fd))

# Now, evaluate the second derivative of your cubic interpolating polynomial
# at x=0, and then do the same for the second derivative of the actual
# polynomial whose coefficients are given in pActual.

sd = evalPoly(d2, 0.)
sdActual = evalPoly(d2Actual, 0.)

print("Interpolated f''(0): %f" % sd)
print("Actual f''(0): %f" % sdActual)
print("Error: %f" % (sdActual - sd))
#
# Outputs for verification:
#
# Problem 5.1.9
# =============
# Central FDA Approximation (h = 0.2): 0.612452
# Richardson Extrapolation (h2 = h1 / 2, p = 2): 0.559636
#
# Problem 5.1.11
# ==============
# Interpolated f'(0): -8.560000
# Actual f'(0): -8.560000
# Error: -0.000000
#
# Interpolated f''(0): -0.600000
# Actual f''(0): -0.600000
# Error: -0.000000
