from src.loader import load_images_matrices
from src.tinder import get_matches
from src.pair_image_presenter import show_pairs
from src.life import neighbour_integrity_filter
from src.ransac import ransac_filter, get_best_model


IMAGES_EXTENSION = '.png'
IMAGES_DIR_PATH = 'images\\raw\\'

# NEIGHBOURHOOD INTEGRITY
NEIGHBOURHOOD_SIZE = 23
MINIMAL_INTEGRITY_POINT = 19

# RANSAC
MAX_ERROR = 100
TRANSFORMATION = 'perspective'
NUMBER_OF_ITERATIONS = 10000
RANSAC = True

if __name__ == '__main__':
    object_name = 'unicum'
    first_image_matrix, second_image_matrix = load_images_matrices(object_name)
    pairs = get_matches(first_image_matrix, second_image_matrix)

    print("Potential pairs:", len(pairs))
    first_image_path = IMAGES_DIR_PATH + object_name + str(1) + IMAGES_EXTENSION
    second_image_path = IMAGES_DIR_PATH + object_name + str(2) + IMAGES_EXTENSION

    if RANSAC:
        model = get_best_model(pairs=pairs,
                               transformation=TRANSFORMATION,
                               max_error=MAX_ERROR,
                               number_of_iterations=NUMBER_OF_ITERATIONS)

        pairs = ransac_filter(model=model,
                              pairs=pairs,
                              max_error=MAX_ERROR)
    else:
        pairs = neighbour_integrity_filter(pairs, NEIGHBOURHOOD_SIZE, MINIMAL_INTEGRITY_POINT)

    print("Confirmed pairs:", len(pairs))

    show_pairs(first_image_path=first_image_path,
               second_image_path=second_image_path,
               pairs=pairs)
