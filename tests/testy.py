from source.priority_queue import PriorityQueue
import source.table as table
import numpy as np
from source.point import Point
import time
from source.A_algorithm import *


#testy w zależności od wielkości tablicy i ilości kart
"""
if __name__ == "__main__":
    f = open("testy.txt", "a")
    f.write("test N=5 ilosc kart=5 w zależności od punktu startowego:")
    f.write('\n')
    test_table = table.generate_table(N = 5)
    print(test_table)
    tim = []
    for i in range(5):
        tes = test_table
        start_time = time.time()
        res = algorithm(tes, 5, 1)
        print(table.get_result(tes, get_hidden_coords(res)))
        temp = time.time() - start_time
        tim.append(temp)
        f.write(str(temp))
        f.write('\n')
    print(str(sum(tim)/len(tim)))
    f.write("sredni czas: ")
    f.write(str(sum(tim)/len(tim)))
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.close()
"""

#testy w zależności od punktu startowego

if __name__ == "__main__":
    f = open("testy.txt", "a")
    f.write("test N=20 ilosc kart=20 w zależności od punktu startowego:")
    f.write('\n')
    test_table = table.generate_table(N = 20)
    print(test_table)
    negative_numbers = table.get_negative_values(test_table)
    for i in range(len(negative_numbers)):
        tes = test_table
        start_time = time.time()
        res = algorithm(tes, 20, i)
        print(table.get_result(tes, get_hidden_coords(res)))
        temp = time.time() - start_time
        f.write("liczba ujemna nr ")
        f.write(str(i))
        f.write(": ")
        f.write(str(temp))
        f.write('\n')
    f.write('\n')
    f.write('\n')
    f.close()
