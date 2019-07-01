import matplotlib.pyplot as plt

someList = [blob.polarity]
plt.hist(someList, bins=[-1,-0.8, -0.5, 0.0, 0.5, 0.8, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1,1.1,0,50])
plt.grid(False)
plt.show()