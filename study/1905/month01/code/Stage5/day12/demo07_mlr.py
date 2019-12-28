"""
demo07_mlr.py   逻辑分类解决多元逻辑分类问题
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
x = np.array([
    [4, 7],
    [3.5, 8],
    [3.1, 6.2],
    [0.5, 1],
    [1, 2],
    [1.2, 1.9],
    [6, 2],
    [5.7, 1.5],
    [5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])

# 通过8个样本点，训练分类器
import sklearn.linear_model as lm
model = lm.LogisticRegression(solver='liblinear',C=1)
model.fit(x,y)
# 测试模型，预测新样本
r = model.predict([[3,9],[6,1]])
print(r)


# 绘制分类边界线
l,r = x[:,0].min()-1,x[:,0].max()+1
b,t = x[:,].min()-1,x[:,1].max()+1
# 把可视区间划分为500*500
n = 500
grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))
# 模拟使用模型，得到点阵中每个坐标的类别
mesh_x = np.column_stack((grid_x.ravel(),grid_y.ravel()))
mesh_z = model.predict(mesh_x)
grid_z = mesh_z.reshape(grid_x.shape)
# 画图
mp.figure('LR Classification',facecolor='lightgray')
mp.title('LR Classification',fontsize=16)
mp.scatter(x[:,0],x[:,1],c=y,cmap='jet',label='Sample Points',s=70,zorder=3)
# 调用mp.pcolormesh()绘制分类边界线
# 根据参数，把可视区间拆分成坐标网格，由于每个网格都有相应的类别，可以使用cmap为每个网格填充颜色
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.legend()
mp.show()