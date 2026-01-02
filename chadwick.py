from pybaseball import chadwick_register, cache
import pandas as pd

cache.enable()

data = chadwick_register()

pd.DataFrame(data).to_csv("chadwick_register.csv", index=False)

