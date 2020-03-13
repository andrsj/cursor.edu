import numpy

def sigmoid(x):
    return 1 / (1 + numpy.exp(-x))

inputs = numpy.array([
    [0,0,1],
    [1,0,1],
    [1,1,0],
    [0,1,0]
])

outputs = numpy.array([
    [[1,1,0,0]]
]).T

synaptic_weights = 2 * numpy.random.random((3,1)) - 1 # [-1 ; 1]

print("Random weights:")
print(synaptic_weights)

for i in range(20000):
    input_layer = input
    outputs = sigmoid(numpy.dot(input_layer, synaptic_weights))

    err = input - outputs
    adjusments = numpy.dot(input_layer.T , err * (outputs * (1 - outputs)))

    synaptic_weights += adjusments

print("Weight after learning:")
print(synaptic_weights)

print("Result:")
print(outputs)