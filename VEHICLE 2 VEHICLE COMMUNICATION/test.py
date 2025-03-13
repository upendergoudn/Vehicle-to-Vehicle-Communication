import pandas as pd
import numpy as np

dataset = pd.read_csv("Dataset/train.csv", usecols=['x', 'y', 'direction', 'congestion'], nrows = 48204)

weather = pd.read_csv("Dataset/Metro_Interstate_Traffic_Volume.csv", usecols=['temp','rain_1h','snow_1h','clouds_all','weather_main','weather_description','date_time'])

weather['x'] = dataset['x'].ravel()
weather['y'] = dataset['y'].ravel()
weather['direction'] = dataset['direction'].ravel()
weather['congestion'] = dataset['congestion'].ravel()

print(weather)

weather.to_csv("Dataset/traffic_data.csv", index=False)
