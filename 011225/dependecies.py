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

    # not working as expected, for some reason.
    mean = t[0, 0].item()

    for i in range(1, t.size(dim = 1)):
        for j in range(0, t.size(dim = 1)):
            mean = (mean + t[i, j].item()) / 2


    standardDeviation1 = (t[0, 0].item() - mean) * (t[0, 0].item() - mean) 
    print(standardDeviation1)
    print(mean)
    
def ex3():
    t = torch.rand(5, 5)
    print(t)

    mean = float(torch.mean(t)) 


    #std = torch.std(t)

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