import theano
from theano import tensor

#declare two symbolic floating-point scalars
a = tensor.dscalar()
b = tensor.dscalar()

#create simple symbolic expression
c = a + b

#convert expression into callable object that takes (a,b) and computes c
f = theano.function([a,b], c)

result = f(1.5, 2.5)
print(result)
