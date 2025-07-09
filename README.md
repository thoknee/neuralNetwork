#  Homemade neural Network

In an attempt to better understand neural networks and how they work I have gone through the process of creating one from scratch in python. 


The src folder has 3 important libraries and one for testing ground. The first 2 backpropagation and neural network build the framework of the neural network. Graph.py simply allows you to visualize the modifications you do to see how the back propogation will go through everything finding the gradient. 

In Testing.ipynb you can see how backpropogation and graph come together. First, you set up a series of equations: 

`
a = Var(3)
b = Var(12)
c = Var(-5)
d = Var(100)
e = Var(-12)
f = Var(19)


z = a + b
y = z * c * f
x = y / d
final = x + e
`

Now you can run .back() to get the gradients of each of these nodes and finally you can draw_graph(final). What comes from this can be seen in Testing and running for yourself.


The next part can be observed in the code.

