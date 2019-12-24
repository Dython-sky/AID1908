"""
demo03_figure.py 测试mp窗口
"""
import matplotlib.pyplot as mp

mp.figure('A Figure',facecolor='gray')
mp.plot([0,1],[1,2])
mp.figure('B Figure',facecolor='lightgray')
mp.plot([1,2],[2,1])
# 如果figure中标题已创建，则不会新建窗口，而是将旧窗口置为当前窗口
mp.figure('A Figure',facecolor='gray')
mp.plot([1,2],[2,1])
# 设置窗口的参数
mp.title('A Figure',fontsize=18)
mp.xlabel('time',fontsize=14)
mp.ylabel('price',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.tight_layout()
mp.show()