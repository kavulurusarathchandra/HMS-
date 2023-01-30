import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('piechart.csv')
name = df["NAME"]
num = df["Num"]
plt.pie(num, labels=name,  
autopct='%1.1f%%')
plt.show()








