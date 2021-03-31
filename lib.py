import bisect
import math
from ast import literal_eval

# ----------------------------------------
def calculate_shapley_ij(c, j ,characteristic ,n,i):
    #for calculation after tohi
    var2=0

    if j != [0]:
        #insert i+1 at the first of c
        bisect.insort_left(c, i + 1)
        var2=characteristic[tuple(j)]
    else:
        #for calculation after tohi
        c = [i + 1]

    print (i+1,"commes after",j)
    print (c ,"--->",characteristic[tuple(c)])

    delta = float(characteristic[tuple(c)] - var2)
    print (characteristic[tuple(c)] ,"-",var2,"=",delta)
    print("-----------")

    temp = delta / float(math.factorial(n))

    return temp


def get_data(fileName):
    with open(fileName) as players:
        data = [line.rstrip() for line in players]
    players.close()

    return data
# -----------------------------------------