# The knapsack problem
# Gabriela Ochoa

import os
import random
import matplotlib.pyplot as plt


# Single knapsack problem

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
print cap

plt.figure()
plt.scatter(weights, values)


def random_sol(number):
    l = []
    for i in range(number):
        x = int(random.getrandbits(1))
        # x = random.randint(0, 1)
        l.append(x)
    return l

list = random_sol(nitems)
# print "Random solution: ",list

def evaluate(sol):
    total_val = 0
    total_wei = 0
    print(sol)
    for i in range(len(sol)):
        if sol[i] == 1:
            total_val += values[i]
            total_wei += weights[i]

    return total_val, total_wei


# print "Evaluated solution: ", evaluate(list)

def random_search(tries):
    best_sol = []
    sol_val = 0
    sol_wei = 0
    for t in range(tries):
        sol = random_sol(nitems)
        val, wei = evaluate(sol)
        # print "Value: ", val, "Weight: ", wei
        if wei <= cap:
            if val > sol_val:
                sol_val = val
                sol_wei = wei
                best_sol = sol


    return best_sol, sol_val, sol_wei

best_sol, sol_val, sol_wei = random_search(10)
print "Random Search: "
print "Solution: ",best_sol, "Value: ", sol_val, "Weight: ", sol_wei

temp_val = values + []

def constructive():
    knapsack = 0
    best_val = 0
    indices = []
    while knapsack <= cap and temp_val:
        best = max(temp_val)    # determine maximum value in a list
        i = temp_val.index(best)  # determine index of a given value in a list
        del temp_val[i]         # delete item in position 'i' from a list
        i = values.index(best)
        print 'Best', best, 'Index', i
        if knapsack + weights[i] <= cap:
            knapsack += weights[i]
            best_val += best
            indices.append(i)
            print 'Added'
    return indices, best_val, knapsack


indices, value, knapsack = constructive()
print "Greedy Construction Heuristic Search: "
print 'Indices', indices, 'Value', value, 'Knapsack weight', knapsack