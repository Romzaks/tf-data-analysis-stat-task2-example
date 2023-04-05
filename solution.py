import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 333357078 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x -= 0.038
    mean_x = x.mean()
    t = (x - mean_x)**2
    tt = t.mean()
    s = np.sqrt(tt)
    alpha = 1 - p
    l = 2 * x.mean() + 2 * s * norm.ppf(alpha / 2) / np.sqrt(len(x)) + 0.038
    r = 2 * x.mean() + 2 * s * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)) + 0.038
    return (l, r)
