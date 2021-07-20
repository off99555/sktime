# -*- coding: utf-8 -*-
import numpy as np
from numpy import testing
from sklearn.ensemble import RandomForestClassifier

from sktime.classification.feature_based import MatrixProfileClassifier
from sktime.datasets import load_gunpoint, load_italy_power_demand


def test_matrix_profile_classifier_on_gunpoint():
    # load gunpoint data
    X_train, y_train = load_gunpoint(split="train", return_X_y=True)
    X_test, y_test = load_gunpoint(split="test", return_X_y=True)
    indices = np.random.RandomState(0).permutation(10)

    # train matrix profile classifier
    rf = RandomForestClassifier(n_estimators=20)
    mpc = MatrixProfileClassifier(random_state=0, estimator=rf)
    mpc.fit(X_train.iloc[indices], y_train[indices])

    # assert probabilities are the same
    probas = mpc.predict_proba(X_test.iloc[indices])
    testing.assert_array_equal(probas, matrix_profile_classifier_gunpoint_probas)


def test_matrix_profile_classifier_on_power_demand():
    # load power demand data
    X_train, y_train = load_italy_power_demand(split="train", return_X_y=True)
    X_test, y_test = load_italy_power_demand(split="test", return_X_y=True)
    indices = np.random.RandomState(0).permutation(100)

    # train TSFresh classifier
    rf = RandomForestClassifier(n_estimators=20)
    mpc = MatrixProfileClassifier(random_state=0, estimator=rf)
    mpc.fit(X_train, y_train)

    score = mpc.score(X_test.iloc[indices], y_test[indices])
    assert score >= 0.9


matrix_profile_classifier_gunpoint_probas = np.array(
    [
        [
            0.35,
            0.65,
        ],
        [
            0.45,
            0.55,
        ],
        [
            0.8,
            0.2,
        ],
        [
            0.4,
            0.6,
        ],
        [
            0.35,
            0.65,
        ],
        [
            0.55,
            0.45,
        ],
        [
            0.25,
            0.75,
        ],
        [
            0.5,
            0.5,
        ],
        [
            0.6,
            0.4,
        ],
        [
            0.6,
            0.4,
        ],
    ]
)


# def print_array(array):
#     print('[')
#     for sub_array in array:
#         print('[')
#         for value in sub_array:
#             print(value.astype(str), end='')
#             print(', ')
#         print('],')
#     print(']')
#
# if __name__ == "__main__":
#     X_train, y_train = load_gunpoint(split="train", return_X_y=True)
#     X_test, y_test = load_gunpoint(split="test", return_X_y=True)
#     indices = np.random.RandomState(0).permutation(10)
#
#     rf = RandomForestClassifier(n_estimators=20)
#     mpc = MatrixProfileClassifier(random_state=0, estimator=rf)
#
#     mpc.fit(X_train.iloc[indices], y_train[indices])
#     probas = mpc.predict_proba(X_test.iloc[indices])
#     print_array(probas)
