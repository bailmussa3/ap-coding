from helperFunctions import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# 1) Using an existing stats dataframe:
stats = weeklyPlayerStats(2024, "QB,WR,RB", week=None) 
plot_player_stat(stats, stat="touchdowns", top_n=20, title="QB Passing Yards (2024)", save_path="qb_passing_yards_2024.png"  )

# 2) One-liner wrapper:
# plot_weekly_player_stats(2024, "WR", stat="receiving_yards", top_n=15, week=[1,2,3], save_path="wr_rec_yards_wk1-3.png")

# Use the new plot_player_stat() and plot_weekly_player_stats() to visualize the data into bar graphs and answer the following questions.
# 1. Metric chosen
metric_description = "I chose to visualize total touchdowns (passing + rushing) for top quarterbacks using the helper functions plot_player_stat() and plot_weekly_player_stats()."

# 2. Player(s) with most touchdowns in 2024
most_touchdowns = "Two players tied for the most total touchdowns (passing and rushing) in the 2024 season: Lamar Jackson (45 total: 41 passing, 4 rushing) and Joe Burrow (45 total: 43 passing, 2 rushing)."

# 3. Player with highest total passing yards in 2024
most_passing_yards = "The player with the highest total passing yards in the 2024 season was Joe Burrow of the Cincinnati Bengals, with 4,918 passing yards."

# 4. Player(s) with highest rushing yards in Week 1 and Week 17
highest_rushing_yards = "Week 1: Joe Mixon of the Houston Texans had the most rushing yards in Week 1 with 159 yards against the Colts. Lamar Jackson was a close second with 122 rushing yards. Week 17: Saquon Barkley of the Philadelphia Eagles had the most rushing yards in Week 17 with 167 yards against the Cowboys."



