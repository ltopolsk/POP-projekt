from priority_queue import PriorityQueue
import table


def gain_function(negative_numbers, binary_vector):
    hidden_items = get_hidden_items(negative_numbers, binary_vector)
    return sum(abs(item.get_value()) for item in hidden_items)


def heuristic_function(binary_vector, negative_values, used_cards, max_cards):
    hidden_items = get_hidden_items(negative_values, binary_vector)
    negative_numbers_sorted = sorted(negative_values.copy(), key=lambda item: item.get_value(), reverse=False)
    for k in range(len(binary_vector)):
        negative_numbers_sorted.remove(negative_values[k])
    value_sum = 0
    i = 0
    j = 0
    while i < max_cards - used_cards and j < len(negative_numbers_sorted):
        if can_be_hidden(negative_numbers_sorted[j], hidden_items):
            value_sum += abs(negative_numbers_sorted[j].get_value())
            i += 1
        j += 1
    return value_sum


def get_hidden_items(negative_values, binary_vector):
    hidden_items = []
    for i in range(len(binary_vector)):
        if binary_vector[i] == 1:
            hidden_items.append(negative_values[i])
    return hidden_items


def can_be_hidden(item, hidden_items):
    neighbours = item.get_neighbors_pos()
    for position in neighbours:
        if not (None in position):
            for hidden in hidden_items:
                if position == hidden.get_position():
                    return False
    return True


def change_positions(start_index, arr):
    new_arr = []
    i = start_index
    for _ in range(len(arr)):
        new_arr.append(arr[i % len(arr)])
        i += 1
    return new_arr


def algorithm(num_table, available_cards, first_index):
    negative_numbers = table.get_negative_values(num_table)
    negative_numbers = change_positions(first_index, negative_numbers)
    max_cards = available_cards if available_cards <= 2 * num_table.shape[1] else 2 * num_table.shape[1]
    start_state = []
    queue = PriorityQueue()
    start_state_value = heuristic_function(start_state, negative_numbers, 0, max_cards)
    queue.put((start_state_value, start_state))
    to_ret = []
    while not queue.empty():
        current_vector = queue.get()

        if len(current_vector) == len(negative_numbers):
            to_ret = current_vector
            break

        hidden_items = get_hidden_items(negative_numbers, current_vector)

        if can_be_hidden(negative_numbers[len(current_vector)], hidden_items) and sum(current_vector) < max_cards:

            # first case
            first_case_vector = current_vector.copy()
            first_case_vector.append(0)
            first_case_f = gain_function(negative_numbers, first_case_vector) + \
                           heuristic_function(first_case_vector, negative_numbers, sum(first_case_vector), max_cards)
            queue.put((first_case_f, first_case_vector))

            # second_case
            second_case_vector = current_vector.copy()
            second_case_vector.append(1)
            second_case_f = gain_function(negative_numbers, second_case_vector) + \
                            heuristic_function(second_case_vector, negative_numbers, sum(second_case_vector), max_cards)
            queue.put((second_case_f, second_case_vector))

        else:
            current_vector.append(0)
            sum_f = gain_function(negative_numbers, current_vector) + \
                           heuristic_function(current_vector, negative_numbers, sum(current_vector), max_cards)
            queue.put((sum_f, current_vector))

    hidden_items_to_ret = get_hidden_items(negative_numbers, to_ret)
    return hidden_items_to_ret


def get_hidden_coords(hidden_items):
    hidden_cords = []
    for i in range(len(hidden_items)):
        if hidden_items[i] is not None:
            hidden_cords.append(hidden_items[i].get_position())
    return hidden_cords


if __name__ == "__main__":
    test_table = table.generate_table(N=4, seed=100)
    print(test_table)
    res = algorithm(test_table, 8, 0)
    print(table.get_result(test_table, get_hidden_coords(res)))