# 极简方案构建手写数字识别模型

import paddle
from paddle.nn import Linear
import paddle.nn.functional as F
import os
import numpy as np
import matplotlib.pyplot as plt

# 设置数据读取器 API自动读取 MNIST 数据训练集
train_dataset = paddle.vision.datasets.MNIST(mode='train')
train_data0 = np.array(train_dataset[0][0])
train_label_0 = np.array(train_dataset[0][1])

# 显示第一batch的第一个图像
# plt.figure("Image")  # 图像窗口名称
# plt.figure(figsize=(2, 2))
# plt.imshow(train_data0, cmap=plt.cm.binary)
# plt.axis("on")
# plt.title("image")
# plt.show()

# 模型设计

# 定义 mnist 数据识别网络结构，同房价预测网络


class MNIST(paddle.nn.Layer):
    def __init__(self):
        super(MNIST, self).__init__()

        # 定义一层全连接层，输出维度是1
        self.fc = paddle.nn.Linear(in_features=784, out_features=1)

    # 定义网络结构的前向计算过程
    def forward(self, inputs):
        outputs = self.fc(inputs)
        return outputs


# 训练配置

# 声明网络结构
# model = MNIST()

# def train(model):
#     # 启动训练模式
#     model.train()
#     # 加载训练集 batch_size 设为 16
#     train_loader = paddle.io.DataLoader(paddle.vision.datasets.MNIST(
#         mode="train"), batch_size=16, shuffle=True)
#     # 定义优化器，使用随机梯度下降 SGD 优化器，学习率设置为 0.001
#     opt = paddle.optimizer.SGD(
#         learning_rate=0.001, parameters=model.parameters())

# 训练过程

# 训练过程采用二层循环嵌套方式，训练完成后需要保存模型参数，以便后续使用
# 内层循环：负责整个数据集的一次遍历，遍历数据采用分批次（batch）方式
# 外层循环：定义遍历数据集的次数，本次训练中外层循环10次，通过参数 EPOCH_NUM 设置

# 图像归一化函数，将数据范围为[0,255]的图像归一化到[0,1]
def norm_img(img):
    # 验证传入数据格式是否正确，img 的 shape 为[batch_size,28,28]
    assert len(img.shape) == 3
    batch_size, img_h, img_w = img.shape[0], img.shape[1], img.shape[2]
    # 归一化图像数据
    img = img / 255
    # 将图像形式 reshape 为 [batch_size,784]
    img = paddle.reshape(img, [batch_size, img_h * img_w])
    return img


# 确保paddle.vision.datasets.MNIST中加载的图像是
paddle.vision.set_image_backend("cv2")

# 声明网络结构
model = MNIST()


def train(model):
    model.train()
    train_loader = paddle.io.DataLoader(paddle.vision.datasets.MNIST(
        mode="train"), batch_size=16, shuffle=True)
    opt = paddle.optimizer.SGD(
        learning_rate=0.001, parameters=model.parameters())
    EPOCH_NUM = 10
    for epoch in range(EPOCH_NUM):
        for batch_id, data in enumerate(train_loader()):
            images = norm_img(data[0]).astype("float32")
            labels = data[1].astype("float32")

            # 向前计算过程
            predicts = model(images)

            # 计算损失
            loss = F.square_error_cost(predicts, labels)
            avg_loss = paddle.mean(loss)

            # 每训练了1000批次数据，打印下当前loss的情况

            if batch_id % 1000 == 0:
                print("epoch_id:{},batch_id:{},loss is: {}".format(
                    epoch, batch_id, avg_loss.numpy()))

            # 后向传播，更新参数过程

            avg_loss.backward()
            opt.step()
            opt.clear_grad()


train(model)
paddle.save(model.state_dict(), "./mnist.pdparams")
