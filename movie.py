from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv(r"C:\Users\ACER\Downloads\next_bechdel\bechdelExpanded.csv")
#print(df.head(10)) --- test 1
#print(df.info()) --- test 2
df["total_score"] = df["bechdel"]+df["waithe"]+df["ko"]
#print(df.head(10)) --- test 3
df_sorted = df.sort_values("total_score").reset_index(drop = True)
#print(df_sorted.head(10)) --- test 4
df2 = df_sorted[[ 'movie', 'bechdel', 'waithe', 'ko', 'total_score' ]]
#print(df2.head()) -- test 5 
ax = df2[["movie" , "total_score"]].set_index("movie")
ax.plot(kind='bar', title ='Representation In Movies', figsize=(15, 10), legend=True)
ax = df_sorted[["movie", "total_score"]].set_index('movie').plot(kind='barh', title ="V comp", figsize=(45, 20), legend=True, fontsize=12)
plt.show()
