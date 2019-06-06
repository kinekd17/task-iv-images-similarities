import numpy as np
from math import sqrt
from pprint import pprint


def get_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def neighbour_integrity_filter(pairs, neighbourhood_size, minimal):
    confirmed_pairs = []

    for pair in pairs:
        np_distances = np.zeros(len(pairs))
        np_distances2 = np.zeros(len(pairs))

        first_x1 = pair[0][0]
        first_y1 = pair[0][1]

        second_x1 = pair[1][0]
        second_y1 = pair[1][1]
        distances = []
        distances2 = []
        for i in range(np_distances.shape[0]):
            pair_to_compare = pairs[i]

            first_x2 = pair_to_compare[0][0]
            first_y2 = pair_to_compare[0][1]
            distance_first = get_distance(x1=first_x1, y1=first_y1, x2=first_x2, y2=first_y2)
            np_distances[i] = round(distance_first, 2)
            distances.append((round(distance_first, 2), pair_to_compare[0]))

            second_x2 = pair_to_compare[1][0]
            second_y2 = pair_to_compare[1][1]
            distance_second = get_distance(x1=second_x1, y1=second_y1, x2=second_x2, y2=second_y2)
            distances2.append((round(distance_second, 2), pair_to_compare[1]))
            np_distances2[i] = round(distance_second, 2)

        n_closest_to_first = np_distances.argsort()[2:neighbourhood_size+2]
        n_closest_to_second = np_distances2.argsort()[2:neighbourhood_size + 2]

        number_of_neighbours_confirmed = 0
        for first_pair_index in n_closest_to_first:
            for second_pair_index in n_closest_to_second:
                first_pair = pairs[first_pair_index]
                second_pair = pairs[second_pair_index]

                if first_pair[0][0] == second_pair[0][0] and first_pair[0][1] == second_pair[0][1]:
                    number_of_neighbours_confirmed += 1

        if number_of_neighbours_confirmed >= minimal:
            confirmed_pairs.append(pair)

    return confirmed_pairs