import random
print(random.randrange(1,10,2))
integers = [1,2,3,4,5]
for i in [1,2,3]:
    print(random.random())
    print(random.randint(10,20))
    print(random.choice(integers))
    print(random.sample(integers, i))
    print(random.uniform(0.1,0.3))


    random.shuffle(integers)
    print(integers)


"""
expovariate(lambd)
betavariate(alpha, beta) a > -1 | b > -1
gammavariate(alpha, beta) a > -1 | b > -1
gauss(mu, sigma)
"""