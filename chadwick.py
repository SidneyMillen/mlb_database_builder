
"""Downloads the chadwick register into a csv file"""

from pybaseball import chadwick_register, cache
import pandas as pd

def main():
    cache.enable()
    data = chadwick_register()
    pd.DataFrame(data).to_csv("chadwick_register.csv", index=False)
    
if __name__ == "__main__":
    main()

