import time
from source.A_algorithm import *
from source.naive_algorithm import *


if __name__ == "__main__":
    num_cards = (
        5,
        10,
        20,
        40
    )
    shapes = (
        10,
        20
    )
    with open("testy_wyników.txt", "a") as res_file:
        for N in shapes:
            for num_card in num_cards:
                test_table = table.generate_table(N=N, seed=420)
                cards = num_card
                res_file.write(f"wyniki algorytmów dla N={N} liczba kart={num_card}:\n")
                negative_numbers = table.get_negative_values(test_table)
                set = range(1) if N == 20 and num_card == 40 else range(len(negative_numbers))
                for i in set:
                    start_time = time.time()
                    res = algorithm(test_table, num_card, i)
                    exec_time = time.time() - start_time
                    res_table = table.get_result(test_table, get_hidden_coords(res))
                    res_file.write(f"algorytm A* dla liczby ujemnej nr {i}: {np.sum(res_table)},  czas wykonania: {exec_time:.2f}\n")
                res_file.write('\n')
                naive_start_time = time.time()
                hidden_items = naive_algorithm(m=num_card, num_table=test_table)
                naive_exec_time = time.time() - naive_start_time
                res_table = table.get_result(test_table, hidden_items)
                res_file.write(f"algorytm naiwny: {np.sum(res_table)}, czas wykonania: {naive_exec_time:.2f}\n\n\n")

