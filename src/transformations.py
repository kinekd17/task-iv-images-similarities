import numpy as np
import random
import copy
from pprint import pprint

def get_affine_transformation(pairs):
    pairs = copy.deepcopy(pairs)
    random.shuffle(pairs)
    pairs = pairs[:3]
    # pprint(pairs)
    # pprint(pairs[0])
    # pprint(pairs[0][0])

    x1, y1 = pairs[0][0][0], pairs[0][0][1]
    x2, y2 = pairs[1][0][0], pairs[1][0][1]
    x3, y3 = pairs[2][0][0], pairs[2][0][1]

    u1, v1 = pairs[0][1][0], pairs[0][1][1]
    u2, v2 = pairs[1][1][0], pairs[1][1][1]
    u3, v3 = pairs[2][1][0], pairs[2][1][1]

    M = [[x1, y1,   1,  0,  0, 0],
         [x2, y2,   1,  0,  0, 0],
         [x3, y3,   1,  0,  0, 0],
         [0,   0,   0, x1, y1, 1],
         [0,   0,   0, x2, y2, 1],
         [0,   0,   0, x3, y3, 1]]


    N = [u1, u2, u3, v1, v2, v3]

    M = np.array(M)
    N = np.array(N)

    M = np.linalg.pinv(M)
    result_vector = np.dot(M, N)
    result_vector = np.append(result_vector, [0, 0, 1])

    affine_trans = result_vector.reshape(3, 3)
    return affine_trans


def get_perspective_transformation(pairs):
    pairs = copy.deepcopy(pairs)
    random.shuffle(pairs)
    pairs = pairs[:4]

    x1, y1 = pairs[0][0][0], pairs[0][0][1]
    x2, y2 = pairs[1][0][0], pairs[1][0][1]
    x3, y3 = pairs[2][0][0], pairs[2][0][1]
    x4, y4 = pairs[3][0][0], pairs[3][0][1]

    u1, v1 = pairs[0][1][0], pairs[0][1][1]
    u2, v2 = pairs[1][1][0], pairs[1][1][1]
    u3, v3 = pairs[2][1][0], pairs[2][1][1]
    u4, v4 = pairs[3][1][0], pairs[3][1][1]

    M = [[x1, y1, 1, 0, 0, 0, -u1*x1, -u1*y1],
         [x2, y2, 1, 0, 0, 0, -u2*x2, -u2*y2],
         [x3, y3, 1, 0, 0, 0, -u3*x3, -u3*y3],
         [x4, y4, 1, 0, 0, 0, -u4*x4, -u4*y4],
         [0, 0, 0, x1, y1, 1, -v1*x1, -v1*y1],
         [0, 0, 0, x2, y2, 1, -v2*x2, -v2*y2],
         [0, 0, 0, x3, y3, 1, -v3*x3, -v3*y3],
         [0, 0, 0, x4, y4, 1, -v4*x4, -v4*y4]]


    N = [u1, u2, u3, u4, v1, v2, v3, v4]

    M = np.linalg.pinv(np.array(M))
    N = np.array(N)

    result_vector = np.dot(M, N)
    result_vector = np.append(result_vector, [1])

    return result_vector.reshape(3, 3)
