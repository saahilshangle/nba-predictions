from data import *
import pandas as pd

stats = pd.DataFrame(player_stats, columns = headers)
print(stats.head(10))
