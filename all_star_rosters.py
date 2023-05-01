# import packages
import pandas as pd
from pybaseball.lahman import *
from pybaseball import playerid_reverse_lookup

# download lahman database
download_lahman()

# import all star roster data
allstar = all_star_full()

# only choose all stars since 2000
allstar_filtered = allstar[allstar["yearID"] >= 2000]

# get full player names instead of player IDs
player_ID = allstar_filtered["playerID"]
allstar_filtered.rename(columns={"playerID": "key_bbref"}, inplace=True)
player_name = playerid_reverse_lookup(player_ID, key_type="bbref")
allstar_key = player_name[["key_bbref", "name_last", "name_first"]]

# join full names with filtered all star dataset
merged_allstars = pd.merge(allstar_filtered, allstar_key, on="key_bbref", how="left")

merged_allstars.to_csv("allstars.csv")
