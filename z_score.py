import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
data = pd.read_csv("modified_air_quality.csv")

mean_aqi_log = data["aqi_log"].mean()
std_aqi_log = data["aqi_log"].std()


lower_limit_1 = mean_aqi_log - 3 * std_aqi_log
upper_limit_1 = mean_aqi_log + 3 * std_aqi_log


data["z_score"] = stats.zscore(data["aqi_log"], ddof=1)
data[(data["z_score"] > 3) | (data["z_score"] < -3)]
