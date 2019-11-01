import os
import random
import matplotlib.pyplot as plt

# Read the instance  data given a file name. Returns: n = no. items,
# c = capacity, vs: list of item values, ws: list of item weights

def read_kfile(fname):
    with open(fname, 'rU') as kfile:
        lines = kfile.readlines()  # reads the whole file
    n = int(lines[0])
    c = int(lines[n + 1])
    vs = []
    ws = []
    lines = lines[1:n + 1]  # Removes the first and last line
    for l in lines:
        numbers = l.split()  # Converts the string into a list
        vs.append(int(numbers[1]))  # Appends value, need to convert to int
        ws.append(int(numbers[2]))  # Appends weight, need to convert to int
    return n, c, vs, ws


dir_path = os.path.dirname(os.path.realpath(__file__))  # Get the directory where the file is located
os.chdir(dir_path)  # Change the working directory so we can read the file

knapfile = 'knap20.txt'
nitems, cap, values, weights = read_kfile(knapfile)

def evaluate(sol):
    total_val = 0
    total_wei = 0
    for i in range(len(sol)):
        if sol[i] == 1:
            total_val += values[i]
            total_wei += weights[i]

    return total_val, total_wei


def random_sol(number):
    l = []
    for i in range(number):
        x = int(random.getrandbits(1))
        # x = random.randint(0, 1)
        l.append(x)
    return l


def random_sol_valid(n):
    binvalid = True
    while binvalid:
        s = random_sol(n)
        v, w = evaluate(s)
        binvalid = (w > cap)
    return s, v, w


def random_search_valid(tries):
    temp_values = []
    best_sol = []
    best_val = 0
    best_wei = 0
    for t in range(tries):
        sol, val, wei = random_sol_valid(nitems)
        temp_values.append(val)
        if wei <= cap:
            if val > best_val:
                best_val = val
                best_wei = wei
                best_sol = sol


    return temp_values, best_sol, best_val, best_wei


search_values, best_sol, best_val, best_wei = random_search_valid(10)
print('Values: ',  search_values, 'Solution: ', best_sol, 'Value: ', best_val, 'Weight: ', best_wei)

def local_optima(sol):
    optima = True
    sol_val, sol_wei = evaluate(sol)
    for i in range(len(sol)):
        if(sol[i] == 1):
            sol[i] = 0
        else:
            sol[i] = 1

        val, wei = evaluate(sol)
        if(sol_val < val & wei < cap):
            optima = False

    return optima

print 'Is it optimal?: ', local_optima(best_sol)

def random_valid_neig(sol):
    length = len(sol)
    binvalid = True
    while binvalid:
        i = random.randint(0, length - 1)
        if (sol[i] == 1):
            sol[i] = 0
        else:
            sol[i] = 1

        v, w = evaluate(sol)
        binvalid = (w > cap)

    return sol, v, w

sol, val, wei = random_valid_neig(best_sol)
print 'Solution: ', sol, 'Value: ', val, 'Weight: ', wei

def hill_climbing():
    s = random_sol_valid(20)
    tries = []
    while not local_optima(s):
        tries.append(s)
        v, w = evaluate(s)
        s1 = random_valid_neig(s)
        v1, w1 = evaluate(s1)
        if v1 > v :
            s = s1

    return s, tries

# s, sols = hill_climbing()
# print s, sols

