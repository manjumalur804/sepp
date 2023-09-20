import numpy as np
import matplotlib.pyplot as plt
LAPTOPS=["HP","DELL","LENOVO","ACER"]
SALES=[700,600,500,400]
c=("silver","black","blue","violet")
plt.bar(LAPTOPS,SALES,color=c,width=0.5)
plt.xlabel("LAPTOPS")
plt.ylabel("SALES")
plt.title("BAR GRAPH")
plt.show()
