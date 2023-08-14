import numpy as np
from sklearn.metrics import log_loss


def balanced_log_loss(y_true, y_pred):
    # Copied from Chris Deotte's post
    # https://www.kaggle.com/competitions/icr-identify-age-related-conditions/discussion/422442#2348779

    nc = np.bincount(y_true)
    return log_loss(y_true, y_pred, sample_weight=1 / nc[y_true], eps=1e-15)
