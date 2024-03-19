import numpy as np
from Functions.metrics import f_measure, covering
from Algorithms.binseg import binseg

def evaluate_binseg(dataset, ts, cps, **seg_kwargs):
    try:
        found_cps = binseg(ts, n_cps=len(cps), **seg_kwargs)
        # print("Found CPS:", found_cps)  # Debug print

        f1_score = f_measure({0: cps}, found_cps, margin=int(ts.shape[0] * .01))
        covering_score = covering({0: cps}, found_cps, ts.shape[0])

        # print("F1 Score:", f1_score)  # Debug print
        # print("Covering Score:", covering_score)  # Debug print

        return dataset, cps, found_cps, np.round(f1_score, 3), np.round(covering_score, 3)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise