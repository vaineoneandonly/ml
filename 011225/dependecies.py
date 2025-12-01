import numpy
#import matplotlib
import torch
#import sklearn
import sys

def tests():
    t1 = torch.randint(low = 0, high = 10, size = [7, 7, 3])
    print(t1)

    t2 = torch.randint(low = 0, high = 10, size = [147])
    print(t2)

    t1 = torch.flatten(t1) + t2
    print(t1)

def ex1():
    t1 = torch.zeros(3, 3)
    print(t1)

def ex2():
    t = torch.zeros(4, 4)
    for i in range(t.size(dim = 1)):
        t[i, i] = 4

    print(t)

    t2 = torch.eye(n = 4) * 4
    print(t2)

#ex3 implementing algos
def ex3a():
    t = torch.rand(5, 5)
    print(t)

    mean = 0
    n = 0

    variance = 0

    for i in range(t.size(dim = 0)):
        for j in range(t.size(dim = 1)):
            n += 1
            mean += t[i, j].item()

    mean /= n
    print(mean)

    for i in range(t.size(dim = 0)):
        for j in range(t.size(dim = 1)):
            variance += (t[i, j].item() - mean) * (t[i, j].item() - mean)     

    #bessel correction applied! 
    variance /= n - 1 

    print(torch.var(t))
    print(variance)


def ex3():
    t = torch.rand(5, 5)
    print(t)

    mean = float(torch.mean(t)) 

    item = t[0, 0].item() 
    itemDeviation = (item - mean) * (item - mean)
    variance = itemDeviation


    for i in range(1, t.size(dim = 1)):
        for j in range(0, t.size(dim = 1)):
            item = t[i, j].item()  
            itemDeviation = (item - mean) * (item - mean)

            variance = (variance + itemDeviation) / 2  

    sd = numpy.sqrt(variance)
    print(variance)
    print(sd)
    print(std)
    

if __name__ == "__main__":
    f = getattr(sys.modules[__name__], sys.argv[1], None)
    f()