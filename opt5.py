import matplotlib.pyplot as plt
names = ['Asthama', 'cancer','heart','skin','covid 19','liver']
values = [11,7,12,9,5,6]


plt.title('Patients Analysis',fontsize=14,color="blue")
plt.xticks( fontsize=14, rotation=30)
plt.bar(names, values,facecolor='r',edgecolor='red')

plt.show()
