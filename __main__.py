from src.loader import load_images_matrices
from src.tinder import get_matches
from src.pair_image_presenter import show_pairs
from src.life import neighbour_integrity_filter
from src.ransac import ransac_filter, get_best_model


IMAGES_EXTENSION = '.png'
IMAGES_DIR_PATH = 'images\\raw\\'
# RANSAC
MAX_ERROR = 0.9
TRANSFORMATION = 'affine'
NUMBER_OF_ITERATIONS = 100


if __name__ == '__main__':
    object_name = 'book'
    first_image_matrix, second_image_matrix = load_images_matrices(object_name)
    pairs = get_matches(first_image_matrix, second_image_matrix)

    first_image_path = IMAGES_DIR_PATH + object_name + str(1) + IMAGES_EXTENSION
    second_image_path = IMAGES_DIR_PATH + object_name + str(2) + IMAGES_EXTENSION

    # show_pairs(first_image_path=first_image_path,
    #            second_image_path=second_image_path,
    #            pairs=pairs)

    # pairs = neighbour_integrity_filter(pairs, 30, 10)
    model = get_best_model(pairs=pairs,
                           transformation=TRANSFORMATION,
                           max_error=MAX_ERROR,
                           number_of_iterations=NUMBER_OF_ITERATIONS)

    pairs = ransac_filter(model=model,
                          pairs=pairs,
                          max_error=MAX_ERROR)

    show_pairs(first_image_path=first_image_path,
               second_image_path=second_image_path,
               pairs=pairs)
