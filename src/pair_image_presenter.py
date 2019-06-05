from PIL import Image
import matplotlib.pyplot as plt


def show_pairs(first_image_path, second_image_path, pairs):
    first_image, second_image = Image.open(first_image_path), Image.open(second_image_path)
    new_image_height = first_image.size[1]
    new_image_width = first_image.size[0] + second_image.size[0]

    new_image = Image.new('RGB',
                          (new_image_width, new_image_height),
                          color=(255, 255, 255))

    new_image.paste(first_image, (0, 0))
    new_image.paste(second_image, (first_image.size[0], 0))
    plt.clf()

    for pair in pairs:

        plt.plot([pair[0][0], pair[1][0] + first_image.size[0]],
                 [pair[0][1], pair[1][1]],
                 '#FFFF00')

    plt.axis('off')
    plt.imshow(new_image)
    plt.show()
