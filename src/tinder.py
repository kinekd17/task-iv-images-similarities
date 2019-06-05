import numpy as np


def get_matches(first_image_matrix, second_image_matrix):
    first_coords, first_features = first_image_matrix[:, :2], np.delete(first_image_matrix, [0, 1], 1)
    second_coords, second_features = second_image_matrix[:, :2], np.delete(second_image_matrix, [0, 1], 1)
    # input(first_coords)
    # input(first_features.shape)
    distances_matrix = np.zeros((first_features.shape[0], second_features.shape[0]))
    for i in range(first_features.shape[0]):
        for j in range(second_features.shape[0]):
            distance = np.sum(np.abs(first_features[i] - second_features[j]))
            distances_matrix[i, j] = distance

    print(distances_matrix)