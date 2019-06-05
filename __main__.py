from src.loader import load_images_matrices
from src.tinder import get_matches

if __name__ == '__main__':
    first_image, second_image = load_images_matrices('book')
    # print(first_image.shape)
    # input(first_image)
    #
    # print(second_image.shape)
    # input(second_image)

    get_matches(first_image, second_image)
