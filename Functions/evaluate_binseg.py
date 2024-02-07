import numpy as np
from metrics import f_measure, covering
from Algorithms.binseg import binseg

def evaluate_binseg(dataset, ts, cps, **seg_kwargs):
    found_cps = binseg(ts, n_cps=len(cps), **seg_kwargs)

    f1_score = f_measure({0: cps}, found_cps, margin=int(ts.shape[0] * .01))
    covering_score = covering({0: cps}, found_cps, ts.shape[0])

    print(f"{dataset}: F1-Score: {np.round(f1_score, 3)}, Covering-Score: {np.round(covering_score, 3)}")
    # return dataset, cps, found_cps, np.round(f1_score, 3), np.round(covering_score, 3)