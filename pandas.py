# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:41:33 2021

@author: 59232
"""

# 导入算法
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# 导入数据
vehicle = pd.read_excel('vehicledata.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

print(vehicle)

# 数据清理

# 清理含有字符串的列
vehicle1 = vehicle.drop(columns=['车型', '轮胎型号', '工况'])

# 清理含有字符串的行
vehicle1 = vehicle1.drop([1, 7, 35]).reset_index(drop=True)

# 增加全部数组随机排序
# vehicle1 = vehicle1.reindex(np.random.permutation(vehicle1.index))

# 设置测试数据的大小
train_size = 28

# 定义训练数据

x_train = vehicle1.iloc[:train_size, :-1].reset_index(drop=True)
y_train = vehicle1.iloc[:train_size, -1].reset_index(drop=True)

# 定义测试数据
x_test = vehicle1.iloc[train_size:, :-1].reset_index(drop=True)
y_test = vehicle1.iloc[train_size:, -1].reset_index(drop=True)
y_test = np.array(y_test)

print(x_train)
print(y_train)
print(x_test)
print(y_test)

# #  增加训练数组随机排序
# vehicle2 = vehicle1.iloc[:train_size, :]
# vehicle2 = vehicle2.reindex(np.random.permutation(vehicle2.index)).reset_index(drop=True)
#
# x_train = vehicle2.iloc[:,:-1].reset_index(drop=True)
# y_train = vehicle2.iloc[:,-1].reset_index(drop=True)
#
# #  增加测试数组随机排序
# vehicle3 = vehicle1.iloc[train_size:, :]
# vehicle3 = vehicle3.reindex(np.random.permutation(vehicle3.index)).reset_index(drop=True)
# x_test = vehicle3.iloc[:,:-1].reset_index(drop=True)
# y_test = vehicle3.iloc[:,-1].reset_index(drop=True)


# 创建算法模型
linear = LinearRegression()
ridge = Ridge()
lasso = Lasso()
elasticnet = ElasticNet()

# 训练模型
linear.fit(x_train, y_train)
ridge.fit(x_train, y_train)
lasso.fit(x_train, y_train)
elasticnet.fit(x_train, y_train)

# 数据预测
y_pre_linear = linear.predict(x_test)
y_pre_ridge = ridge.predict(x_test)
y_pre_lasso = lasso.predict(x_test)
y_pre_elasticnet = elasticnet.predict(x_test)

# 模型评价
linear_score = r2_score(y_test, y_pre_linear)
ridge_score = r2_score(y_test, y_pre_ridge)
lasso_score = r2_score(y_test, y_pre_lasso)
elasticnet_score = r2_score(y_test, y_pre_elasticnet)
display(linear_score, ridge_score, lasso_score, elasticnet_score)

# 绘图，结果可视化

plt.plot(y_test, label='true', color='r', linewidth=3, linestyle='--')
plt.plot(y_pre_linear, label='linear')
plt.plot(y_pre_ridge, label='ridge')
plt.plot(y_pre_lasso, label='lasso')
plt.plot(y_pre_elasticnet, label='elasticnet')
plt.legend()