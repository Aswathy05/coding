import random
import piModule

pi=piModule.pi
print(pi)

randomInt=random.randint(1,5)
print(randomInt)

randomFloat=random.random() #gives number from [0,1)
randomFloat=random.random()*5 #to expand the range
print(randomFloat)
