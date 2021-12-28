import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a + b
print(c)

# 创建 ndarray 数组

# 从 list 创建 array

a = [1, 2, 3, 4, 5, 6]
b = np.array(a)
print(b)

# arange 创建元素从0到10依次递增2的数组
a = np.arange(0, 10, 2)
print(a)

# 创建指定长度或形状全0的数组
a = np.zeros([3, 3])
print(a)

# 创建指定长度或形状的全1数组
a = np.ones([3, 3])
print(a)

# 查看 ndarray 数组的属性
# shape: 数组的形状 ndarray.shape, 一维数组(N,),二维数组(M,N),三维数组(M,N,K)
# dtype: 数组的数据类型
# size: 数组的中包含的元素个数 ndarray.size，其大小等于各个维度的长度的乘积
# ndim: 数组的维度大小, ndarray.ndim 其大小等于 ndarray.shape 所包含的元素的个数

a = np.ones([3, 3])
print('a,dtype: {},shape: {},size: {},ndim: {}'.format(
    a.dtype, a.shape, a.size, a.ndim))

# 改变 ndarray 数组的数据类型和形状

# 转化数据类型
b = a.astype(np.int64)
print('b,dtype: {},shape:{}'.format(b.dtype, b.shape))

# 改变形状
c = a.reshape([1, 9])
print('c,dtype: {},shape:{}'.format(c.dtype, c.shape))

# ndarray数组的基本运算

# 标量和 ndarray 数组之间的运算

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(1. / arr)

# 两个 ndarray 数组之间的运算

arr1 = np.array([[1., 2., 3.], [4., 5., 6., ]])
arr2 = np.array([[11., 12., 13.], [21., 22., 23.]])

print(arr2 - arr1)

# ndarray 数组的索引和切片
a = np.arange(30)
print(a)
b = a[4:7]
print(b)

# 将一个标量值赋值给一个切片时，该值会自动传播到整个选区
a = np.arange(30)
a[4:7] = 10
print(a)

# 数组切片产生的新数组，还是指向原来的内存区域，数据不会被复制
# 视图上的任何修改都会直接反映到源数组上
a = np.arange(30)
arr_slice = a[4:7]
arr_slice[0] = 100
print(a, arr_slice)

# 通过 copy 给新数组创建不同的内存空间
a = np.arange(30)
arr_slice = a[4:7]
arr_slice = np.copy(arr_slice)
arr_slice[0] = 100
print(a, arr_slice)

# 多维 ndarray 数组的索引和切片

# 在多维数组中，各索引位置上的元素不再是标量而是多维数组
# 以逗号隔开的索引列表来选取单个元素
# 在多维数组中，如果省略了后面的索引，则返回对象会是一个维度低一点的 ndarray

a = np.arange(30)
arr3d = a.reshape(5, 3, 2)
print(arr3d)
print(arr3d[0])
print(arr3d[0][1])

# 使用 for 语句生成 list
print([k for k in range(0, 6, 2)])

a = np.arange(24)
a = a.reshape([6, 4])
print("a::", a)
slices = [a[k:k+2] for k in range(0, 6, 2)]
print("slices::", slices)

## ndarray 数组的统计方法

# mean 计算算术平均数
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.mean(),arr.dtype)

# 求和
print(arr.sum())

# 求最大值
print(arr.max())

# 求最小值
print(arr.min())

# 指定计算的维度

# 沿着第一维求平均
print(arr.mean(axis = 1))
# 沿着第0维求最大值（第0维指矩阵的每一列）
print(arr.max(axis = 0))
# 沿着第1维求最小值
print(arr.min(axis = 1))
# 计算标准差
print(arr.std())
# 计算方差
print(arr.var())
# 找出最大元素的索引
print(arr.argmax(),arr.argmax(axis = 0),arr.argmax(axis = 1))

## 随机数 np.random

# 设置随机种子
# np.random.seed(10)
a = np.random.rand(3,3)
print(a)

# 均匀分布
a = np.random.rand(3,3)
print(a)
# 生成均匀分布随机数，指定随机数取值范围和数组形状
a = np.random.uniform(low = -1.0,high = 1.0,size=(2,2))
print(a)
# 正态分布
a = np.random.randn(3,3)
print(a)

## 随机打乱 ndarray 数组顺序
a = np.arange(0,30)
np.random.shuffle(a)
print(a)

## 随机选取部分元素
a = np.arange(30)
b = np.random.choice(a,size = 5)
print(b)