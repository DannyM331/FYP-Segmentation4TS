import numpy as np
from Functions.metrics import f_measure, covering
from Algorithms.floss import floss

# In evaluate_floss.py
def evaluate_floss(dataset, routine, subject, sensor, sample_rate, cps, activities, ts, **seg_kwargs):
    profile, found_cps = floss(ts, 20*sample_rate, sample_rate, n_cps=len(cps), return_cac=True, **seg_kwargs)

    f1_score = f_measure({0: cps}, found_cps, margin=int(ts.shape[0] * .01))
    covering_score = covering({0: cps}, found_cps, ts.shape[0])

    # Return these values without converting to list since they are already lists
    return dataset, cps, found_cps, np.round(f1_score, 3), np.round(covering_score, 3), profile
