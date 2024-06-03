#HWK2
#ziyi Su

import numpy as np
import matplotlib.pyplot as plt
import time
import random
import pandas as pd

#p1 The function np.random.rand(shape) generates an array of a given shape with random numbers between 0 and 1. Each number in this array is a random sample from a uniform distribution over the interval [0, 1) and if I want to have it's range between a and b (assume right here 0<a,b<1), first is to multiply the array by (b - a). This scales the range of the values from [0, 1) to [0, b - a). Then add a to the array that shifts all the values in the array by a, so now they lie in the interval [a, b) ---- in mathe :Y = a + X*(b-a)


def problem_02(a,b,c):
    array = np.random.uniform(a, b, 100)
    mask = array < c
    return np.sum(mask)

def problem_03():
    array = np.random.rand(5, 5)
    out = array[[0, 2], 1:5]
    
    return out

def problem_04(a):
    array = np.ones((a, a))
    if a > 2:
        array[1:-1, 1:-1] = 0
    
    return array

def least_squares_error(x, y):
    if len(x) != len(y):
        raise ValueError("input arrays must have the same length.")
    return np.sum((x - y) ** 2)

def normalized_random(a):
    array = np.random.rand(a, a)
    array /= array.sum(axis=1, keepdims=True)
    
    return array

def problem_07():
    #fig1
    x = np.linspace(0.01, 10, 100)
    y = x*x

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x) = x^2")
    plt.title("Plot of f(x) = x^2")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("plot1.jpg")
    plt.close
    plt.show()
    
    #fig2
    x = np.linspace(-np.pi, np.pi, 100)
    y = np.sin(x)
    z = np.cos(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.plot(x, z)

    plt.title('Plot of f(x) and g(x)')
    plt.xlabel("x")
    plt.grid(True)
    plt.savefig("plot2.jpg")
    plt.close
    
    #fig3
    x = np.linspace(0.01, 5, 100)
    y = np.arctan(x)
    z = 1 / (1 + np.exp(-x))

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.plot(x, z)

    plt.title('Plot of f(x) and g(x)')
    plt.xlabel("x")
    plt.grid(True)
    plt.savefig("plot3.jpg")
    plt.close
    plt.show()

    
#p8
def sort_times_with01():
    times = {}
    time_list = []
    time_array = []
    for i in range(10):
        random_list = [random.randint(0, 10000000) for _ in range(10000000)]
        random_array = np.array(random_list)
        
        
        start1 = time.time()
        random_list.sort()
        end1 = time.time()
        total_time_list = end1-start1
        
        start2 = time.time()
        np.sort(random_array)
        end2 = time.time()
        total_time_array = end2-start2
        
        time_list.append(total_time_list)
        time_array.append(total_time_array)
        
    times['list'] = time_list
    times['array'] = time_array
        
    return times

def sort_times():
    times = {}
    time_list = []
    time_array = []
    for i in range(10):
        random_array = np.random.rand(10000000)
        random_list = random_array.tolist()
        
        
        start1 = time.time()
        random_list.sort()
        end1 = time.time()
        total_time_list = end1-start1
        
        start2 = time.time()
        np.sort(random_array)
        end2 = time.time()
        total_time_array = end2-start2
        
        time_list.append(total_time_list)
        time_array.append(total_time_array)
        
    times['list'] = time_list
    times['array'] = time_array
        
    return times

def table():
    #table1 with number from 0 to 1
    df = pd.DataFrame(sort_times_with01())


    fig, ax = plt.subplots(1, 1)
    table_data = []
    for row in df.itertuples(index=False):
        table_data.append(row)
    table = ax.table(cellText=table_data, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    ax.axis('off')
    plt.savefig("table_plot1.png")


    plt.show()
    plt.close()
    
    #table2 without number from 0 to 1
    df = pd.DataFrame(sort_times())


    fig, ax = plt.subplots(1, 1)
    table_data = []
    for row in df.itertuples(index=False):
    table_data.append(row)
    table = ax.table(cellText=table_data, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    ax.axis('off')
    plt.savefig("table_plot2.png")


    plt.show()
    plt.close()
    
#The sort time of a list, based on my graph, is approximately four times larger than times of sorting an array. There's a big difference between the first one with numbers from 0 to 10000000 and number range from 0 to 1. For the last one, the times of sorting list and sorting array are bascially follow the ratio of 3:1 . Then different range of number decides the difference between sort list and array. As the range gose up, the time of sort list also gose up but the time of sorting array remains constant.