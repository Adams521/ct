import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Excel文件路径列表
xls_files = [
    r"loss_excel/FCOS.xlsx",
    r"loss_excel/SAF-FCOS.xlsx",
    r"loss_excel/SAF-FCOS+CBAM.xlsx",
    r"loss_excel/SAF(IMPROVED)-FCOS+CBAM.xlsx"
]
out_names = [
    r"fcos",
    r"fcos+rwef+2cbam",
    r"rac2d",
    r"fcos+rwef",
]

# 单独绘制每个数据集并保存
for i, xls_file in enumerate(xls_files):
    # 读取Excel文件
    df = pd.read_excel(xls_file)
    x = df['x'].values
    y = df['y'].values

    # 初始化图形
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, '-')
    
    # 设置标签和标题
    plt.xlabel('iter.(*1e4)')
    plt.ylabel('error(%)')
    plt.title("loss:"+out_names[i])

    # 保存图形
    plt.savefig(out_names[i]+".png")
    plt.close()  # 关闭当前图形，避免重叠


# 初始化一个图形用于汇总
plt.figure(figsize=(10, 6))

# 再次遍历文件，这次将所有数据集绘制到一张图上
for i, xls_file in enumerate(xls_files):
    # 读取Excel文件
    df = pd.read_excel(xls_file)
    x = df['x'].values
    y = df['y'].values

    # 绘制每个数据集
    plt.plot(x, y, '-', label=out_names[i])

# 设置图例、标签和标题
plt.legend()
plt.xlabel('iter.(*1e4)')
plt.ylabel('error(%)')
plt.title('Loss')

# 保存汇总图形
plt.savefig("All_Data_Comparison.png")
plt.show()