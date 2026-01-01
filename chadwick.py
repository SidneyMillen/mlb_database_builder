from pybaseball import chadwick_register, cache

# get the register data and save to disk
data = chadwick_register(save=True)

print(cache.contents().cache_directory)
