from random import randint

# Fill matrices with random integer values
a11 = randint(0, 9)
a12 = randint(0, 9)
a21 = randint(0, 9)
a22 = randint(0, 9)
b11 = randint(0, 9)
b12 = randint(0, 9)
b21 = randint(0, 9)
b22 = randint(0, 9)

# Traditional matrix multiplication
# O(N^3)
c11 = a11 * b11 + a12 * b21
c12 = a11 * b12 + a12 * b22
c21 = a21 * b11 + a22 * b21
c22 = a21 * b12 + a22 * b22

# Strassen's method
# O(N^2.807)
q1 = (a11 + a22) * (b11 + b22)
q2 = (a21 + a22) * b11
q3 = a11 * (b12 - b22)
q4 = a22 * (-b11 + b21)
q5 = (a11 + a12) * b22
q6 = (-a11 + a21) * (b11 + b12)
q7 = (a12 - a22) * (b21 + b22)

assert (c11 == q1 + q4 - q5 + q7)
assert (c21 == q2 + q4)
assert (c12 == q3 + q5)
assert (c22 == q1 + q3 - q2 + q6)