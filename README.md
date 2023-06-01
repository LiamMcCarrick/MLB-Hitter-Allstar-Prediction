# MLB-Hitter-Allstar-Prediction
Predicting MLB position player all stars

## Code and Resources

**Python Version:** 3.9.7           
**Textbook:**           
Data Mining for Business Analytics: Concepts, Techniques and Applications in Python
Book by Galit Shmueli, Nitin R. Patel, and Peter C. Bruce           
**Inspiration:**            
https://towardsdatascience.com/using-machine-learning-to-predict-nba-all-stars-part-1-data-collection-9fb94d386530          
**Documentation**           
https://github.com/jldbc/pybaseball

## Data Cleaning/Preprocessing

<ins>All Star Roster Data</ins>
1. Replace Special Characters
2. Pull Pitchers with a min of 20 innings pitched to catch relievers using pybaseball
3. Use VLOOKUP in Excel to match pitchers and remove from dataset

<ins>First Half Hitting Stats Data</ins>
1. Replace Special Characters
2. Get league for each player of the 2021 season
    1. Pull hitters with a min of 50 PAs to using pybaseball to get teams for each player
    2. Get list of each team in AL and NL
    3. Use IF formula in Excel to assign each players league
    4. Use VLOOKUP to match league to player in first half data
3. Add all star colum to 2000-19 and 21 data
    1. Delimite each player to remove jr/sr/etc
    2. Create concat key with year and name to get unique player season
    3. Use VLOOKUP to match AS to first half data