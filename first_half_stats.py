# selecting first half stats
import pandas as pd
from pybaseball import pitching_stats

df = pitching_stats(2000, 2019)
df2 = df[df["Name"] == "Madison Bumgarner"]
print(df2)
