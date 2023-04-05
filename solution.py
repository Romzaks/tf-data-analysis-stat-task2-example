import pandas as pd
import numpy as np

from scipy.stats import norm, t


chat_id = 333357078 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    mean_x = x.mean()
    tp = (x - mean_x)**2
    tt = tp.mean()
    s = np.sqrt(tt)
    s /= np.sqrt(len(x) - 1)
    b_t = 2 * mean_x - 0.038
    l = b_t - t.ppf(1 - alpha / 2, len(x) - 1) * s / np.sqrt(len(x))
    r = b_t + t.ppf(1 - alpha / 2, len(x) - 1) * s / np.sqrt(len(x))
    return (l, r)
