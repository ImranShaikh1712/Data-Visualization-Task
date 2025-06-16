import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Player': ['Virat Kohli', 'Shubman Gill', 'Ruturaj Gaikwad', 'Rohit Sharma', 'Sanju Samson',
               'Rinku Singh', 'David Warner', 'Faf du Plessis', 'KL Rahul', 'Heinrich Klaasen'],
    'Matches': [14]*10,
    'Runs': [741, 702, 690, 665, 640, 620, 610, 605, 590, 580],
    'Average': [61.75, 58.5, 57.5, 55.4, 53.3, 51.6, 50.8, 50.4, 49.1, 48.3],
    'Strike Rate': [147.2, 142.1, 139.7, 148.3, 152.6, 156.2, 144.7, 141.3, 135.9, 160.4],
    '100s': [3, 2, 2, 1, 1, 1, 1, 0, 0, 1],
    '50s': [5, 4, 4, 5, 5, 4, 3, 5, 4, 2],
    'Team': ['RCB', 'GT', 'CSK', 'MI', 'RR', 'KKR', 'DC', 'RCB', 'LSG', 'SRH']
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")
colors = sns.color_palette("coolwarm", len(df))

bars = plt.barh(df['Player'], df['Runs'], color=colors)

for index, bar in enumerate(bars):
    avg = df['Average'][index]
    sr = df['Strike Rate'][index]
    plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f"Avg: {avg:.1f}, SR: {sr:.1f}", va='center', fontsize=10, fontweight='bold')

plt.title('🏏 IPL 2024 – Top 10 Batsmen Performance', fontsize=16, fontweight='bold', color='darkgreen')
plt.xlabel('Runs Scored', fontsize=12)
plt.ylabel('Players', fontsize=12)
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
