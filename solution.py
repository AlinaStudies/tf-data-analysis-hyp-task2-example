import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 721973830

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.04
    _, _, pval = anderson_ksamp([x, y])
    return pval < alpha
