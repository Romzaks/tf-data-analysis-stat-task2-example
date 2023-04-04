import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 333357078 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p = 1 - p
    a = (1 - p) / 2
    b = 1 - a
    x -= 0.038
    mn = np.min(x)
    mx = np.max(x)
    q = (mn + mx) / 2
    l = 0.038 + q / (1 - a)
    r = 0.038 + q / (1 - b)
    return (l, r)
