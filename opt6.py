import pandas as pd
import matplotlib.pyplot as plt
print('line plot')
df=pd.read_csv("hbill.csv")
x1=df['medicines']
y1=df['room']
plt.xlabel('medicines')
plt.ylabel('room')
plt.plot(x1,y1)
plt.title('charges of medicines and room records')
plt.show()
