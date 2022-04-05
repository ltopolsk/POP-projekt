import numpy as np
import table


def naive_algorithm(num_table, m):

    hidden_items = []

    negative_values = table.get_negative_values(num_table)

    negative_values = sorted(negative_values, key=lambda item: item.get_value())
    k = 0
    max_used_cards = m if m <= 2 * num_table.shape[1] else 2 * num_table.shape[1]
    while k < len(negative_values) and len(hidden_items) < max_used_cards:
        forbidden_coords = negative_values[k].get_neighbors_pos()
        coord = negative_values[k].get_position()
        to_hide = True
        for item in forbidden_coords:
            if item in hidden_items:
                to_hide = False
                break
        if to_hide:
            hidden_items.append(coord)
        k += 1

    return hidden_items


if __name__ == "__main__":
    num_table = table.generate_table(N=10, seed=420)
    print(num_table)
    print(np.sum(num_table))
    hidden_items = naive_algorithm(m=15, num_table=num_table)
    res_table = table.get_result(num_table, hidden_items)
    print(res_table)
    print(np.sum(res_table))