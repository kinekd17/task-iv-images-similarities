import numpy as np


def get_matches(first_image_matrix, second_image_matrix):
    first_coords, first_features = first_image_matrix[:, :2], np.delete(first_image_matrix, [0, 1], 1)
    second_coords, second_features = second_image_matrix[:, :2], np.delete(second_image_matrix, [0, 1], 1)

    distances_matrix = np.zeros((first_features.shape[0], second_features.shape[0]))
    for i in range(first_features.shape[0]):
        for j in range(second_features.shape[0]):
            distance = np.sum(np.abs(first_features[i] - second_features[j]))
            distances_matrix[i, j] = distance
    pairs = []

    for key_point_index in range(distances_matrix.shape[0]):
        pair = key_point_index, np.argmin(distances_matrix[key_point_index])
        pairs.append(pair)

    pairs = filter_pairs_by_reciprocity(pairs, distances_matrix)

    key_points_pairs = []
    for pair in pairs:
        first_point_index, second_point_index = pair[0], pair[1]
        key_points_pair = first_coords[first_point_index], second_coords[second_point_index]
        key_points_pairs.append(key_points_pair)

    return key_points_pairs


def filter_pairs_by_reciprocity(pairs, distance_matrix):
    pairs = [pair for pair in pairs if np.argmin(distance_matrix[:, pair[1]]) == pair[0]]
    return pairs
