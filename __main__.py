from src.loader import load_images_matrices
from src.tinder import get_matches
from src.pair_image_presenter import show_pairs
from src.life import neighbour_integrity_filter

IMAGES_EXTENSION = '.png'
IMAGES_DIR_PATH = 'images\\raw\\'


if __name__ == '__main__':
    object_name = 'book'
    first_image_matrix, second_image_matrix = load_images_matrices(object_name)
    pairs = get_matches(first_image_matrix, second_image_matrix)

    first_image_path = IMAGES_DIR_PATH + object_name + str(1) + IMAGES_EXTENSION
    second_image_path = IMAGES_DIR_PATH + object_name + str(2) + IMAGES_EXTENSION

    # show_pairs(first_image_path=first_image_path,
    #            second_image_path=second_image_path,
    #            pairs=pairs)

    pairs = neighbour_integrity_filter(pairs, 30, 10)

    show_pairs(first_image_path=first_image_path,
               second_image_path=second_image_path,
               pairs=pairs)
