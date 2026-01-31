import pandas as pd
import numpy as np

df = pd.read_csv("deliveries.csv")


# Question 1: Data Loading & Initial Exploration


print("\n===== Question 1: Data Exploration =====")

print("\nFirst 15 rows:")
print(df.head(15))

print("\nTotal Rows (Deliveries):", df.shape[0])
print("Total Columns (Attributes):", df.shape[1])

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


# Question 2: Batting Analysis – Top Run Scorers


print("\n===== Question 2: Batting Analysis =====")

# Total runs by batter
runs_by_batter = df.groupby("batter")["batsman_runs"].sum()

top15_batters = runs_by_batter.sort_values(ascending=False).head(15)

# Balls faced by these batters
balls_faced = df[df["batter"].isin(top15_batters.index)] \
                .groupby("batter").size()

batting_analysis = pd.DataFrame({
    "Total Runs": top15_batters,
    "Balls Faced": balls_faced
})

batting_analysis["Strike Rate"] = (
    batting_analysis["Total Runs"] /
    batting_analysis["Balls Faced"]
) * 100

batting_analysis = batting_analysis.sort_values(
    "Total Runs", ascending=False
)

print(batting_analysis)

# Question 3: Bowling Analysis – Wicket Takers


print("\n===== Question 3: Bowling Analysis =====")

# Wickets taken
wicket_deliveries = df[df["is_wicket"] == 1]

wickets_by_bowler = wicket_deliveries.groupby("bowler") \
                        .size() \
                        .sort_values(ascending=False) \
                        .head(10)

# Runs conceded
runs_conceded = df[df["bowler"].isin(wickets_by_bowler.index)] \
                    .groupby("bowler")["total_runs"].sum()

bowling_analysis = pd.DataFrame({
    "Wickets": wickets_by_bowler,
    "Runs Conceded": runs_conceded
})

bowling_analysis["Bowling Average"] = (
    bowling_analysis["Runs Conceded"] /
    bowling_analysis["Wickets"]
)

bowling_analysis = bowling_analysis.sort_values(
    "Wickets", ascending=False
)

print(bowling_analysis)


# Question 4: Team Performance Analysis

print("\n===== Question 4: Team Performance =====")

# 1. KKR bowling vs RCB wickets
kkr_vs_rcb_wickets = df[
    (df["bowling_team"] == "Kolkata Knight Riders") &
    (df["batting_team"] == "Royal Challengers Bangalore") &
    (df["is_wicket"] == 1)
]

print("\nKKR wickets vs RCB:", kkr_vs_rcb_wickets.shape[0])
print(kkr_vs_rcb_wickets.head(10))

# 2. Boundaries against Mumbai Indians
mi_boundaries = df[
    (df["bowling_team"] == "Mumbai Indians") &
    (df["batsman_runs"].isin([4, 6]))
]

print("\nBoundaries conceded by MI:", mi_boundaries.shape[0])
print(mi_boundaries.head(10))

# 3. Deliveries with extras
extras_deliveries = df[df["extra_runs"] > 0]

print("\nDeliveries with Extras:", extras_deliveries.shape[0])
print(extras_deliveries.head(10))

# Question 5: Match-Specific Deep Dive
# match_id = 335982

print("\n===== Question 5: Match Deep Dive =====")

match_df = df[df["match_id"] == 335982]

# Inning-wise total runs
inning_runs = match_df.groupby("inning")["total_runs"].sum()
print("\nInning-wise Runs:")
print(inning_runs)

# Top 3 batters per inning
print("\nTop 3 Batters per Inning:")
for inn in match_df["inning"].unique():
    top_batters = (
        match_df[match_df["inning"] == inn]
        .groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )
    print(f"\nInning {inn}")
    print(top_batters)

# Best bowler in the match
best_bowler = (
    match_df[match_df["is_wicket"] == 1]
    .groupby("bowler")
    .size()
    .sort_values(ascending=False)
    .head(1)
)

print("\nBest Bowler of the Match:")
print(best_bowler)

# Extras per inning
extras_by_inning = match_df.groupby("inning")["extra_runs"].sum()
print("\nExtras per Inning:")
print(extras_by_inning)


# Bonus Question: Powerplay Analysis (Overs 1–6)
print("\n===== Bonus: Powerplay Analysis =====")

powerplay = df[(df["over"] >= 1) & (df["over"] <= 6)]

# Total powerplay runs
print("\nTotal Powerplay Runs:", powerplay["total_runs"].sum())

# Top powerplay batter
top_pp_batter = powerplay.groupby("batter")["batsman_runs"].sum().idxmax()
print("Top Powerplay Batter:", top_pp_batter)

# Economy rate (runs per over)
bowler_runs_pp = powerplay.groupby("bowler")["total_runs"].sum()
bowler_overs_pp = powerplay.groupby("bowler")["over"].nunique()

economy_rate = (bowler_runs_pp / bowler_overs_pp).sort_values()
print("Most Economical Bowler in Powerplay:")
print(economy_rate.head(1))

# Powerplay wickets
pp_wickets = powerplay["is_wicket"].sum()
print("Total Powerplay Wickets:", pp_wickets)





