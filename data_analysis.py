# --*-- conding:utf-8 --*--
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: 读取CSV文件
def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("数据读取成功!")
        return data
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None

# Step 2: 数据分析（简单描述性统计）
def analyze_data(data):
    print("数据基本信息:")
    print(data.info())
    print("\n数据描述统计:")
    print(data.describe())

# Step 3: 绘制散点图
def plot_scatter(data, x_column, y_column):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(data[x_column], data[y_column], alpha=0.5)
        plt.title(f"Scatter Plot of {x_column} vs {y_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        plt.show()
    except KeyError as e:
        print(f"列名错误: {e}")
    except Exception as e:
        print(f"绘图时出错: {e}")

# 主程序入口
if __name__ == "__main__":
    file_path = "your_file.csv"  # 替换为你的CSV文件路径
    data = read_csv(file_path)

    if data is not None:
        analyze_data(data)
        
        # 替换为你的列名
        x_column = "Column1"
        y_column = "Column2"
        
        plot_scatter(data, x_column, y_column)
