import pandas as pd
import numpy as np

from scipy.stats import norm, t


chat_id = 333357078 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    x -= 0.038
    xmax = np.max(x)
    n = len(x)
    l = 0.038 + xmax
    r = 0.038 + xmax / alpha**(1/n)
    return (l, r)
