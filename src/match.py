import numpy as np
from true_points import TruePoint
from src.estimated_point import EstimatePoint
import sys
sys.path.append("utils")
from utils import utils


def get_match_possibility(estimated_point: EstimatePoint, true_point: TruePoint):

    if not estimated_point.isTimeDiffValid(true_point):
        return 0
    else:
        normalized_point = utils.to_standard_normal_distribution_point(true_point.x,
                                                                       true_point.y, estimated_point.x,
                                                                       estimated_point.y,
                                                                       estimated_point.major, estimated_point.minor)
        distance = np.sqrt((normalized_point[0] ** 2) + (normalized_point[1] ** 2))
        if (distance / utils.chi_stv) > 5:
            return 0
        else:
            return utils.chi_distribution_density_function(distance)


def matches():
    true_points = utils.get_all_true_points()
    estimated_points = utils.get_all_estimated_points()

    for estimated_point in estimated_points:
        estimated_point_matches = []
        possibility_sum = 0
        for true_point in true_points:
            possibility = get_match_possibility(estimated_point, true_point)
            estimated_point_matches.append(possibility)
            possibility_sum += possibility
        if not possibility_sum == 0:
            for index in range(0, len(estimated_point_matches)):
                estimated_point_matches[index] /= possibility_sum
                estimated_point_matches[index] = [index+1,estimated_point_matches[index]]

        print(f'estimated point {estimated_point.point_id}:{estimated_point_matches}')
