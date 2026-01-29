from pybaseball import chadwick_register, cache
import pandas as pd

cache.enable()

data = pd.DataFrame(chadwick_register())

data = data[data['key_mlbam'] != -1]

data.to_csv("chadwick_register.csv", index=False)

