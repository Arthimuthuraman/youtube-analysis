import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
INPUT_CSV = "INvideos.csv"  
OUTPUT_PLOT="title vs views.png"
df = pd.read_csv(INPUT_CSV, encoding='utf-8')  
print(f"Loaded {len(df)} rows")
print(df.tail)

plt.figure(figsize=(8,6))
sns.scatterplot(x='title', y='views', data=df.sample(min(2000,len(df))), alpha=0.3)
plt.yscale('log')  
plt.xlabel("title (characters)")
plt.ylabel("views (log scale)")
plt.title("Title vs Views")
plt.tight_layout()
plt.savefig(OUTPUT_PLOT)
plt.show()


