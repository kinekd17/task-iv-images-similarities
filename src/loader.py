import sys
import numpy as np

IMAGE_EXTENSION = '.png.haraff.sift'


def load_image_matrix(image_name:str):
    file_path = 'images\\extracted\\' + image_name + IMAGE_EXTENSION
    np_image_matrix = np.genfromtxt(file_path)
    # print(np_image.shape)
    # print(np_image)
    # input()
    np_image_matrix = np.delete(np_image_matrix, [2, 3, 4], 1)
    # print(np_image.shape)
    # print(np_image)

    return np_image_matrix


def load_images_matrices(object_name):
    return load_image_matrix(object_name + str(1)), load_image_matrix(object_name + str(2))


if __name__ == "__main__":
    load_image_matrix("bass1")
