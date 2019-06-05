from src.loader import load_images_matrices
from src.tinder import get_matches, filter_pairs_by_reciprocity


if __name__ == '__main__':
    first_image, second_image = load_images_matrices('book')
    pairs = get_matches(first_image, second_image)
    print(pairs)
    print(len(pairs))
