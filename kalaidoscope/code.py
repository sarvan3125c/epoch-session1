import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("moon.jpeg")

img_array = np.array(image)
m=len(img_array[0])
n=len(img_array)
for i in range(0,n):
    for j in range(0,m):
        if i<=n/2-1:
            if j>m/2-1:
                img_array[i][j]=img_array[i][m-j-1]
        else:
            if j<=m/2-1:
                img_array[i][j]=img_array[n-i-1][j]
            else:
                img_array[i][j]=img_array[n-i-1][m-j-1]
plt.imshow(img_array, cmap="gray")
plt.axis("off") 
plt.show()