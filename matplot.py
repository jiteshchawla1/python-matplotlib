import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[4,5,6]
plt.plot(x1,y1,label="first line")
x2=[5,8,9]
y2=[2,3,1]
plt.plot(x2,y2,label="second line")
plt.xlabel("plot number ")
plt.ylabel("new variables")
plt.legend()
plt.show()
