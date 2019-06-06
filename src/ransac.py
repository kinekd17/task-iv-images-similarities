import numpy as np
from src.transformations import get_affine_transformation, get_perspective_transformation


AFFINE_TRANSFORMATION = 'affine'


def ransac_filter(model, pairs, max_error):
    confirmed_pairs = []
    for pair in pairs:
        error = get_model_error(model, pair)
        if error < max_error:
            confirmed_pairs.append(pair)
    return confirmed_pairs


def get_best_model(pairs, number_of_iterations, transformation, max_error):
    best_model = None
    best_score = 0

    for i in range(number_of_iterations):

        if transformation is AFFINE_TRANSFORMATION:
            model = get_affine_transformation(pairs=pairs)
        else:
            model = get_perspective_transformation(pairs=pairs)

        score = 0
        for pair in pairs:
            error = get_model_error(model=model,
                                    pair=pair)
            if error < max_error:
                score += 1

        if score > best_score:
            best_score = score
            best_model = model

    return best_model


def get_model_error(model, pair):
    x = pair[0][0]
    y = pair[0][1]
    u = pair[1][0]
    v = pair[1][1]

    transformation = model.dot(np.array([x, y, 1]))
    u_transformed, v_transformed = transformation[0], transformation[1]

    a = np.array([u, v])
    b = np.array(u_transformed, v_transformed)

    model_error = np.linalg.norm(a - b)
    return model_error
