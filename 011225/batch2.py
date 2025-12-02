from deps import *

def ex1():
    t1 = torch.randint(low = 0, high = 10, size = [3, 3])
    t2 = torch.randint(low = 0, high = 10, size = [3, 3])
    t3 = torch.matmul(t1, t2)

    print(t1)
    print(t2)
    print(t3)

def ex2():
    t1 = torch.rand(3, 3)

    print(torch.eye(n = 3) * t1)
    print(t1.det())

    print(t1)
    print(t1.inverse())

def ex3():
    t1 = torch.rand(3, 3)

    print(t1)

    for i in range(3):
        l1 = t1[i, 0:3]
        t1[i, 0:3] = torch.nn.functional.normalize(l1, p = 1.0, dim = 0)

    print(t1)